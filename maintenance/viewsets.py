from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import MaintenanceOrder
from .serializers import MaintenanceOrderSerializer

class MaintenanceOrderViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceOrder.objects.all()
    serializer_class = MaintenanceOrderSerializer
    filter_backend = [DjangoFilterBackend]
    filterset_fields = ['tx_status', 'tx_type', 'machine']