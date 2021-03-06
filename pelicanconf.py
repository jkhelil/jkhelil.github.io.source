#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jawed khelil'
SITENAME = 'IotNetworks'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/jkhelil'),
          ('Linkedin', 'https://www.linkedin.com/in/jawed-khelil/'),
	    ('Twitter', 'https://twitter.com/jkhelil'),
          ('Mail','mailto:jkhelil@iotnetworks.io'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra']
TYPOGRIFY = True


OUTPUT_PATH = '../jkhelil.github.io'

THEME = '../themes/pelican-bootstrap3'
#THEME = 'themes/tuxlite_tbs'
#THEME = 'themes/pelican-simplegrey'
#THEME = 'themes/modernscientist'
#THEME = 'themes/nosferalatu'

#BOOTSTRAP_THEME = 'flatly'
#BOOTSTRAP_THEME = 'slate'
#BOOTSTRAP_THEME = 'spacelab'
#BOOTSTRAP_THEME = 'cyborg'
BOOTSTRAP_THEME = 'yeti'

#PYGMENTS_STYLE = 'solarizeddark'
#PYGMENTS_STYLE = 'solarizedlight'
PYGMENTS_STYLE = 'emacs'
#PYGMENTS_STYLE = 'autumn'
#PYGMENTS_STYLE = 'monokai'

# We put our theme customizations into our own custom.css file
# Pelican needs path separators to be OS-specific (e.g. backslash for Windows)
CUSTOM_CSS = 'static/custom.css'

# Tell Pelican what to add to the output dir
STATIC_PATHS = ['images', 'extra\custom.css', 'CNAME']

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra\custom.css': {'path': 'static\custom.css'}
}

DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_PAGES_ON_MENU = True
PLUGIN_PATHS=['../plugins']
PLUGINS = ['render_math']

MENUITEMS = (('About','/pages/about.html'),)