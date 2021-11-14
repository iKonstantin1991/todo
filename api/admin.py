from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'do_until', 'status',
                    'responsible', 'author')
    fields = ['name', 'description', 'do_until', 'status',
              ('responsible', 'author')]
