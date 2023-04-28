from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.users.forms import UserForm, UserUpdateForm
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from task_manager.users.mixins import UserCheckMixin


User = get_user_model()


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserForm
    template_name = 'form.html'

    success_url = reverse_lazy('login')
    success_message = _('User created successfully')

    extra_context = {
        'title': _('Registration'),
        'button_text': _('Register'),
    }


class UserIndexView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'


class UserUpdateView(UserCheckMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'form.html'

    permission_message = _("You can't update other users")
    no_login_message = _('You are not logged in! Please log in')
    permission_url = reverse_lazy("user_index")

    success_message = _('User is successfully edited')
    success_url = reverse_lazy('user_index')

    extra_context = {
        'title': _('Editing user'),
        'button_text': _('Submit changes'),
    }


class UserDeleteView(SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'

    permission_message = _("You can't delete other users")
    no_login_message = _('You are not logged in! Please log in')
    permission_url = reverse_lazy("user_index")
    protected_message = _("User can't be deleted because he have assigned tasks")
    protected_url = reverse_lazy('users')

    success_url = reverse_lazy('user_index')
    success_message = _('User is successfully deleted')

    extra_context = {
        'title': _('Deleting user'),
        'button_text': _('Yes, delete'),
    }
