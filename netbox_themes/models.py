from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel
from django.urls import reverse

from .exceptions import ThemeDeleteError

BASE_THEME_CHOICES = [
    ('dark', 'Dark'),
    ('light', 'Light'),
]

class Theme(NetBoxModel):
    name = models.CharField(
        max_length=100
    )
    active = models.BooleanField(
            default=False
    )
    css_data = models.TextField(
        default=''
    )
    base_theme = models.CharField(
        max_length=10,
        choices=BASE_THEME_CHOICES,
        default='dark',
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_themes:theme', args=[self.id])

    def delete(self, *args, **kwargs):
        if self.active == True:
            raise ThemeDeleteError("Cannot delete active theme, deactivate it before deleting")
        if self.name == "default":
            raise ThemeDeleteError("Cannot delete default theme")
        super().delete(*args, **kwargs)
