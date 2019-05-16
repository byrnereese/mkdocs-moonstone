# Page-level Customization

Mkdocs allows for individual pages to be controlled by page-level template variables. These exist as name/value pairs at the top of the markdown file. 

## Custom Meta Description Tags

If you wish to specify a custom `<meta name="description">` tag, you can use the following page variable at the top of your markdown page:

```yml
meta_description: This is my custom meta description
```

## Breadcrumb Trails

If you wish to turn off the breadcrumb trail at the top of the page, set the page variable `no_breadcrumb` to "True."

```yml
no_breadcrumb:True

# Page Title

Some page content goes here

## Sub-Topic

Etc. 
```

