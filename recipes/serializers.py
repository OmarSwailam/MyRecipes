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


class RecipeSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

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
        tags = validated_data.pop("tags", [])
        recipe = Recipe.objects.create(**validated_data)

        # Create a list of Tag objects to be bulk created
        tag_objs = [Tag(**tag) for tag in tags]

        # Bulk create Tag objects and get their IDs
        created_tags = Tag.objects.bulk_create(tag_objs)

        # Add the created tags to the recipe
        recipe.tags.add(*created_tags)

        return recipe

    def update(self, instance, validated_data):
        tags = validated_data.pop("tags", [])
        recipe = Recipe.objects.update(instance, validated_data)

        tag_objs = [Tag(**tag) for tag in tags]

        created_tags = Tag.objects.bulk_create(tag_objs)

        recipe.tags.add(*created_tags)

        return recipe
