# Adam S. Forsythe - Website Templates

This directory contains Jinja2 templates for the Adam S. Forsythe website.

## Template Structure

- `base.html` - The base template that all other templates extend
- `index.html` - The homepage
- `work.html` - The selected works gallery
- `about.html` - The about page
- `contact.html` - The contact page
- `beast.html` - The Beast of Goblin Combe promotion page
- `available.html` - The available works gallery
- `artwork.html` - Template for individual artwork pages

## How to Build the Site

The static HTML files are generated using the `build.py` script in the root directory. This script takes the templates from this directory and generates HTML files in the root directory.

To build the site:

```bash
python3 build.py
```

## How to Modify Templates

### Changing Page Content

To change the content of a page, edit the corresponding template file. For example, to change the content of the about page, edit `about.html`.

### Adding New Pages

1. Create a new template file in this directory
2. Either extend the `base.html` template or create a standalone template
3. Add the new page to the `pages` list in `build.py`

### Adding New Artwork

1. Add the artwork details to the `artworks` list in `build.py` for the work gallery
2. Add the artwork details to the `available_artworks` list in `build.py` if it's available for purchase
3. Add the artwork details to the `artwork_details` dictionary in `build.py` for the individual artwork page

## Template Variables

- `active_page` - The currently active page (used for navigation highlighting)
- `artworks` - List of artworks for the work gallery
- `available_artworks` - List of available artworks
- `static(path)` - Function to generate URLs for static assets

## Template Blocks

- `title` - The page title
- `meta` - Additional meta tags
- `extra_styles` - Additional CSS styles
- `header` - The page header
- `content` - The main content of the page
- `footer` - The page footer
- `main_attributes` - Attributes for the main element