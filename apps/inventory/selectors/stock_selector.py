from apps.inventory.models import StockMovement


def get_stock_movements():
    return (
        StockMovement.objects
        .select_related("material")
        .order_by("-created_at")
    )