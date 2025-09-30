from django.urls import path
from .views import (
    CommentCreateView,
    CommentDeleteView,
    CommentUpdateView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path("post/", PostListView.as_view(), name="post-list"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path(
        "post/<int:post_pk>/comments/new/",
        CommentCreateView.as_view(),
        name="comment-create",
    ),
    path("comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment-update"),
    path(
        "comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"
    ),
]
