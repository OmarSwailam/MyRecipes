from django.db.models import Q
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import RecipeSerializer
from .models import Recipe
from .permissions import IsOwnerOrReadOnly
from .filters import RecipeFilter


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, RecipeFilter]
    filterset_fields = ["cost", "is_public"]
    ordering_fields = ["duration", "title"]
    search_fields = ["title", "description"]
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Recipe.objects.filter(
            Q(user_id__exact=self.request.user.id) | Q(is_public__exact=True)
        ).select_related("user")

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)
