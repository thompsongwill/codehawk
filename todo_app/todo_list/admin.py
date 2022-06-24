from django.contrib import admin
from .models import List

# Register your models here.


admin.site.register(List)

admin.site.site_header = "To Do List App"
admin.site.site_title = "App Dashboard"
admin.site.index_title = "To-Do List"