from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .viewsets import MachineSerializer, MachineViewSet

router = DefaultRouter()

router.register('machines', MachineViewSet)

urlpatterns = [
    path('', include(router.urls))
]

