# Theme Customization

## Customization

The theme can be customized in the standard mkdocs fashion by overriding templates. Just specify the `custom_dir` parameter under the `theme` as so:

```yml
theme:
  name: moonstone
  custom_dir: 'theme/'
```

You may then place in the `theme/` directory any file you wish to override.

## Theme Options

#### Fixed vs Fluid Layout

By default, Moonstone utilized a fixed-width layout. If you wish to switch to a fluid, full-width layout, just set the `fluid_layout` theme option to "True."

```yaml
theme:
  name: moonstone
  fluid_layout: True
```

#### Next/Previous Links

Some documentation sites are non-linear. If you wish to turn off the "next page" and "previous page" links, set the `suppress_nextprev` theme option to "True."

```yaml
theme:
  name: moonstone
  suppress_nextprev: True
```
