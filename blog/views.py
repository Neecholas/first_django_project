from django.shortcuts import render
from django.http import HttpResponse

# the function takes a request and
def home(request):
  context = {
    'Poo': 'Hey there'
    }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html', {'title' : 'About'})
