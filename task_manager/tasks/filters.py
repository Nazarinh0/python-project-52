from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter
from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task

User = get_user_model()


class TaskFilter(FilterSet):
    statuses = Status.objects.all()
    status = ModelChoiceFilter(
        queryset=statuses,
        label=_('Status'),
        field_name='status'
    )
    labels = Label.objects.all()
    label = ModelChoiceFilter(
        queryset=labels,
        label=_('Label'),
        field_name='labels'
    )
    executors = User.objects.all()
    executor = ModelChoiceFilter(
        queryset=executors,
        label=_('Executor'),
        field_name='executor'
    )
    owned_tasks = BooleanFilter(
        method='get_task_owner',
        widget=forms.CheckboxInput(),
        label=_('Only my tasks')
    )

    def get_task_owner(self, queryset, name, value):
        if value:
            queryset = queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'label', 'owned_tasks']
