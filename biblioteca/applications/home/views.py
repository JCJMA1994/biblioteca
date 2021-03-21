from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
)


# Create your views here.
class IndexView(TemplateView):
    template_name = "home/index.html"

class ListBook(ListView):
    template_name = "home/list.html"
    queryset = ['El quijote de la mancha', 'Cien años de soledad', 'Codigo Limpio']
    context_object_name = "books"