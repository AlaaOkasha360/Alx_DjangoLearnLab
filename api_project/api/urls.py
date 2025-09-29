from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import BookList, BookViewSet, RegisterView

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')
urlpatterns = [
    path("books/", BookList.as_view(), name="book-list"),  # Maps to the BookList view
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name = 'api-token-auth'),
    path('register/', RegisterView.as_view(), name='register'),
]
