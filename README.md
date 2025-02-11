# NetBox Themes Plugin

Plugin to inject custom CSS themes into NetBox.

Tested on Netbox >= 4.1.0.

> [!WARNING]  
> This is experimental so use at your own risk 🌞

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

This is a basic example to change to a monospace font:

![Create a theme](media/create-theme.png?raw=true "Create a theme")

Or take a look in the `samples` directory:

![Doom](media/doom.png?raw=true "Doom theme")

![Star Trek](media/startrek.png?raw=true "Star Trek theme")

![Pokemon](media/pokemon.png?raw=true "Pokemon theme")

![Greggs](media/greggs.png?raw=true "Greggs theme")

![Excel](media/excel.png?raw=true "Excel theme")

## Build instructions

```
python3 -m pip install --upgrade build
python3 -m build
```
