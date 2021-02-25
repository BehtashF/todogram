from django.contrib import admin
from .models import *



@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'title']

@admin.register(Trash)
class TrashAdmin(admin.ModelAdmin):
    list_display = ['user', 'title']