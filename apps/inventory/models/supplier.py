from django.db import models

from apps.core.models import BaseModel


class Supplier(BaseModel):
    name = models.CharField(
        max_length=150,
        verbose_name="Nome",
    )
    document = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="CPF/CNPJ",
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Telefone",
    )
    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name="E-mail",
    )

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
        ordering = ["name"]

    def __str__(self):
        return self.name