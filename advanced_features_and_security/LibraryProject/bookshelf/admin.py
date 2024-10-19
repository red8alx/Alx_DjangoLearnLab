from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
class bookAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'publication_year')
    search_fields = ('title','author')
    list_filter = ('publication_year',)

admin.site.register(Book, bookAdmin)
#Integrate the Custom User Model into Admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    list_display = ('email', 'is_staff', 'date_of_birth', 'username', 'profile_photo')

admin.site.register(CustomUser, CustomUserAdmin)