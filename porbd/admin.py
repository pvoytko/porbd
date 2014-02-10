from django.contrib import admin
from models import *
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group, User

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'name_short']

admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.unregister(User)
admin.site.register(Project, ProjectAdmin)