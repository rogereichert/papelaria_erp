from django.db import models

from apps.core.models import BaseModel
from apps.inventory.models.material import Material


class MovementType(models.TextChoices):
    ENTRY = "ENTRY", "Entrada"
    OUTPUT = "OUTPUT", "Saída"
    ADJUSTMENT = "ADJUSTMENT", "Ajuste"


class StockMovement(BaseModel):
    material = models.ForeignKey(
        Material,
        on_delete=models.PROTECT,
        related_name="movements",
        verbose_name="Material",
    )

    movement_type = models.CharField(
        max_length=20,
        choices=MovementType.choices,
        verbose_name="Tipo de movimentação",
    )

    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Quantidade",
    )

    previous_stock = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Estoque anterior",
    )

    new_stock = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Novo estoque",
    )

    notes = models.TextField(
        blank=True,
        null=True,
        verbose_name="Observações",
    )

    class Meta:
        verbose_name = "Movimentação de estoque"
        verbose_name_plural = "Movimentações de estoque"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.material} - {self.get_movement_type_display()}"