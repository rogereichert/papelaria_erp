from django.urls import path

from apps.inventory.views import (
    category_create_view,
    category_delete_view,
    category_list_view,
    category_update_view,
)

app_name = "inventory"

urlpatterns = [
    path(
        "categories/",
        category_list_view,
        name="category_list",
    ),

    path(
        "categories/create/",
        category_create_view,
        name="category_create",
    ),

    path(
        "categories/<uuid:pk>/update/",
        category_update_view,
        name="category_update",
    ),

    path(
        "categories/<uuid:pk>/delete/",
        category_delete_view,
        name="category_delete",
    ),
]