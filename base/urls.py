from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index),
    path('posts/<str:pk>/', views.post_detail),
]