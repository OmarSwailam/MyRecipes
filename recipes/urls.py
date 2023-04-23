from rest_framework_nested import routers
from .views import RecipeViewSet, TagViewSet, IngredientViewSet, ImageViewSet

router = routers.SimpleRouter()
router.register("recipes", RecipeViewSet, basename="recipes")
router.register("tags", TagViewSet, basename="tags")
router.register("ingredients", IngredientViewSet, basename="ingredients")

recipes_router = routers.NestedDefaultRouter(router, "recipes", lookup="recipe")
recipes_router.register("images", ImageViewSet, basename="recipe-image")

urlpatterns = router.urls + recipes_router.urls
