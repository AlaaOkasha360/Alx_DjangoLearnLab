book = Book.objects.get(title="1984")
book.title = "New Name of the book"
book.save()
book.title
# Output: 'New Name of the book'
