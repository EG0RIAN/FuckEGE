from django.contrib import admin

from .models import Task, Message


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_num', 'answer')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('time_and_date', 'text')
