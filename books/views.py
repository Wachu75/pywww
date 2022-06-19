from django.shortcuts import render
from books.models import Book

# Create your views here.
def books_details(request, book_id: int):
    book = Book.objects.get(pk=book_id)
    context = {'book': book}
    return render(request, 'books/details.html', context)


def books_list(request):
    books = Book.objects.all()
    context = {'books_list': books}
    return render(request, 'books/list.html', context)

