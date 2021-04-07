from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
  data = Post.objects.all()
  params = {
    'data': data
  }
  return render(request, 'app/index.html', params)

# class CreateView(View):
#   def get 

# class ReadView(View):

# class UpdateView(View):

# class DeleteView(View):