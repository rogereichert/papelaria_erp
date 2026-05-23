from django.db.models import F, Q

from apps.inventory.models import Material


def get_all_materials():
    return (
        Material.objects
        .select_related("category", "supplier")
        .order_by("name")
    )


def get_active_materials():
    return (
        Material.active_objects
        .select_related("category", "supplier")
        .order_by("name")
    )


def get_filtered_materials(*, search=None, category_id=None, stock_status=None):
    materials = (
        Material.objects
        .select_related("category", "supplier")
        .order_by("name")
    )

    if search:
        materials = materials.filter(
            Q(name__icontains=search)
            | Q(description__icontains=search)
            | Q(category__name__icontains=search)
            | Q(supplier__name__icontains=search)
        )

    if category_id:
        materials = materials.filter(category_id=category_id)

    if stock_status == "low":
        materials = materials.filter(
            current_stock__lte=F("minimum_stock")
        )

    if stock_status == "normal":
        materials = materials.filter(
            current_stock__gt=F("minimum_stock")
        )

    return materials


def get_low_stock_materials():
    return (
        Material.active_objects
        .select_related("category", "supplier")
        .filter(current_stock__lte=F("minimum_stock"))
        .order_by("name")
    )


def get_material_by_id(*, material_id):
    return (
        Material.objects
        .select_related("category", "supplier")
        .get(id=material_id)
    )