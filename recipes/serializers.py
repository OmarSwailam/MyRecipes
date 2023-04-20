from rest_framework.serializers import ModelSerializer
from .models import Recipe, Tag
from django.contrib.auth import get_user_model

User = get_user_model()


class SimpleUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "full_name"]


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class RecipeSerializer(ModelSerializer):
    user = SimpleUserSerializer(read_only=True)
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = [
            "id",
            "user",
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
        auth_user = self.context["request"].user
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(
                user=auth_user,
                **tag,
            )
            recipe.tags.add(tag_obj)

        return recipe
