from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('index/', views.index, name='index'),
    path('new/', views.NewPost.as_view(), name="new"),
    path('post/<int:pk>', views.PostDetail.as_view(), name='detail'),
    path('post/<int:pk>/delete', views.PostDelete.as_view(), name="delete"),
]