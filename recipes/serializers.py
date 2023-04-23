from django.db.models.query import QuerySet
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Recipe, Tag, Ingredient, Image

User = get_user_model()


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "full_name"]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "image"]


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["id", "name", "amount", "amount_type"]


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
    user = SimpleUserSerializer(read_only=True)
    tags = TagSerializerField(required=False)
    ingredients = IngredientSerializer(many=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )
    images = ImageSerializer(read_only=True, many=True)

    class Meta:
        model = Recipe
        fields = [
            "id",
            "user",
            "title",
            "description",
            "duration",
            "duration_type",
            "cost",
            "reference_link",
            "is_public",
            "tags",
            "ingredients",
            "uploaded_images",
            "images",
        ]

    def validate_ingredients(self, attrs):
        if len(attrs) == 0:
            raise serializers.ValidationError("At least one ingredient required")
        return attrs

    def _create_ingredients(self, ingredients, recipe):
        # Create a list of X objects to be bulk created
        ingredient_objs = [Ingredient(**ingredient) for ingredient in ingredients]
        # Bulk create X objects "bulk_create also check for redundancy"
        created_ingredients = Ingredient.objects.bulk_create(ingredient_objs)
        # Add the created objects to the recipe
        recipe.ingredients.clear()
        recipe.ingredients.add(*created_ingredients)

    def _create_tags(self, tags, recipe):
        tag_objs = [Tag(name=tag) for tag in tags]
        created_tags = Tag.objects.bulk_create(tag_objs)
        recipe.tags.clear()
        recipe.tags.add(*created_tags)

    def _create_images(self, images, recipe):
        # Image.objects.filter(recipe=recipe).delete()
        image_objects = [Image(recipe=recipe, image=image) for image in images]
        Image.objects.bulk_create(image_objects)

    def create(self, validated_data):
        tags = validated_data.pop("tags", [])
        ingredients = validated_data.pop("ingredients", [])
        images = validated_data.pop("uploaded_images", [])
        recipe = Recipe.objects.create(
            user=self.context["request"].user, **validated_data
        )
        self._create_tags(tags, recipe)
        self._create_ingredients(ingredients, recipe)
        self._create_images(images, recipe)
        return recipe

    def update(self, instance, validated_data):
        tags = validated_data.pop("tags", [])
        ingredients = validated_data.pop("ingredients", [])
        images = validated_data.pop("uploaded_images", [])
        recipe = super(RecipeSerializer, self).update(instance, validated_data)
        self._create_tags(tags, recipe)
        self._create_ingredients(ingredients, recipe)
        self._create_images(images, recipe)
        return recipe
