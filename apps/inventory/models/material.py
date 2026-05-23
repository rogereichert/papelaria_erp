from django.db import models

from apps.core.models import BaseModel
from apps.inventory.models.category import Category
from apps.inventory.models.supplier import Supplier


class Material(BaseModel):
    name = models.CharField(
        max_length=150,
        verbose_name="Nome",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="materials",
        verbose_name="Categoria",
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.SET_NULL,
        related_name="materials",
        blank=True,
        null=True,
        verbose_name="Fornecedor",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descrição",
    )

    current_stock = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Estoque atual",
    )
    minimum_stock = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Estoque mínimo",
    )
    unit = models.CharField(
        max_length=20,
        default="un",
        verbose_name="Unidade",
    )

    cost_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Preço de custo",
    )

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiais"
        ordering = ["name"]

    def __str__(self):
        return self.name

    @property
    def is_low_stock(self):
        return self.current_stock <= self.minimum_stock