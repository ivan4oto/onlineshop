from stats.views import OrderViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter


app_name = 'stats_api'

router = DefaultRouter()
router.register(r'stats', OrderViewSet, basename='stats')
router.register(r'product', ProductViewSet, basename='product')
urlpatterns = router.urls