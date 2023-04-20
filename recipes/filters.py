from rest_framework.filters import BaseFilterBackend


class RecipeFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if "me" in request.query_params:
            me = request.query_params.get("me")
            if me.lower() == "true":
                queryset = queryset.filter(user_id=request.user)
            elif me.lower() == "false":
                queryset = queryset.exclude(user_id=request.user)
        return queryset
