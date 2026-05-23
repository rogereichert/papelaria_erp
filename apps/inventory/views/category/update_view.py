from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from apps.inventory.forms import CategoryForm
from apps.inventory.models import Category
from apps.inventory.services.category_service import (
    update_category,
)


def category_update_view(request, pk):
    category = get_object_or_404(
        Category,
        pk=pk,
    )

    form = CategoryForm(
        request.POST or None,
        instance=category,
    )

    if request.method == "POST":
        if form.is_valid():
            update_category(form=form)

            messages.success(
                request,
                "Categoria atualizada com sucesso.",
            )

            return redirect("inventory:category_list")

    context = {
        "form": form,
        "category": category,
    }

    return render(
        request,
        "inventory/category/form.html",
        context,
    )