from django.db import models

class Machine(models.Model):
    STATUS = (
        ("O", "Operational"),
        ("S", "Stopped"),
        ("M", "Maintenance"),
    )

    tx_name = models.CharField(
        max_length=50,
        unique=True
    )
    tx_location = models.CharField(
        max_length=50,
        unique=False
    )
    tx_status = models.CharField(
        max_length=1,
        choices=STATUS,
        default='O'
    )