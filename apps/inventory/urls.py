from django.urls import path

from apps.inventory.views import (
    category_create_view,
    category_delete_view,
    category_list_view,
    category_update_view,

    material_create_view,
    material_delete_view,
    material_list_view,
    material_update_view,

    stock_entry_view,
    stock_movement_list_view,
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

    path(
        "materials/",
        material_list_view,
        name="material_list",
    ),

    path(
        "materials/create/",
        material_create_view,
        name="material_create",
    ),

    path(
        "materials/<uuid:pk>/update/",
        material_update_view,
        name="material_update",
    ),

    path(
        "materials/<uuid:pk>/delete/",
        material_delete_view,
        name="material_delete",
    ),
    path(
        "stock/entry/",
        stock_entry_view,
        name="stock_entry",
    ),
    path(
        "stock/movements/",
        stock_movement_list_view,
        name="stock_movement_list",
    ),
]