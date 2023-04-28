from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


class UserCheckMixin(LoginRequiredMixin, UserPassesTestMixin):
    no_login_message = None
    permission_message = None
    permission_url = None

    def test_func(self):
        user = self.get_object()
        return user == self.request.user

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, self.permission_message)
        else:
            messages.error(self.request, self.no_login_message)
        return redirect(self.success_url)
