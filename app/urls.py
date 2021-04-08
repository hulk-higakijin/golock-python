from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('index/', views.index, name='index'),
    path('index/new', views.NewPost.as_view(), name="new_post"),
]