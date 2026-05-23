from django.shortcuts import render

from apps.inventory.selectors.stock_selector import (
    get_stock_movements,
)


def stock_movement_list_view(request):
    movements = get_stock_movements()

    context = {
        "movements": movements,
    }

    return render(
        request,
        "inventory/stock/list.html",
        context,
    )