from django.db import models
from django.utils.translation import gettext_lazy as _
from task_manager.users.models import User
from task_manager.statuses.models import Status


class Task(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
    )
    description = models.TextField(
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
    )
    assignee = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='assignee',
    )
    
    def __str__(self):
        return self.name