from django.urls import path
from books.views import books_list, books_details


app_name = "books"

urlpatterns = [
    path('', books_list, name="list"),
    path('<int:book_id>', books_details, name="details"),
]