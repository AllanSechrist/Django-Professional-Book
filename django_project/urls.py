from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #Admin
    path("admin/", admin.site.urls),
    #Users
    path("accounts/", include("allauth.urls")),
    #LocaL
    path("", include("pages.urls")),
]
