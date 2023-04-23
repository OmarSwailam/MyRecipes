from django.db.models.query import QuerySet
from rest_framework import serializers
from .models import Recipe, Tag
from django.contrib.auth import get_user_model

User = get_user_model()


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "full_name"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class TagSerializerField(serializers.ListField):
    child = serializers.CharField()

    def to_representation(self, data):
        if isinstance(data, QuerySet):
            # when you retrieve all recipe objects and prefetch their tags field using prefetch_related,
            # you get a queryset that includes the related Tag objects for each Recipe object
            # therefore, you can access the tag names directly from each Tag object in the queryset.
            tags = [tag.name for tag in data]
        else:
            # when you retrieve a single recipe object and access its tags field,
            # you get a related manager object because the tags field is a many-to-many relationship
            # therefore, you need to use the all() method on the related manager object to retrieve
            # the related Tag objects and access their names.
            tags = [tag.name for tag in data.all()]
        return tags


class RecipeSerializer(serializers.ModelSerializer):
    tags = TagSerializerField(required=False)

    class Meta:
        model = Recipe
        fields = [
            "id",
            "title",
            "description",
            "duration",
            "cost",
            "reference_link",
            "is_public",
            "tags",
        ]

    def create(self, validated_data):
        tags = validated_data.pop("tags", None)
        recipe = super(RecipeSerializer, self).create(validated_data)

        # Create a list of Tag objects to be bulk created
        tag_objs = [Tag(name=tag) for tag in tags]

        # Bulk create Tag objects and get their IDs
        created_tags = Tag.objects.bulk_create(tag_objs)

        # Add the created tags to the recipe
        recipe.tags.add(*created_tags)

        return recipe

    def update(self, instance, validated_data):
        tags = validated_data.pop("tags", None)
        recipe = super(RecipeSerializer, self).update(instance, validated_data)

        tag_objs = [Tag(name=tag) for tag in tags]

        created_tags = Tag.objects.bulk_create(tag_objs)

        recipe.tags.add(*created_tags)

        return recipe
