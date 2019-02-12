# Theme Options

## `extra.logo`

Relative path (from `$PROJECT/docs/`) to a logo image, which will appear in the upper left corner above the name of the project.

> If logo is not set, your project name setting (from the MkDocs config) will be used in a text header instead. This preserves a link back to your homepage from inner doc pages.

## `extra.logo_name`

Set to `true` to insert your site's `project` name under the logo image as text. Useful if your logo doesn't include the project name itself. Defaults to `false`.

## `extra.logo_title`

Logo's title attribute. Default: your `site_name`.

## `extra.include_toc`

Boolean, whether to include TOC in sidebar navigation or not. Default: false.

## `extra.extra_nav_links`

A dict of navigation links. Example:

```yaml
extra:
  extra_nav_links:
    Fork me on GitHub: https://github.com/iamale/rock-cli
```

## `extra.show_powered_by`

Show “Powered by” message, mentioning MkDocs and this theme. Default: true.

## `extra.sidebars`

Specify sidebars shown in the left menu. By default, the following ones are
shown, top to bottom:

  - `about`: logo and title (`sidebars/about.html`)
  - `toc`: current page table of contents (`sidebars/toc.html`)
  - `related`: links to the previous and next pages (`sidebars/related.html`)
  - `search`: quick search (`sidebars/search.html`)

To add your own sidebar, put its template in `$THEME_DIR/sidebars` and add its
name to `extra.sidebars`:

```yaml
extra:
  sidebars:
    - about
    - toc
    - my-awesome-sidebar # corresponds to `$THEME_DIR/sidebars/my-awesome-sidebar.html`
    - related
    - search
```

## `extra.homepage_sidebars`

List of sidebar names shown in the left menu *on the homepage only*.
By default, the following sidebars are shown, top to bottom:

  - `about`: logo and title (`sidebars/about.html`)
  - `search`: quick search (`sidebars/search.html`)

As you see, homepage is a little special as it doesn't have `toc` and `related`
sidebars by default. The option `extra.homepage_sidebars` lets you easily
override this behavior:

```yaml
extra:
  homepage_sidebars:
    - about
    - toc
    - related
    - search
```

## Navigation sidebar

The table of contents sidebar includes only the current page's headings. If you
want to have the global navigation in the menu, use an alternative sidebar
called `navigation`:

```yaml
extra:
  sidebars:
    - about
    - navigation
    - related
    - search
```

This is a port of the original Alabaster theme's sidebar of the same name.


### Example

```yaml
site_name: rock-cli
theme: alabaster
copyright: 2016 Alexander Pushkov

markdown_extensions:
  - toc:
      permalink: "¶"

extra:
  logo: logo.png
  logo_title: "Rocketbank logo"
  include_toc: yes
  extra_nav_links:
    Fork me on GitHub: https://github.com/iamale/rock-cli
```
