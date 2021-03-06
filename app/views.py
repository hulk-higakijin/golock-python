from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View,DetailView
from .models import Post
from .forms import PostForm

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def welcome(request):
  return render(request, 'app/welcome.html')

def index(request):
  data = Post.objects.all()
  params = {
    'data': data
  }
  return render(request, 'app/index.html', params)

class FormPost(View):
  def get(self, request, *args, **kwargs):
    form = PostForm(request.POST or None)
    return render(request, 'app/form.html', {'form': form})

  def post(self, request, *args, **kwargs):
    form = PostForm(request.POST or None)

    if form.is_valid():
      post_data = Post()
      post_data.author = request.user
      post_data.year = form.cleaned_data['year']
      post_data.text = form.cleaned_data['text']
      post_data.supplement = form.cleaned_data['supplement']
      post_data.save()
      return redirect('index')

    return render(request, 'app/form.html', {'form': form})

class PostDetail(View):
  def get(self, request, *args, **kwargs):
    post_data = Post.objects.get(id=self.kwargs['pk'])
    return render(request, 'app/detail.html', {
      'post_data': post_data,
    })
  
class PostEdit(View):
  def get(self, request, *args, **kwargs):
    post_data = Post.objects.get(id=self.kwargs['pk'])
    form = PostForm(
      request.POST or None,
      initial = {
        'year': post_data.year,
        'text': post_data.text,
        'supplement': post_data.supplement,
      }
    )
    return render(request, 'app/form.html', {
      'form': form
    })
  def post(self, request, *args, **kwargs):
    form = PostForm(request.POST or None)

    if form.is_valid():
      post_data = Post.objects.get(id=self.kwargs['pk'])
      post_data.author = request.user
      post_data.year = form.cleaned_data['year']
      post_data.text = form.cleaned_data['text']
      post_data.supplement = form.cleaned_data['supplement']
      post_data.save()
      return redirect('detail', self.kwargs['pk'])

    return render(request, 'app/form.html', {'form': form})


class PostDelete(View):
  def get(self, request, *args, **kwargs):
    post_data = Post.objects.get(id=self.kwargs['pk'])
    return render(request, 'app/delete.html', {
      'post_data': post_data
    })
  def post(self, request, *args, **kwargs):
    post_data = Post.objects.get(id=self.kwargs['pk'])
    post_data.delete()
    return redirect('index')
  