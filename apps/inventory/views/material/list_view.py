from django.core.paginator import Paginator
from django.shortcuts import render

from apps.inventory.selectors.category_selector import get_active_categories
from apps.inventory.selectors.material_selector import get_filtered_materials


def material_list_view(request):
    search = request.GET.get("search", "")
    category_id = request.GET.get("category", "")
    stock_status = request.GET.get("stock_status", "")

    materials = get_filtered_materials(
        search=search,
        category_id=category_id,
        stock_status=stock_status,
    )

    paginator = Paginator(materials, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "materials": page_obj,
        "page_obj": page_obj,
        "categories": get_active_categories(),
        "search": search,
        "selected_category": category_id,
        "selected_stock_status": stock_status,
        "total_results": paginator.count,
    }

    return render(
        request,
        "inventory/material/list.html",
        context,
    )