from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
# Create your views here.


def home(request):
    projects = Project.objects.all()
    context = {'project':projects}
    return render(request,'projects/index.html', context)

def singleProject(request,project_id):
    project = Project.objects.get(id=project_id)
    # tags = project.tags.all()
    context = {'project':project, }
    return render(request,'projects/project.html', context)

def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects:home')
        
    context = {"form":form}
    return render(request,'projects/project_form.html', context)
    
    
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects:home')
        
    context = {"form":form}
    return render(request,'projects/project_form.html', context)
    
    
def deleteProject(request,pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects:home')
    context = {'delete':project}
    return render(request, 'projects/delete.html', context)
    