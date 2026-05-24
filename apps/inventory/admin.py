from django.contrib import admin

from apps.inventory.models import Category, Material, Supplier, StockMovement, UnitOfMeasure


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
    "purchase_unit",
    "stock_unit",
    "conversion_factor",
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
                    "purchase_unit",
                    "stock_unit",
                    "conversion_factor",
                    "current_stock",
                    "minimum_stock",
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

@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = [
        "material",
        "movement_type",
        "purchase_quantity",
        "purchase_unit",
        "converted_quantity",
        "stock_unit",
        "previous_stock",
        "new_stock",
        "created_at",
    ]

    search_fields = [
        "material__name",
        "notes",
    ]

    list_filter = [
        "movement_type",
        "purchase_unit",
        "stock_unit",
        "created_at",
    ]

    readonly_fields = [
        "created_at",
        "updated_at",
    ]

    ordering = [
        "-created_at",
    ]

@admin.register(UnitOfMeasure)
class UnitOfMeasureAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "abbreviation",
        "unit_type",
        "is_active",
    ]

    search_fields = [
        "name",
        "abbreviation",
        "description",
    ]

    list_filter = [
        "unit_type",
        "is_active",
    ]

    ordering = [
        "name",
    ]

    readonly_fields = [
        "created_at",
        "updated_at",
    ]