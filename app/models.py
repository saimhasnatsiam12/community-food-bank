

from django.db import models


class Family(models.Model):
    family_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    members = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.family_id} - {self.name}"


class FoodStock(models.Model):
    available_packs = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Available: {self.available_packs} packs"


class Distribution(models.Model):
    family = models.ForeignKey(
        Family,
        on_delete=models.CASCADE,
        related_name="distributions"
    )
    packs = models.PositiveIntegerField()
    distributed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.family.family_id} - {self.packs} packs"