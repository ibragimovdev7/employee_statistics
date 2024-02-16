from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, OrderDetailViewSet

router = DefaultRouter()
router.register('list', OrderViewSet,basename='order_all')
router.register('details', OrderDetailViewSet, basename='order_detail')

