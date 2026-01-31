# Configuration file for the Sphinx documentation builder.
# See https://www.sphinx-doc.org/en/master/usage/configuration.html

project = "ExtraBar"
copyright = "2026, ExtraBar"
author = "ExtraBar"

# Extensions
extensions = [
    "sphinx_immaterial",
]

# Root document (main page)
root_doc = "index"

# Exclude build artifacts
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Sphinx Immaterial theme
html_theme = "sphinx_immaterial"

# Static files (images, CSS, etc.)
html_static_path = ["_static"]

# Logo (smaller size)
html_logo = "_static/logo.png"

# Theme customization with brand colors (Black #000000, Purple #5B5DE7)
html_theme_options = {
    "site_url": "https://extrabar-documentation.readthedocs.io/",
    "repo_url": "https://github.com/AppitStudio/extrabar-docs",
    "repo_name": "ExtraBar",
    "icon": {
        "repo": "fontawesome/brands/github",
    },
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "deep-purple",
            "accent": "deep-purple",
            "toggle": {
                "icon": "material/brightness-7",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "deep-purple",
            "accent": "deep-purple",
            "toggle": {
                "icon": "material/brightness-4",
                "name": "Switch to light mode",
            },
        },
    ],
    "features": [
        "navigation.tabs",
        "navigation.sections",
        "navigation.top",
        "search.highlight",
        "toc.follow",
    ],
}

# Custom CSS for additional styling
html_css_files = ['custom.css']
