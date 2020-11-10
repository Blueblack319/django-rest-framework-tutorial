from django.urls import path, include
from snippets import views

urlpatterns = [
    path("", views.api_root),
    path("api-auth/", include("rest_framework.urls")),
]
