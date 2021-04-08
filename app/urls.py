from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('index/', views.index, name='index'),
    path('create/', views.CreatePost.as_view(), name="create"),
    path('update/<int:pk>/', views.update, name="update"),
]