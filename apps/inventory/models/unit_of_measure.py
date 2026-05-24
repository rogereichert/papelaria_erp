from django.db import models

from apps.core.models import BaseModel


class UnitType(models.TextChoices):
    UNIT = "UNIT", "Unidade"
    PACKAGE = "PACKAGE", "Embalagem"
    WEIGHT = "WEIGHT", "Peso"
    LENGTH = "LENGTH", "Comprimento"
    VOLUME = "VOLUME", "Volume"
    AREA = "AREA", "Área"


class UnitOfMeasure(BaseModel):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nome",
    )

    abbreviation = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Abreviação",
    )

    unit_type = models.CharField(
        max_length=20,
        choices=UnitType.choices,
        default=UnitType.UNIT,
        verbose_name="Tipo",
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descrição",
    )

    class Meta:
        verbose_name = "Unidade de medida"
        verbose_name_plural = "Unidades de medida"
        ordering = ["name"]

    def __str__(self):
        return self.abbreviation