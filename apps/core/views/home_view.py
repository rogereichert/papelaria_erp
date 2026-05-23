from django.shortcuts import render

from apps.inventory.selectors.dashboard_selector import (
    get_dashboard_metrics,
)


def home_view(request):
    context = get_dashboard_metrics()

    return render(
        request,
        "core/home.html",
        context,
    )