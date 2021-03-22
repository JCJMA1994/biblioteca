from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
)
from .models import Author, Book


# Create your views here.


class ListAuthor(ListView):
    template_name = "libreria/list-author.html"
    model = Author
    context_object_name = 'authors'


class ListBooksAuthor(ListView):
    template_name = "libreria/list-books.html"
    context_object_name = 'books'

    def get_queryset(self):
        id = self.kwargs['pk']
        lista = Book.objects.filter(
            author=id
        )

        return lista

class AddAuthor(CreateView):
    template_name = "libreria/add-author.html"
    model = Author
    fields = [
        'name',
        'lastname',
        'nationality',
    ]
    success_url = '/'