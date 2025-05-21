import re
import glob
from jinja2 import Environment, FileSystemLoader

# Set up the Jinja environment
env = Environment(loader=FileSystemLoader("templates"))


# Define a function to handle static asset paths
def static(path):
    return path


# Add the static function to the Jinja environment
env.globals["static"] = static

# Define artwork data for the work page
artworks = [
    {
        "url": "green_grin.html",
        "image": "green_grin.jpeg",
        "alt": "Green grin",
        "width": "350",
    },
    {
        "url": "feral_colbalt_claw.html",
        "image": "feral_colbalt_claw.jpeg",
        "alt": "feral colbalt claw",
        "width": "370",
    },
    {
        "url": "snowbite_sprite.html",
        "image": "snowbite_sprite.jpeg",
        "alt": "snowbite sprite",
        "width": "375",
    },
    {
        "url": "crystalgaze_frostbeast.html",
        "image": "Crystalgaze.jpeg",
        "alt": "Crystalgaze frostbeast",
        "width": "370",
    },
    {
        "url": "jarrod_thornbush.html",
        "image": "jarrod_thornbush.jpeg",
        "alt": "jarrod thornbush",
        "width": "355",
    },
    {
        "url": "kissmark_shadow.html",
        "image": "kissmark_shadow.jpeg",
        "alt": "kissmark shadow",
        "width": "370",
    },
    {
        "url": "icicle-eyed-icerend.html",
        "image": "icicle_eyed_icerend.jpeg",
        "alt": "Icicle eyed icerend",
        "width": "355",
    },
    {"url": "buzzer.html", "image": "buzzer.jpeg", "alt": "Buzzer", "width": "360"},
    {"url": "grimjaw.html", "image": "grimjaw.jpeg", "alt": "Grimjaw", "width": "355"},
    {
        "url": "sunstrider.html",
        "image": "P6120440.jpeg",
        "alt": "Sunstrider",
        "width": "340",
    },
    {
        "url": "glimmer_friend.html",
        "image": "Glimmerfriend.jpeg",
        "alt": "glimmer friend",
        "width": "360",
    },
    {
        "url": "Gilded_gryphon.html",
        "image": "P7080475.jpeg",
        "alt": "Gilded Gryphon",
        "width": "350",
    },
    {
        "url": "obsidian_mawbeast.html",
        "image": "obsidian_mawbeast.jpeg",
        "alt": "obsidian mawbeast",
        "width": "355",
    },
    {
        "url": "emerald_mirthmew.html",
        "image": "Emerald_mirthmew.jpeg",
        "alt": "Emerald mirthmew",
        "width": "360",
    },
    {
        "url": "Sartorus.html",
        "image": "Sartorus.jpeg",
        "alt": "Sartorus Scalesbane The Third",
        "width": "350",
    },
    {
        "url": "slybite_smirkle.html",
        "image": "slybite_smirkle.jpeg",
        "alt": "slybite smirkle",
        "width": "350",
    },
    {
        "url": "chic_smirkotaur.html",
        "image": "chic_smirkotaur.jpeg",
        "alt": "chic smirkotaur",
        "width": "355",
    },
    {
        "url": "ray_cat.html",
        "image": "P2080564.jpeg",
        "alt": "Ray Cat II",
        "width": "360",
    },
    {
        "url": "Bluebeam_Plumage_Licker.html",
        "image": "P2270568.jpeg",
        "alt": "Bluebeam Plumage Licker",
        "width": "355",
    },
    {
        "url": "Lumina_whisp.html",
        "image": "Lumina_whisp.jpeg",
        "alt": "Lumina whisp",
        "width": "360",
    },
    {"image": "SparklePup.jpeg", "alt": "SparklePup", "width": "350"},
    {"image": "feral_snarlfiend.jpeg", "alt": "feral snarlfiend", "width": "355"},
    {
        "image": "Specter_of_Silent_Vale.jpeg",
        "alt": "Specter of Silent Vale",
        "width": "360",
    },
    {"image": "P8010641.jpeg", "alt": "Frostlip Chomper", "width": "350"},
]

