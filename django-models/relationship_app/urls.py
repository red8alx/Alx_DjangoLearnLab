from django.urls import path

from . import views list_books


urlpatterns = [
    path("", views.index, name="index"), 
    path("list_books/", views.list_books, name="list_books"),
    path("library_detail/", views.LibraryDetailView.as_view(), name="library_detail"),

]