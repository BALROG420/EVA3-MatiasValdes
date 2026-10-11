from rest_framework.routers import DefaultRouter
from .views import BandaViewSet

router = DefaultRouter()
router.register('bandas', BandaViewSet)