from django.shortcuts import render, redirect
from .models import List
from .forms import ItemList
from django.contrib import messages


# Create your views here.


def index(request):
    if request.method == 'POST':
        form = ItemList(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ("Item has been added to List"))
            return render(request, 'todo_list/index.html', {"items":all_items})
    else:
        all_items = List.objects.all
        return render(request, 'todo_list/index.html', {"items":all_items})


def about(request):
    return render(request, 'todo_list/about.html')


def delete(request, list_id):
    item = List.objects.get(id=list_id)
    item.delete()
    messages.success(request, ("Item has been deleted"))
    return redirect('home')
    
    
def completed(request, complete_id):
    item = List.objects.get(id=complete_id)
    item.completed = True
    item.save()
    return redirect('home')



def uncross(request, complete_id):
    item = List.objects.get(id=complete_id)
    item.completed = False
    item.save()
    return redirect('home')


def edit(request, item_id):
    
    if request.method == 'POST':
        item = List.objects.get(pk=item_id)
        form = ItemList(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
           
            messages.success(request, ("Item has been edited to Successfully"))
            return redirect('home')
    else:
        item = List.objects.get(pk=item_id)
        return render(request, 'todo_list/edit.html', {"item":item})

    