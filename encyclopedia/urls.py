from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.name, name="name"),
    path("search/", views.search, name="search"),
    path("newpage/", views.newpage, name="newpage"),
    path("edit/", views.edit, name="edit"),
    path("saveedit/", views.saveedit, name="saveedit"),
    path("ran/", views.ran, name="ran")
]
