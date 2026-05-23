from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect

from apps.inventory.models import Category
from apps.inventory.services.category_service import (
    deactivate_category,
)


def category_delete_view(request, pk):
    category = get_object_or_404(
        Category,
        pk=pk,
    )

    deactivate_category(category=category)

    messages.success(
        request,
        "Categoria desativada com sucesso.",
    )

    return redirect("inventory:category_list")