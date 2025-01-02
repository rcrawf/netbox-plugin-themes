import base64

from django import forms

from netbox.forms import NetBoxModelForm
from .exceptions import ThemeEditError
from .models import Theme

class ThemeForm(NetBoxModelForm):

    class Meta:
        model = Theme
        fields = ('name', 'active', 'base_theme', 'css_data')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Check if the theme being edited is the "default" theme
        if self.instance.name == 'default':
            self.fields['css_data'].widget.attrs['readonly'] = True 

        # Decode the base64 css_data
        if self.instance and self.instance.pk:
            try:
                # Decode the Base64 encoded css_data and set the initial value
                decoded_css_data = base64.b64decode(self.instance.css_data.encode()).decode()
                self.initial['css_data'] = decoded_css_data  # Set the decoded value as initial
            except Exception:
                pass  # Handle decoding errors if needed

    def save(self, commit=True):
        # If this theme is being activated, deactivate the others
        if self.cleaned_data.get('active'):
            # Deactivate any currently active theme
            Theme.objects.filter(active=True).update(active=False)

        # If the theme is being deactivated, activate the default
        instance = super().save(commit=False)
        # only if the theme isn't a new resource
        if instance.pk:
            if self.cleaned_data.get('active') == False:
                # and we're switching from True -> False (not editing an inactive theme)
                if self.instance._prechange_snapshot.get("active") == True:
                    Theme.objects.filter(name="default").update(active=True)

        # B64 encode the css_data
        # instance = super().save(commit=False)
        if self.cleaned_data.get('css_data'):
            instance.css_data = base64.b64encode(self.cleaned_data['css_data'].encode()).decode()

        # Prevent no themes being active
        if self.cleaned_data.get("name") == "default":
            pre = Theme.objects.get(pk=self.instance.pk)
            if pre.active == True and self.cleaned_data.get("active") == False:
                raise ThemeEditError("Cannot deactive default theme")

        # Save the current theme (it will be the only active one if checked)
        return super().save(commit)

    def clean_css_data(self):
        """ Crude check to stop scripts being uploaded. """
        data = self.cleaned_data['css_data']
        if "script" in data:
            raise forms.ValidationError("Invalid CSS")
        return data
