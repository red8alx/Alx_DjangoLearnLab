from django.contrib import admin
from .models import Author, Book, Library, Librarian

# Add admin classes that can be use adminstrator each model here.
class authorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

# Register your models here.
admin.site.register(Author,authorAdmin )
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
