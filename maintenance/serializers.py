from rest_framework import serializers
from .models import MaintenanceOrder

class MaintenanceOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceOrder
        fields = '__all__'