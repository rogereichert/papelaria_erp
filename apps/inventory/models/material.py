from django.db import models

from apps.core.models import BaseModel
from apps.inventory.models.category import Category
from apps.inventory.models.supplier import Supplier
from apps.inventory.models.unit_of_measure import UnitOfMeasure

class MaterialType(models.TextChoices):
    SIMPLE = "SIMPLE", "Simples"
    FRACTIONED = "FRACTIONED", "Fracionado"
    PACKAGE = "PACKAGE", "Embalagem"
    KIT = "KIT", "Kit"

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

    material_type = models.CharField(
        max_length=20,
        choices=MaterialType.choices,
        default=MaterialType.SIMPLE,
        verbose_name="Tipo de material",
    )

    purchase_unit = models.ForeignKey(
        UnitOfMeasure,
        on_delete=models.PROTECT,
        related_name="materials_as_purchase_unit",
        verbose_name="Unidade de compra",
    )

    stock_unit = models.ForeignKey(
        UnitOfMeasure,
        on_delete=models.PROTECT,
        related_name="materials_as_stock_unit",
        verbose_name="Unidade de estoque",
    )

    conversion_factor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=1,
        verbose_name="Fator de conversão",
        help_text="Quantidade da unidade de estoque gerada por 1 unidade de compra.",
    )

    current_stock = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Estoque atual",
        help_text="Estoque armazenado sempre na unidade de estoque.",
    )

    minimum_stock = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Estoque mínimo",
        help_text="Estoque mínimo na unidade de estoque.",
    )

    cost_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Preço de custo",
        help_text="Preço de custo por unidade de compra.",
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

    @property
    def stock_display(self):
        return f"{self.current_stock} {self.stock_unit}"

    @property
    def purchase_display(self):
        return f"1 {self.purchase_unit} = {self.conversion_factor} {self.stock_unit}"