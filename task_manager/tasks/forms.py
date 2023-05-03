from django import forms
from task_manager.tasks.models import Task


class TaskForm(forms.ModelForm):
    model = Task
    fields = ('name', 'description', 'status', 'assignee')
