from django.shortcuts import render

from apps.inventory.selectors.material_selector import (
    get_all_materials,
)


def material_list_view(request):
    materials = get_all_materials()

    context = {
        "materials": materials,
    }

    return render(
        request,
        "inventory/material/list.html",
        context,
    )