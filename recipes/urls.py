from rest_framework_nested import routers
from .views import RecipeViewSet, TagViewSet, IngredientViewSet

router = routers.SimpleRouter()
router.register("recipes", RecipeViewSet, basename="recipes")
router.register("tags", TagViewSet, basename="tags")
router.register("ingredients", IngredientViewSet, basename="ingredients")

urlpatterns = router.urls
