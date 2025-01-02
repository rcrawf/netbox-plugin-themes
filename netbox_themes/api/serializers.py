from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ..models import Theme

class ThemeSerializer(NetBoxModelSerializer):

    class ThemeSerializer(NetBoxModelSerializer):
        url = serializers.HyperlinkedIdentityField(
            view_name='plugins-api:netbox_themes-api:theme-detail'
        )

    class Meta:
        model = Theme
        fields = (
            'id', 'name', 'active', 'base_theme', 'css_data',
        )
