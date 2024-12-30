from django.contrib import admin
from .models import Book, BorrowedBook

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published_year', 'available_copies')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('category', 'published_year')

admin.site.register(BorrowedBook)