# Define data for available artworks
available_artworks = [
    {
        "url": "kissmark_shadow.html",
        "image": "kissmark_shadow.jpeg",
        "alt": "kissmark shadow",
        "width": "370",
    },
    {
        "url": "crystalgaze_frostbeast.html",
        "image": "Crystalgaze.jpeg",
        "alt": "Crystalgaze frostbeast",
        "width": "370",
    },
    {
        "url": "emerald_mirthmew.html",
        "image": "Emerald_mirthmew.jpeg",
        "alt": "Emerald mirthmew",
        "width": "360",
    },
    {
        "image": "Specter_of_Silent_Vale.jpeg",
        "alt": "Specter of Silent Vale",
        "width": "360",
    },
    {
        "url": "chic_smirkotaur.html",
        "image": "chic_smirkotaur.jpeg",
        "alt": "chic smirkotaur",
        "width": "355",
    },
    {"image": "P2270568.jpeg", "alt": "Bluebeam Plumage Licker", "width": "355"},
    {"url": "buzzer.html", "image": "buzzer.jpeg", "alt": "Buzzer", "width": "360"},
    {"url": "grimjaw.html", "image": "grimjaw.jpeg", "alt": "Grimjaw", "width": "355"},
    {
        "url": "sunstrider.html",
        "image": "P6120440.jpeg",
        "alt": "Sunstrider",
        "width": "340",
    },
    {
        "url": "glimmer_friend.html",
        "image": "Glimmerfriend.jpeg",
        "alt": "glimmer friend",
        "width": "360",
    },
    {
        "url": "Sartorus.html",
        "image": "Sartorus.jpeg",
        "alt": "Sartorus Scalesbane The Third",
        "width": "350",
    },
    {"image": "P8010641.jpeg", "alt": "Frostlip Chomper", "width": "350"},
]

# Render the main pages
pages = [
    {"template": "index.html", "output": "index.html", "context": {}},
    {"template": "about.html", "output": "about.html", "context": {}},
    {"template": "work.html", "output": "work.html", "context": {"artworks": artworks}},
    {"template": "contact.html", "output": "contact.html", "context": {}},
    {"template": "beast.html", "output": "beast.html", "context": {}},
    {
        "template": "available.html",
        "output": "available.html",
        "context": {"available_artworks": available_artworks},
    },
]

# Build the main pages
for page in pages:
    template = env.get_template(page["template"])
    output = template.render(**page["context"])

    with open(page["output"], "w") as f:
        f.write(output)

    print(f"Generated {page['output']}")


# Process artwork pages by scanning the images directory
def extract_artwork_details(html_file):
    try:
        with open(html_file, "r") as f:
            content = f.read()

            # Extract title and year
            title_match = re.search(
                r'<title>Adam S Forsythe - "([^"]+)", (\d{4})</title>', content
            )

            # Extract image src
            img_match = re.search(r'<img src="([^"]+)"', content)

            # Extract description/medium/dimensions
            desc_match = re.search(
                r'<p class="center">"[^"]+", \d{4}\. ([^<]+?)\.(?:\s+([^<]+))?</p>',
                content,
            )

            if title_match and img_match:
                title = title_match.group(1)
                year = title_match.group(2)
                image = img_match.group(1)

                # Extract medium and dimensions if available
                medium = (
                    desc_match.group(1).strip() if desc_match else "Acrylic on canvas"
                )
                dimensions = (
                    desc_match.group(2).strip()
                    if desc_match and desc_match.group(2)
                    else ""
                )

                # Extract meta description if available
                meta_match = re.search(
                    r'<meta name="description" content="([^"]+)"', content
                )
                description = meta_match.group(1) if meta_match else title

                return {
                    "title": title,
                    "year": year,
                    "image": image,
                    "medium": medium,
                    "dimensions": dimensions,
                    "description": description,
                }
            else:
                return None
    except Exception as e:
        print(f"Error processing {html_file}: {str(e)}")
        return None


# Process all HTML files in the images directory
artwork_html_files = glob.glob("images/*.html")
for html_file in artwork_html_files:
    try:
        details = extract_artwork_details(html_file)
        if details:
            template = env.get_template("artwork.html")
            output = template.render(**details)

            with open(html_file, "w") as f:
                f.write(output)

            print(f"Generated {html_file}")
    except Exception as e:
        print(f"Error generating {html_file}: {str(e)}")

print("All pages have been generated successfully!")
