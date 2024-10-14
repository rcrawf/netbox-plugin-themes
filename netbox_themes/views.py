from netbox.views import generic
from . import forms, models, tables

class ThemeView(generic.ObjectView):
    queryset = models.Theme.objects.all()

class ThemeListView(generic.ObjectListView):
    queryset = models.Theme.objects.all()
    table = tables.ThemeTable

class ThemeEditView(generic.ObjectEditView):
    queryset = models.Theme.objects.all()
    form = forms.ThemeForm

class ThemeDeleteView(generic.ObjectDeleteView):
    queryset = models.Theme.objects.all()
