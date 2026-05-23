from apps.inventory.models import Material


def get_all_materials():
    return (
        Material.objects
        .select_related(
            "category",
            "supplier",
        )
        .order_by("name")
    )


def get_active_materials():
    return (
        Material.active_objects
        .select_related(
            "category",
            "supplier",
        )
        .order_by("name")
    )


def get_low_stock_materials():
    materials = (
        Material.active_objects
        .select_related(
            "category",
            "supplier",
        )
        .order_by("name")
    )

    return [
        material
        for material in materials
        if material.is_low_stock
    ]


def get_material_by_id(*, material_id):
    return (
        Material.objects
        .select_related(
            "category",
            "supplier",
        )
        .get(id=material_id)
    )