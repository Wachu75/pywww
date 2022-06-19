from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin

from .models import Book, Author

class BookResource(resources.ModelResource):
    class Meta:
        model = Book

class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title","description"]


#admin.site.register(Book, BookAdmin)