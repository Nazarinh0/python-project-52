from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusForm
from task_manager.mixins import DeleteProtectionMixin


class StatusesIndexView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/index.html'

    context_object_name = 'statuses'
    extra_context = {'title': _('Statuses')}


class StatusCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = StatusForm

    success_url = reverse_lazy('statuses_index')
    success_message = _('Status created successfully')

    extra_context = {
        'title': _('Create status'),
        'button_text': _('Create'),
    }


class StatusUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Status
    template_name = 'form.html'
    form_class = StatusForm

    success_url = reverse_lazy('statuses_index')
    success_message = _('Status edited successfully')

    extra_context = {
        'title': _('Editing status'),
        'button_text': _('Submit changes'),
    }


class StatusDeleteView(SuccessMessageMixin, LoginRequiredMixin, 
                       DeleteProtectionMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'

    success_url = reverse_lazy('statuses_index')
    success_message = _('Status deleted successfully')

    protected_url = reverse_lazy('statuses_index')
    protected_message = _("You can't delete this status, because some task is using it")

    extra_context = {
        'title': _('Deleting status'),
        'button_text': _('Yes, delete'),
    }
