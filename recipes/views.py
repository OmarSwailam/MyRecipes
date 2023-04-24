from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)
from .serializers import (
    RecipeSerializer,
    TagSerializer,
    IngredientSerializer,
    ImageSerializer,
)
from .models import Recipe, Tag, Ingredient, Image
from .permissions import (
    IsOwnerOrReadOnly,
    AdminOnlyCanDeletePermission,
    ImagesPermission,
)
from .filters import RecipeFilter


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                "me",
                OpenApiTypes.STR,
                description="true Or false to filter recipes",
            ),
            OpenApiParameter(
                "tags",
                OpenApiTypes.STR,
                description="Comma separated list of tag names to filter",
            ),
            OpenApiParameter(
                "ingredients",
                OpenApiTypes.STR,
                description="Comma separated list of ingredient names to filter",
            ),
        ]
    )
)
class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, RecipeFilter]
    filterset_fields = ["cost", "is_public"]
    ordering_fields = ["duration", "title"]
    search_fields = ["title", "description"]
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return (
            Recipe.objects.filter(
                Q(user_id__exact=self.request.user.id) | Q(is_public__exact=True)
            )
            .select_related("user")
            .prefetch_related("tags")
            .prefetch_related("ingredients")
            .prefetch_related("images")
        )


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [AdminOnlyCanDeletePermission]


class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    permission_classes = [AdminOnlyCanDeletePermission]


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    permission_classes = [ImagesPermission]

    def get_queryset(self):
        return Image.objects.filter(recipe_id=self.kwargs["recipe_pk"])

    def get_serializer_context(self):
        return {"recipe_id": self.kwargs["recipe_pk"]}
