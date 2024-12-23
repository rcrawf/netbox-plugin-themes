# Generated by Django 5.0.9 on 2024-10-12 15:42

import taggit.managers
import utilities.json
from django.db import migrations, models

from netbox_themes.models import Theme

def insert_initial_data(apps, schema_editor):
    """ Create default theme. """
    default_theme = Theme(name="default", active=True, css_data='e30K')
    default_theme.save()

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('extras', '0121_customfield_related_object_filter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=100)),
                ('css_data', models.TextField(default='')),
                ('base_theme', models.CharField(default='dark', max_length=10)),
                ('active', models.BooleanField(default=False)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.RunPython(
            code=insert_initial_data,
        ),
    ]

