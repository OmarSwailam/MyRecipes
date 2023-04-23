from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import RecipeSerializer, TagSerializer, IngredientSerializer
from .models import Recipe, Tag, Ingredient
from .permissions import IsOwnerOrReadOnly, AdminOnlyCanDeletePermission
from .filters import RecipeFilter


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
        )


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [AdminOnlyCanDeletePermission]


class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    permission_classes = [AdminOnlyCanDeletePermission]
