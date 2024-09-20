from relationship_app.models import Author, Book, Library, Librarian

#Query all books by a specific author.
author_name = "author_name"
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)
for book in books:
    print(book.title)
#List all books in a library.

#Retrieve the librarian for a library.