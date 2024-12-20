"""
URL configuration for flyhub_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


class ApiRootView(APIView):
    """
    Головна сторінка для /api/.
    """
    def get(self, request, *args, **kwargs):
        return Response({
            "user-create":
                request.build_absolute_uri(reverse(
                    "user:create"
                )),
            "user-manage":
                request.build_absolute_uri(reverse(
                    "user:manage"
                )),
            "flyhub-airplane-list":
                request.build_absolute_uri(reverse(
                    "flyhub_manager:airplane-list"
                )),
            "flyhub-airplane-type":
                request.build_absolute_uri(reverse(
                    "flyhub_manager:airplanetype-list"
                )),
            "flyhub-airports":
                request.build_absolute_uri(reverse(
                    "flyhub_manager:airports-list"
                )),
            "flyhub-crew":
                request.build_absolute_uri(reverse(
                    "flights:flight-list"
                )),
            "flights":
                request.build_absolute_uri(reverse(
                    "flights:flight-list"
                )),
            "orders-orders":
                request.build_absolute_uri(reverse(
                    "orders:order-list"
                )),
            "orders-tickets":
                request.build_absolute_uri(reverse(
                    "orders:ticket-list"
                )),
            "routes":
                request.build_absolute_uri(reverse(
                    "routes:route-list"
                )),
            "token-login":
                request.build_absolute_uri(reverse("token")),
            "token-refresh":
                request.build_absolute_uri(reverse("token_refresh")),
        })


urlpatterns = [
    # ADMIN_PANEL
    path("admin/", admin.site.urls),
    # ALL API
    path("api/", ApiRootView.as_view(), name="api-root"),
    # USER
    path("api/user/", include("user.urls", namespace="user")),
    # FLYNUB_MANAGER
    path(
        "api/flyhub/",
        include(
            "flyhub_manager.urls",
            namespace="flyhub_manager"
        )
    ),
    path(
        "api/routes/",
        include(
            "routes.urls",
            namespace="routes"
        )
    ),
    path(
        "api/orders/",
        include(
            "orders.urls",
            namespace="orders"
        )
    ),
    path(
        "api/flights/",
        include(
            "flights.urls",
            namespace="flights"
        )
    ),
    # JWT
    path(
        "api/token/",
        TokenObtainPairView.as_view(),
        name="token"
    ),
    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),
    # DEBUG_TOOL_BAR
    path("__debug__/", include("debug_toolbar.urls")),
]
