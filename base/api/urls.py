from django.urls import path 
from . import views

urlpatterns = [
    path('posts/', views.posts),
    path('posts/<str:pk>/', views.posts_detail),
    path('posts/edit/<str:pk>/', views.posts_edit),
    path('sidebar/', views.sidebar),
]