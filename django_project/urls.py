from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #Admin
    path("admin/", admin.site.urls),
    #Users
    path("accounts/", include("django.contrib.auth.urls")),
    #Local
    path("accounts/", include("accounts.urls")),
    path("", include("pages.urls")),
]
