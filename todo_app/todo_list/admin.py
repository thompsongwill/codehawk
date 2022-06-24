from django.contrib import admin
from .models import List

# Register your models here.


admin.site.register(List)

admin.site.site_header = "To Do List App"
admin.site.site_title = "To-Do List"
admin.site.index_title = "App Dashboard "