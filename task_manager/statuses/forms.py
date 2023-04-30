from django.utils.translation import gettext_lazy as _
from django import forms
from task_manager.statuses.models import Status


class StatusForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        required=True,
    )

    class Meta:
        model = Status
        fields = ('name',)
