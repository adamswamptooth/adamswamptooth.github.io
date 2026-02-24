# Contemporary Fine Artist Portfolio (Static Site)

This repository contains a minimal, image-led portfolio website designed for a contemporary fine artist. It is built as plain HTML/CSS with a tiny amount of JavaScript for mobile navigation.

## Design Intent

- Calm, serious visual tone
- Artwork-led layouts with minimal interface noise
- No sales or e-commerce patterns
- Generous white space and restrained typography
- Strong readability and accessibility on desktop and mobile

## Tech Stack

- HTML5 (semantic structure)
- CSS3 (single shared stylesheet)
- Minimal vanilla JavaScript (mobile menu toggle)
- Static-file friendly for GitHub Pages

## Folder Structure

```text
.
├── index.html                # Home / Work landing page (single hero artwork)
├── works.html                # Selected Works grid
├── about.html                # Artist statement and bio
├── cv.html                   # CV sections
├── contact.html              # Professional contact page
├── artworks/
│   ├── work-01.html          # Artwork detail page template instance
│   ├── work-02.html
│   ├── work-03.html
│   ├── work-04.html
│   ├── work-05.html
│   └── work-06.html
├── assets/
│   ├── css/
│   │   └── styles.css        # Shared styles and responsive layout
│   ├── js/
│   │   └── main.js           # Mobile menu behavior
│   └── images/
│       ├── placeholder-artwork.svg
│       └── placeholder-portrait.svg
└── CNAME
```

## Navigation

Primary navigation appears across all pages:

- Work
- About
- CV
- Contact

Mobile behavior:

- Burger button at top right
- Full-screen overlay menu
- Large tap targets
- Keyboard `Esc` closes the overlay

## Replacing Image Placeholders

Current image slots use neutral grey SVG placeholders.

- Replace `assets/images/placeholder-artwork.svg` references for landscape/hero artwork locations.
- Replace `assets/images/placeholder-portrait.svg` references for portrait/grid/portrait locations.
- Keep the `alt` text meaningful and specific to each artwork.

## Editing Artwork Entries

### Selected Works grid
Edit cards in `works.html`:

- Link target (`href`) to detail page
- Artwork title and year
- Grid image source and `alt`

### Artwork detail pages
Edit files in `artworks/`:

- Title (`h1`)
- Year
- Medium
- Dimensions (metric only)
- Optional short description paragraph
- Image source and `alt`

## Accessibility Notes

- Clear heading hierarchy (`h1` per page, section headings where needed)
- Semantic landmarks (`header`, `nav`, `main`, `section`, `figure`, `figcaption`)
- Keyboard-accessible menu button and links
- Descriptive alt text placeholders included for replacement

## Deployment (GitHub Pages)

This project is ready to deploy as a static site.

1. Push to a GitHub repository.
2. In repository settings, enable GitHub Pages from the main branch (root).
3. If using a custom domain, keep/update `CNAME`.

