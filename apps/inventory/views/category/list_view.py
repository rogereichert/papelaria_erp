from django.shortcuts import render

from apps.inventory.selectors.category_selector import (
    get_categories,
)


def category_list_view(request):
    categories = get_categories()

    context = {
        "categories": categories,
    }

    return render(
        request,
        "inventory/category/list.html",
        context,
    )