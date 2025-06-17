from django.db import models

from machines.models import Machine
from users.models import CustomUser


# Create your models here.

class MaintenanceOrder(models.Model):
    #--TIPO DE MANUTENÇÃO
    TYPE = [
        ('P', 'Preventive'),
        ('C', 'Corrective')
    ]
    #--STATUS DA MANUTENÇÃO
    STATUS = [
        ('O', 'Open'),
        ('I', 'In Progress'),
        ('C', 'Completed'),
    ]


    machine = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        related_name='maintenance_orders',
    )

    tx_type = models.CharField(
        max_length=1,
        choices=TYPE,
    )

    tx_description = models.CharField(
        max_length=256,
    )

    dt_scheduled = models.DateTimeField()

    tx_status = models.CharField(
        max_length=1,
        choices=STATUS,
        default='O',
    )

    responsible = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    dt_created = models.DateTimeField(
        auto_now_add=True
    )

    dt_updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
      return f"Pedido {self.id} - Máquina: {self.machine.tx_name} - Status: {self.tx_status}"