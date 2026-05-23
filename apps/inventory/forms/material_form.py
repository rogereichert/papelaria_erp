from django import forms

from apps.inventory.models import Material


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material

        fields = [
            "name",
            "category",
            "supplier",
            "description",
            "current_stock",
            "minimum_stock",
            "unit",
            "cost_price",
            "is_active",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nome do material",
                }
            ),

            "category": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "supplier": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Descrição do material",
                }
            ),

            "current_stock": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                }
            ),

            "minimum_stock": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                }
            ),

            "unit": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex: un, cx, pct",
                }
            ),

            "cost_price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                }
            ),

            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }