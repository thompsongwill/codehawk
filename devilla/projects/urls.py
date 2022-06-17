import imp
from django.urls import path
from . import views


app_name = 'projects'


urlpatterns = [ 
               path('', views.home, name='home' ),
               path('project/<str:project_id>/', views.singleProject, name='single_project'),
               path('update-project/<str:pk>/', views.updateProject, name='update_project'),
               path('delete-project/<str:pk>/', views.deleteProject, name='delete_project'),
               path('create-project', views.createProject, name='new_project'),
               ]