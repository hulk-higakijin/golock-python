from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('index/', views.index, name='index'),
    path('fly/', views.Fly.as_view(), name="fly"),
]