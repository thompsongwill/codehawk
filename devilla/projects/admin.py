from django.contrib import admin
from .models import Project, Review, Tag

# Register your models here.


admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)

admin.site.site_header = 'Devilla Admin Dashboard'
admin.site.site_title = 'Welcome Devilla Dashboard'
admin.site.index_title = 'Admin Dashboard'
