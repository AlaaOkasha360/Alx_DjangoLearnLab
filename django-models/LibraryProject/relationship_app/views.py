from typing import Any
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Book
# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'books/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library/library_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
