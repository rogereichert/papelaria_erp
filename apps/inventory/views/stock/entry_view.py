from django.contrib import messages
from django.shortcuts import redirect, render

from apps.inventory.forms import StockEntryForm
from apps.inventory.services.stock_service import register_stock_entry


def stock_entry_view(request):
    form = StockEntryForm(request.POST or None)

    material_id = request.GET.get("material")

    if material_id and request.method == "GET":
        form.fields["material"].initial = material_id

    if request.method == "POST":
        if form.is_valid():
            register_stock_entry(
                material=form.cleaned_data["material"],
                quantity=form.cleaned_data["quantity"],
                notes=form.cleaned_data["notes"],
            )

            messages.success(
                request,
                "Entrada de estoque registrada com sucesso.",
            )

            return redirect("inventory:material_list")

    context = {
        "form": form,
    }

    return render(
        request,
        "inventory/stock/entry.html",
        context,
    )