from .models import Author, Book, Library, Librarian

books = Book.objects.filter(author__name = "Alaa")

lib_books = Library.objects.get(name="House").books.all()

librarian = Librarian.objects.get(library__name = "House")
