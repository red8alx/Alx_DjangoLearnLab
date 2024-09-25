from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import DetailView
from .models import Book, Library


# Create your views here.
def index(request):
    return HttpResponse("Hello, Welcome to the relationship_app page.")

#Function-based views
def list_books(request):
    books = Book.objects.all() #fetching all books from the database
    context = {'list_books':books} #creates a context dictionary with list of books
    return render(request, 'list_books.html', context)