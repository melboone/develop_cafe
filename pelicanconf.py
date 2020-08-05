#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Default author not set. Each .md article should have an author name and (optional) link.
# Example: Author: <a href="your_link">Author Name</a>

# Should a default author be added, remove the comment below
# AUTHOR = "Julian"

SITENAME = "Develop Cafe"
SITEURL = "http://127.0.0.1:8000"
PATH = "content"
TIMEZONE = "UTC"
DEFAULT_LANG = "en"

# Menu sorting and listing. Categories are hidden by default so we can add them properly below
DISPLAY_CATEGORIES_ON_MENU = False
# Due to the static nature of this job, unfortunately this is a manual job
# Every link needs to the entry added below. Format: Black
MENUITEMS = [
    # ("Home", "/"),
    (
        "Archives",
        [
            ("zip", "/archives/zip.html"),
            ("7z", "/archives/7z.html"),
            ("yaml", "/archives/yaml.html"),
        ],
    ),
]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# RSS Feeds
FEED_ALL_RSS = "feeds/all.rss.xml"
CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"

# Set the Github url
GITHUB_URL = "https://github.com/melboone"

# Default pagination. Should this be necessary, add a number, example "DEFAULT_PAGINATION = 5"
DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "theme/"

# Custom Variables
META_KEYWORDS = ""

# global metadata to all the contents
DEFAULT_METADATA = {"yeah": "it is"}

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
# Pages in the menu can be hidden with the setting "Status: hidden" or "Status: draft" at the begining of the page
DISPLAY_PAGES_ON_MENU = True
