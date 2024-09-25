from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import DetailView
from .models import Book
from .models import Library
from typing import Any
from django.views.generic.detail import DetailView

# Create your views here.
def index(request):
    return HttpResponse("Hello, Welcome to the relationship_app page.")

#Function-based views
def list_books(request):
    books = Book.objects.all() #fetching all books from the database
    context = {'list_books':books} #creates a context dictionary with list of books
    return render(request, 'relationship_app/list_books.html', context)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        #library = self.get_object()
        library = Library.objects.all()
        #context['books_list'] = library.get_books_list()
        context = {'library_list': library}
        return context