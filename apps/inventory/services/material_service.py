from apps.inventory.models import Material


def create_material(*, form):
    material = form.save()

    return material


def update_material(*, form):
    material = form.save()

    return material


def deactivate_material(*, material: Material):
    material.is_active = False

    material.save(
        update_fields=[
            "is_active",
            "updated_at",
        ]
    )

    return material