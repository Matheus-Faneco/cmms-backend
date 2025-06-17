from rest_framework import viewsets
from .models import MaintenanceOrder
from .serializers import MaintenanceOrderSerializer

class MaintenanceOrderViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceOrder.objects.all()
    serializer_class = MaintenanceOrderSerializer