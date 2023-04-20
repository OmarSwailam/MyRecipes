from rest_framework.serializers import ModelSerializer
from .models import Recipe
from django.contrib.auth import get_user_model

User = get_user_model()


class SimpleUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "full_name"]


class RecipeSerializer(ModelSerializer):
    user = SimpleUserSerializer(read_only=True)

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
        ]
