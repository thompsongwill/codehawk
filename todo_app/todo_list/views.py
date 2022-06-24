from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'todo_list/index.html')


def about(request):
    return render(request, 'todo_list/about.html')