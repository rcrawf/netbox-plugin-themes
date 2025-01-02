from netbox.plugins import PluginConfig
from pathlib import Path
from django.conf import settings


class NetBoxThemes(PluginConfig):
    name = 'netbox_themes'
    verbose_name = 'NetBox Themes'
    description = 'Manage CSS themes for NetBox'
    version = '0.4.1'
    base_url = 'themes'

    def ready(self):
        plugin_templates_dir = Path(__file__).resolve().parent / 'templates/'
        if str(plugin_templates_dir) not in settings.TEMPLATES[0]['DIRS']:
            settings.TEMPLATES[0]['DIRS'].insert(0, str(plugin_templates_dir))
        super().ready()

config = NetBoxThemes
