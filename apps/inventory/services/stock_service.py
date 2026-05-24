from decimal import Decimal

from django.db import transaction

from apps.inventory.models import Material, StockMovement
from apps.inventory.models.stock_movement import MovementType


def calculate_converted_quantity(
    *,
    material: Material,
    purchase_quantity: Decimal,
):
    return purchase_quantity * material.conversion_factor


@transaction.atomic
def register_stock_entry(
    *,
    material: Material,
    quantity: Decimal,
    notes: str = "",
):
    converted_quantity = calculate_converted_quantity(
        material=material,
        purchase_quantity=quantity,
    )

    previous_stock = material.current_stock
    new_stock = previous_stock + converted_quantity

    material.current_stock = new_stock

    material.save(
        update_fields=[
            "current_stock",
            "updated_at",
        ]
    )

    StockMovement.objects.create(
        material=material,
        movement_type=MovementType.ENTRY,

        purchase_quantity=quantity,
        purchase_unit=material.purchase_unit,

        converted_quantity=converted_quantity,
        stock_unit=material.stock_unit,

        previous_stock=previous_stock,
        new_stock=new_stock,

        notes=notes,
    )

    return material


@transaction.atomic
def register_stock_output(
    *,
    material: Material,
    quantity: Decimal,
    notes: str = "",
):
    previous_stock = material.current_stock

    if quantity > previous_stock:
        raise ValueError("Estoque insuficiente.")

    new_stock = previous_stock - quantity

    material.current_stock = new_stock

    material.save(
        update_fields=[
            "current_stock",
            "updated_at",
        ]
    )

    StockMovement.objects.create(
        material=material,
        movement_type=MovementType.OUTPUT,

        purchase_quantity=quantity,
        purchase_unit=material.stock_unit,

        converted_quantity=quantity,
        stock_unit=material.stock_unit,

        previous_stock=previous_stock,
        new_stock=new_stock,

        notes=notes,
    )

    return material