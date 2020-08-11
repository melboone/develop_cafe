#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Default author not set.
# Each .md article should have an author name and (optional) link.
# Example: Author: <a href="your_link">Author Name</a>
# Should a default author be added, remove the comment below
# AUTHOR = "Julian"

# Website details
SITENAME = "Develop Cafe"
# SITEURL = "https://develop.cafe"
SITEURL = "http://127.0.0.1:8000"
PATH = "content"
TIMEZONE = "UTC"

# Translations
DEFAULT_LANG = "en"
ARTICLE_TRANSLATION_ID = "slug"

# Menu sorting and listing. Categories are hidden by default so we can add them properly below
DISPLAY_CATEGORIES_ON_MENU = False
# Due to the static nature of this job, unfortunately this is a manual job
# Every link needs to the entry added below. Format: Black
MENUITEMS = [
    # ("Home", "/"),
    (
        "Digital Samples",
        [
            ("Archives", "/category/archives.html"),
            # ("Audio", "/category/audio.html"),
            # ("Coding", "/category/zip.html"),
            # ("Databases", "/category/zip.html"),
            # ("Documents", "/category/zip.html"),
            # ("Images", "/category/zip.html"),
            # ("Spreadsheets", "/category/zip.html"),
        ],
    ),
    (
        "Images",
        [
            ("Illustrations", "/category/illustrations.html"),
        ],
    ),
    (
        "Hosting",
        [
            ("Image-CDN", "/category/image-cdn.html"),
        ],
    ),
]

# Feed generation is usually not desired when developing
#  Feeds
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_RSS = None
CATEGORY_FEED_RSS = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

# Set the Github url
GITHUB_URL = "https://github.com/melboone"

# Default pagination. Should this be necessary, add a number,
# example "DEFAULT_PAGINATION = 5"
DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Set the theme folder
THEME = "theme/"
CSS_FILE = "main.css"

# Custom Variables
META_KEYWORDS = ""

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    "pictures",
    "robots.txt",
]
# path-specific metadata
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
}

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {"linenos": "table"}

# Default setting for displaying the pages in the menu
# Pages in the menu can be hidden with the setting "Status: hidden" or "Status: draft"
# at the beginning of the page
DISPLAY_PAGES_ON_MENU = True

READERS = {"html": None}
IGNORE_FILES = [".#*"]
GZIP_CACHE = True

# Let's declare the category and TAGS express output files, for visibility sake
# CATEGORY_URL = 'category/{slug}.html'
# CATEGORY_SAVE_AS = None
TAG_URL = "tag/{slug}.html"
TAG_SAVE_AS = "tag/{slug}.html"
TAGS_SAVE_AS = "tags.html"
# Don't create an all categories file
CATEGORIES_SAVE_AS = ""

# Set the date format
DATE_FORMATS = {
    "en": "%a, %d %b %Y",  # English
    "en_US": "%a, %d %b %Y",  # United States of America
    "jp": "%Y-%m-%d(%a)",  # Japan
}
# #
# # # Extra Plugins
# PLUGIN_PATHS = ["plugins", "/plugins"]
# PLUGINS = ["category_meta"]
