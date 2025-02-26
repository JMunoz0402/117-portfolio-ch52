from django.urls import path
from .import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.project_list_view, name="project_list"),
    path("new_project/", views.project_new_view, name="project_new"),
]