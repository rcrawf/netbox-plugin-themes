from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel
from django.urls import reverse

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
