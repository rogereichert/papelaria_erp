from django.contrib import messages
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)

from apps.inventory.forms import MaterialForm
from apps.inventory.models import Material
from apps.inventory.services.material_service import (
    update_material,
)


def material_update_view(request, pk):
    material = get_object_or_404(
        Material,
        pk=pk,
    )

    form = MaterialForm(
        request.POST or None,
        instance=material,
    )

    if request.method == "POST":
        if form.is_valid():

            update_material(form=form)

            messages.success(
                request,
                "Material atualizado com sucesso.",
            )

            return redirect("inventory:material_list")

    context = {
        "form": form,
        "material": material,
    }

    return render(
        request,
        "inventory/material/form.html",
        context,
    )