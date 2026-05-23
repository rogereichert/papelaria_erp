from apps.inventory.models import Category


def create_category(*, form):
    category = form.save()

    return category


def update_category(*, form):
    category = form.save()

    return category


def deactivate_category(*, category: Category):
    category.is_active = False
    category.save(
        update_fields=[
            "is_active",
            "updated_at",
        ]
    )

    return category