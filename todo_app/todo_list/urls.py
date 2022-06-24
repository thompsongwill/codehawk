import imp
from django.urls import path
from . import views



urlpatterns = [ 
               
               path('',views.index, name="home"),
               path('about/',views.about, name="about"),
               path('delete/<list_id>', views.delete, name="delete"),
               path('completed/<complete_id>', views.completed, name="completed"),
               path('uncross/<complete_id>', views.uncross, name="uncross"),
               path('edit/<item_id>', views.edit, name="edit"),
               
               ]