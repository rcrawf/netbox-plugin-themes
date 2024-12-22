# NetBox Themes Plugin

Plugin to inject custom CSS themes into NetBox.

# Installation

Install the plugin:

```
pip install netbox-plugin-themes
```

Add to Netbox configuration:

```
# configuration.py
PLUGINS = [
    'netbox_themes',
]
```

Run the migrations and generate static content:

```
manage.py migrate
manage.py collectstatic
```

Then restart the Netbox service.

# Create a theme!

![Create a theme](media/create-theme.png?raw=true "Create a theme")

## Build instructions

```
python3 -m pip install --upgrade build
python3 -m build
```
