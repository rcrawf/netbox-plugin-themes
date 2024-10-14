import django_tables2 as tables

from netbox.tables import NetBoxTable
from .models import Theme

class ThemeTable(NetBoxTable):

    class Meta(NetBoxTable.Meta):
        model = Theme
        fields = ('id', 'name', 'active')
        default_columns = ('id', 'name', 'active')
