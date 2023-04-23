from rest_framework.filters import BaseFilterBackend


class RecipeFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        tags = request.query_params.getlist("tags", None)
        if tags:
            queryset = queryset.filter(tags__name__in=tags).distinct()
        ingredients = request.query_params.getlist("ingredients", None)
        if ingredients:
            queryset = queryset.filter(ingredients__name__in=ingredients).distinct()
        me = request.query_params.get("me")
        if me:
            if me.lower() == "true":
                queryset = queryset.filter(user_id=request.user)
            elif me.lower() == "false":
                queryset = queryset.exclude(user_id=request.user)
        return queryset
