from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'form.html'
    next_page = reverse_lazy('index')
    success_message = _('You are logged in')
    extra_context = {
        'title': _('Authorisation'),
        'button_text': _('Login'),
    }


class UserLogoutView(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy('index')
    success_message = _('You are logged out')
