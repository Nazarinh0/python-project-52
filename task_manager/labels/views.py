from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.labels.models import Label
from task_manager.labels.forms import LabelForm
from task_manager.mixins import DeleteProtectionMixin


class LabelsIndexView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'labels/index.html'

    context_object_name = 'labels'
    extra_context = {'title': _('Labels')}


class LabelCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = LabelForm

    success_url = reverse_lazy('labels_index')
    success_message = _('Label creates successfully')

    extra_context = {
        'title': _('Create label'),
        'button_text': _('Create'),
    }


class LabelUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Label
    template_name = 'form.html'
    form_class = LabelForm

    success_url = reverse_lazy('labels_index')
    success_message = _('Label edited successfully')

    extra_context = {
        'title': _('Editing label'),
        'button_text': _('Submit changes'),
    }


class LabelDeleteView(SuccessMessageMixin, LoginRequiredMixin,
                      DeleteProtectionMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'

    success_url = reverse_lazy('labels_index')
    success_message = _('Label deleted successfully')

    protected_url = reverse_lazy('labels_index')
    protected_message = _("You can't delete this label, because some task is using it")  # noqa

    extra_context = {
        'title': _('Deleting labels'),
        'button_text': _('Yes, delete'),
    }
