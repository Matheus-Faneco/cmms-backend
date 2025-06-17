from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import MaintenanceOrderViewSet

router = DefaultRouter()
router.register(r'maintenanceorders', MaintenanceOrderViewSet)

urlpatterns = [
    path('', include(router.urls))
]