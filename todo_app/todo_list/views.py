from django.shortcuts import render
from .models import List
from .forms import ItemList
# Create your views here.


def index(request):
    all_items = List.objects.all()
    
    context = {'items': all_items}
    
    return render(request, 'todo_list/index.html', context)


def about(request):
    return render(request, 'todo_list/about.html')