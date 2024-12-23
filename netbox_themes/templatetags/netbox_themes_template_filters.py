from base64 import b64decode

from django import template
from django.utils.safestring import mark_safe

from ..models import Theme

register = template.Library()

@register.filter(name="base64decode")
def base64decode(value):
    """ Decode base64 content """
    return mark_safe(b64decode(value).decode())

@register.filter(name="return_custom_css")
def return_custom_css(value):
    """ Return a custom theme CSS. """
    theme = Theme.objects.get(active=True)
    return mark_safe(b64decode(theme.css_data).decode())

@register.filter(name="return_base_theme")
def return_base_theme(value):
    """ Return base theme name. """
    theme = Theme.objects.get(active=True)
    return theme.base_theme

@register.filter(name="theme_name")
def theme_name(value):
    """ Theme name """
    theme = Theme.objects.get(active=True)
    return theme.name
