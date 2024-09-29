from django.urls import path

from . import views
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.index, name="index"), 
    path("list_books/", list_books, name="list_books"),
    path("library_detail/", views.LibraryDetailView.as_view(), name="library_detail"),
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),

]