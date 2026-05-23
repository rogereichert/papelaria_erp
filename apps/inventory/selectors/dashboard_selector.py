from apps.inventory.models import (
    Material,
    StockMovement,
)


def get_dashboard_metrics():
    total_materials = Material.active_objects.count()

    low_stock_count = len([
        material
        for material in Material.active_objects.all()
        if material.is_low_stock
    ])

    recent_movements = (
        StockMovement.objects
        .select_related("material")
        .order_by("-created_at")[:5]
    )

    return {
        "total_materials": total_materials,
        "low_stock_count": low_stock_count,
        "recent_movements": recent_movements,
    }