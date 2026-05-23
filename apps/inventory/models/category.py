from django.db import models

from apps.core.models import BaseModel


class Category(BaseModel):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nome",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descrição",
    )

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["name"]

    def __str__(self):
        return self.name