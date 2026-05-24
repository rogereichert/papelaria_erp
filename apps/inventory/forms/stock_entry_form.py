from django import forms

from apps.inventory.models import Material


class StockEntryForm(forms.Form):
    material = forms.ModelChoiceField(
        queryset=Material.active_objects.all(),
        label="Material",
        widget=forms.Select(
            attrs={
                "class": "form-select",
            }
        ),
    )

    quantity = forms.DecimalField(
        label="Quantidade comprada",
        min_value=0.01,
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "step": "0.01",
                "placeholder": "Ex: 2 pacotes, 3 caixas, 5 resmas",
            }
        ),
    )

    notes = forms.CharField(
        label="Observações",
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Ex: compra realizada, ajuste de entrada, fornecedor...",
            }
        ),
    )