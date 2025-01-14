from django.urls import path
from .views import (
    CreateBlogPostView,
    ListBlogPostView,
    DetailBlogPostView,
    UpdateBlogPostView,
    DeleteBlogPostView,
)

app_name = 'blog'

urlpatterns = [
    path('create/', CreateBlogPostView.as_view(), name='create'),
    path('list/', ListBlogPostView.as_view(), name='list'),
    path('list/<int:pk>/', DetailBlogPostView.as_view(), name='detail'),
    path('update/<int:pk>/', UpdateBlogPostView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteBlogPostView.as_view(), name='delete'),
]