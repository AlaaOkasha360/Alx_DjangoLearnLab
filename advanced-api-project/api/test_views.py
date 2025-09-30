from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")
        self.author = Author.objects.create(name="George Orwell")
        self.book = Book.objects.create(
            title="1984", publication_year=1949, author=self.author
        )
        self.valid_book_data = {
            "title": "Animal Farm",
            "publication_year": 1945,
            "author": self.author.id,
        }
        self.invalid_book_data = {
            "title": "Future Book",
            "publication_year": 3000,
            "author": self.author.id,
        }

    def test_list_books(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_book_detail(self):
        url = reverse("book-detail", args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "1984")

    def test_create_book_valid(self):
        url = reverse("book-create")
        response = self.client.post(url, self.valid_book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Animal Farm")

    def test_create_book_invalid_year(self):
        url = reverse("book-create")
        response = self.client.post(url, self.invalid_book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_book(self):
        url = reverse("book-update", args=[self.book.id])
        update_data = {
            "title": "Nineteen Eighty-Four",
            "publication_year": 1949,
            "author": self.author.id,
        }
        response = self.client.put(url, update_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Nineteen Eighty-Four")

    def test_delete_book(self):
        url = reverse("book-delete", args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())
