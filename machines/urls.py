from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import cached_machine_list
from .viewsets import MachineViewSet

router = DefaultRouter()

router.register('machines', MachineViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('machines/cached', cached_machine_list, name='cached-machine-list')
]

