from .models import Author, Book, Library, Librarian


def query_all_book_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)


def list_all_books_in_library(library_name):
    lib_books = Library.objects.get(name=library_name).books.all()


def retrieve_librarian_for_library(library_name):
    librarian = Librarian.objects.get(library__name=library_name)
