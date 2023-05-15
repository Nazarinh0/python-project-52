from django.db import models
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from django.utils.translation import gettext as _


class Task(models.Model):
    name = models.CharField(
        _("name"),
        max_length=150,
        unique=True,
    )
    description = models.TextField(
        _('Description'),
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='author',
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name='status',
        verbose_name=_('status')
    )
    assignee = models.ForeignKey(
        User,
        blank=True,
        on_delete=models.PROTECT,
        related_name='assignee',
        verbose_name=_('assignee')
    )
    labels = models.ManyToManyField(
        Label,
        blank=True,
        related_name='labels',
        through='TaskLabel',
        verbose_name=_('labels')
    )

    def __str__(self):
        return self.name


class TaskLabel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.RESTRICT)
