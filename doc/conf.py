import os
import sys
sys.path.append(os.path.abspath("./demo/"))
from openwisp.sphinx.theme import __version__ as theme_version

project = 'OpenWISP Demo Documentation'
version = theme_version
author = 'OpenWISP'
extensions = [
    'sphinx.ext.autodoc',
    'openwisp.sphinx.theme',
]

# OpenWISP demo docs site configuration
from datetime import date
project = 'OpenWISP'
copyright = f'2017-{date.today().year}, OpenWISP'
author = 'OpenWISP Community'
exclude_patterns = []
templates_path = ['templates']
html_theme = 'openwisp-sphinx-theme'
html_logo = 'demo/assets/design/openwisp-logo-black.svg'
html_favicon = 'demo/assets/design/favicon.png'
html_favicon = 'demo/assets/design/favicon.png'
