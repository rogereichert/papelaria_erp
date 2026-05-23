from django.contrib import admin

from apps.inventory.models import Category, Material, Supplier


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "is_active",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "name",
        "description",
    ]
    list_filter = [
        "is_active",
        "created_at",
    ]
    ordering = [
        "name",
    ]

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "document",
        "phone",
        "email",
        "is_active",
    ]
    search_fields = [
        "name",
        "document",
        "phone",
        "email",
    ]
    list_filter = [
        "is_active",
        "created_at",
    ]
    ordering = [
        "name",
    ]

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "category",
        "supplier",
        "current_stock",
        "minimum_stock",
        "unit",
        "cost_price",
        "is_active",
    ]
    search_fields = [
        "name",
        "description",
        "category__name",
        "supplier__name",
    ]
    list_filter = [
        "category",
        "supplier",
        "is_active",
        "created_at",
    ]
    ordering = [
        "name",
    ]
    readonly_fields = [
        "created_at",
        "updated_at",
    ]
    fieldsets = [
        (
            "Identificação",
            {
                "fields": [
                    "name",
                    "category",
                    "supplier",
                    "description",
                ]
            },
        ),
        (
            "Estoque",
            {
                "fields": [
                    "current_stock",
                    "minimum_stock",
                    "unit",
                ]
            },
        ),
        (
            "Financeiro",
            {
                "fields": [
                    "cost_price",
                ]
            },
        ),
        (
            "Controle",
            {
                "fields": [
                    "is_active",
                    "created_at",
                    "updated_at",
                ]
            },
        ),
    ]