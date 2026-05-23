from apps.inventory.models import Category


def get_categories():
    return (
        Category.objects
        .order_by("name")
    )


def get_active_categories():
    return (
        Category.active_objects
        .order_by("name")
    )