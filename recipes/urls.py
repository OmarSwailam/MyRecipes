from rest_framework_nested import routers
from .views import RecipeViewSet

router = routers.SimpleRouter()
router.register("recipes", RecipeViewSet, basename="recipes")

urlpatterns = router.urls
