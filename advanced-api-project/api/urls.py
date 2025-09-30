from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.BookListAPIView.as_view()),
    path("books/<int:pk>/", views.BookDetailAPIView.as_view()),
    path("books/create/", views.BookCreateAPIView.as_view()),
    path("books/<int:pk>/update/", views.BookUpdateAPIView.as_view()),
    path('"books/<int:pk>/delete/', views.BookDeleteAPIView.as_view()),
]
