from django.contrib import messages
from django.shortcuts import redirect, render

from apps.inventory.forms import CategoryForm
from apps.inventory.services.category_service import (
    create_category,
)


def category_create_view(request):
    form = CategoryForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            create_category(form=form)

            messages.success(
                request,
                "Categoria cadastrada com sucesso.",
            )

            return redirect("inventory:category_list")

    context = {
        "form": form,
    }

    return render(
        request,
        "inventory/category/form.html",
        context,
    )