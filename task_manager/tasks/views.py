from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django_filters.views import FilterView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.mixins import DeleteAuthorCheckMixin
from .models import Task
from .forms import TaskForm
from .filters import TaskFilter


class TasksIndexView(LoginRequiredMixin, FilterView):
    model = Task
    template_name = 'tasks/index.html'
    filterset_class = TaskFilter

    context_object_name = 'tasks'
    extra_context = {
        'title': _('Tasks'),
        'button_text': _('Show'),
    }


class TaskDetailView(LoginRequiredMixin, DetailView):
    template_name = 'tasks/show.html'
    model = Task

    context_object_name = 'task'
    extra_context = {
        'title': _('Task details')
    }


class TaskCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = TaskForm

    success_url = reverse_lazy('tasks_index')
    success_message = _('Task created successfully')

    extra_context = {
        'title': _('Create task'),
        'button_text': _('Create'),
    }

    def form_valid(self, form):
        """
        Set current user as the task's author.
        """
        user = self.request.user
        form.instance.author = user
        return super().form_valid(form)


class TaskUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'form.html'
    form_class = TaskForm

    success_url = reverse_lazy('tasks_index')
    success_message = _('Task edited successfully')

    extra_context = {
        'title': _('Editing task'),
        'button_text': _('Submit changes'),
    }


class TaskDeleteView(SuccessMessageMixin, LoginRequiredMixin,
                     DeleteAuthorCheckMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'

    success_url = reverse_lazy('tasks_index')
    success_message = _('Task deleted successfully')

    permission_message = _("Task can be deleted only by its author")
    permission_url = reverse_lazy('tasks_index')

    extra_context = {
        'title': _('Deleting task'),
        'button_text': _('Yes, delete'),
    }
