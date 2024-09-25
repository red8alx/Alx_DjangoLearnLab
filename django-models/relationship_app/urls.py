from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("list_books/", views.list_books, name="list_books"),
]