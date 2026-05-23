from django.contrib import messages
from django.shortcuts import (
    get_object_or_404,
    redirect,
)

from apps.inventory.models import Material
from apps.inventory.services.material_service import (
    deactivate_material,
)


def material_delete_view(request, pk):
    material = get_object_or_404(
        Material,
        pk=pk,
    )

    deactivate_material(material=material)

    messages.success(
        request,
        "Material desativado com sucesso.",
    )

    return redirect("inventory:material_list")