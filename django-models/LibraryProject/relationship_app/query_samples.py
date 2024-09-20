
from .models import Author, Book, Library, Librarian
author = Author.objects.get(name="Rediet A.")
books = Book.objects.filter(author=author)
for i in books:
    print(i.title)