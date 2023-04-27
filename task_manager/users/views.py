from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.users.forms import UserForm
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserForm
    template_name = 'form.html'
    success_url = reverse_lazy('login')
    success_message = _('User created successfully')
    extra_context = {
        'title': _('Registration'),
        'button_text': _('Register'),
    }
