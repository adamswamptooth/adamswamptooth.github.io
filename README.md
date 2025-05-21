# adamswamptooth.github.io

The website for Adam S Forsythe

## Website Structure

This website is built using Jinja2 templates that generate static HTML files.

### Directory Structure

- `templates/` - Contains Jinja2 templates
- `images/` - Contains image files and artwork detail pages
- `build.py` - Script to generate static HTML files from templates
- `main.css` - Main stylesheet

## How to Build the Site

### Prerequisites

- Python 3
- Jinja2 library (`pip install jinja2`)

### Building

To generate the static HTML files from the templates:

```bash
python3 build.py
```

This will generate HTML files in the root directory.

## Making Changes

### To change page content:

1. Edit the corresponding template in the `templates/` directory
2. Run `build.py` to regenerate the HTML files

### To add a new artwork:

1. Add the image to the `images/` directory
2. Add the artwork details to `build.py` in the appropriate lists:
   - `artworks` for the work gallery
   - `available_artworks` for the available works gallery
   - `artwork_details` for individual artwork pages
3. Run `build.py` to regenerate the HTML files

See `templates/README.md` for more detailed information about the templating system.