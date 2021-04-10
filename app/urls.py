from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('index/', views.index, name='index'),
    path('new/', views.FormPost.as_view(), name="form"),
    path('post/<int:pk>', views.PostDetail.as_view(), name='detail'),
    path('post/<int:pk>/edit', views.PostEdit.as_view(), name='edit'),
    path('post/<int:pk>/delete', views.PostDelete.as_view(), name="delete"),
]