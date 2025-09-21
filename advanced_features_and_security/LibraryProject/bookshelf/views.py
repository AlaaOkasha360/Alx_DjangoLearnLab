from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.db.models import Q
from django.shortcuts import render
from .models import Book
from .forms import BookSearchForm
# Create your views here.


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get("query")
        if query:
            # Safe ORM query (prevents SQL injection)
            books = books.filter(Q(title__icontains=query) | Q(author__icontains=query))

    return render(request, "bookshelf/book_list.html", {"books": books, "form": form})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    return render(request, 'bookshelf/book_create.html')

@permission_required('relationship_app.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/book_edit.html', {'book': book})

@permission_required('relationship_app.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/book_delete.html', {'book': book})