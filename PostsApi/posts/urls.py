from django.urls import path
from .views import PostListCreateAPIView, PostDetailAPIView

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post-list-create'),  # For GET and POST
    path('posts/<int:post_id>/', PostDetailAPIView.as_view(), name='post-detail'),  # For GET, PUT, DELETE
]
