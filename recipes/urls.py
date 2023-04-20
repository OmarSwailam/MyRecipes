from rest_framework_nested import routers
from .views import RecipeViewSet, TagViewSet

router = routers.SimpleRouter()
router.register("recipes", RecipeViewSet, basename="recipes")
router.register("tags", TagViewSet, basename="tags")

urlpatterns = router.urls
