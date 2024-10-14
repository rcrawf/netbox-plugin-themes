from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel
from django.urls import reverse

class Theme(NetBoxModel):
    name = models.CharField(
        max_length=100
    )
    active = models.BooleanField(
            default=False
    )
    css_data = models.TextField(
        #max_length=100_000,
        default=''
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_themes:theme', args=[self.id])
