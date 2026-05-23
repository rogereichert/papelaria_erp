from django.contrib import messages
from django.shortcuts import redirect, render

from apps.inventory.forms import MaterialForm
from apps.inventory.services.material_service import (
    create_material,
)


def material_create_view(request):
    form = MaterialForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():

            create_material(form=form)

            messages.success(
                request,
                "Material cadastrado com sucesso.",
            )

            return redirect("inventory:material_list")

    context = {
        "form": form,
    }

    return render(
        request,
        "inventory/material/form.html",
        context,
    )