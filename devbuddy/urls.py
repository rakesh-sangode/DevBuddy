from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("base.urls")),
]
