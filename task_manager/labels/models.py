from django.db import models
from django.utils.translation import gettext as _


class Label(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
        verbose_name=_('Name'),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Creation date'),
    )

    def __str__(self):
        return self.name
