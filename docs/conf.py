# -*- coding: utf-8 -*-
"""
Fanatical Support for AWS documentation build configuration file.

This file is execfile()d with the current directory set to its
containing dir.

Note that not all possible configuration values are present.

All configuration values have a default; values that are commented out
serve to show the default.
"""
#import sys
import os
import sphinx

try:
    import sphinx_rtd_theme
except ImportError:
    sphinx_rtd_theme = None

try:
    from sphinxcontrib import spelling
except:
    spelling = None

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# ,
# 'chios.bolditalic',
# 'chios.remotecode',
# 'chios.remoteinclude'
extensions = [
    'sphinx.ext.githubpages',
    'sphinx.ext.ifconfig',
    'sphinx.ext.todo'
]

if spelling is not None:
    extensions.append('sphinxcontrib.spelling')


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_context = {
    'css_files': [
        '_static/theme_overrides.css',  # overrides wide tables in RTD theme
        '_static/bespoke.css',  # custom CSS styling
        '_static/bolditalic.css',  # bolditalic styling
    ],
}

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# set ifconfig tags
# if not 'CONTENT_ID_BASE' in os.environ or 'build-' in os.environ['CONTENT_ID_BASE']:
# for Nexus previews, gh-pages, and local builds
#    internal = True
# else:
#    # for Nexus publishing
#    internal = False

# The master toctree document.
master_doc = 'index'

# The builder to use when running via the deconst preparer
# builder = 'deconst-single'
# builder = 'deconst-serial'

# General information about the project.
project = 'Fanatical Support for AWS Product Guide'
copyright = '2019, Rackspace'
author = 'Rackspace'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# version = sphinx.__released__
# The full version, including alpha/beta/rc tags.
# release = version

# Global variables that are replaced by the specified value during the build
# process.

rst_epilog = """
.. |service| replace:: Fanatical Support for AWS
.. |apiservice| replace:: <officialProjectName API>
.. |no changes| replace:: None for this release
.. |contract version| replace:: <version>
.. |product name| replace:: Fanatical Support for AWS
"""

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'samples', 'README.rst']

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# External link library
extlinks = {
    'rax': ('http://www.rackspace.com/%s', ''),
    'rax-cart': ('http://cart.rackspace.com/%s', ''),
    'rax-special': ('http://%s.rackspace.com/', ''),
    'rax-cloud': ('http://www.rackspace.com/cloud/%s', ''),
    'rax-dev': ('https://developer.rackspace.com/%s', ''),
    'rax-devdocs': ('https://developer.rackspace.com/docs/%s', ''),
    'rax-devguide': ('https:/developer.rackspace.com/docs/%s', ''),
    'rax-api':
    ('https:/developer.rackspace.com/docs/%s/api-reference', ''),
    'rax-git': ('https://github.com/rackspace/%s', ''),
    'rax-glossary': ('https://developer.rackspace.com/docs/glossary/%s', ''),
    'mycloud': ('https://login.rackspace.com/%s', ''),
    'how-to': ('https://support.rackspace.com/how-to/%s', ''),
    'os': ('http://www.openstack.org/%s', ''),
    'os-docs': ('http://docs.openstack.org/%s', ''),
    'os-wiki': ('http://wiki.openstack.org/%s', ''),
    'git-repo': ('https://github.com/rackerlabs/'
                 'docs-core-infra-user-guide/%s', ''),
    'rackerlabs': ('https://github.com/rackerlabs/%s', ''),
    'rocket': ('https://objectrocket.com/%s', '')
}

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    #  'typekit_id': 'hiw1hhg'
    #  'analytics_id':
    #  'sticky_navigation': False,
    #  'logo_only':
    #  'collapse_navigation': False,
    #  'display_version': False,
    #  'navigation_depth': 4
    #  'prev_next_buttons_location': 'bottom'
    #  'canonical_url':
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Fanatical Support for AWS Product Guide"

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = '_static/<LOGO>' # It goes a _static dir at the repo root.

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = '_static/<ICON>' # It goes a _static dir at the repo root.

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None


# SCVersioning.
#scv_banner_greatest_tag = True
scv_grm_exclude = ('.gitignore', '.nojekyll', 'README.rst')
scv_show_banner = True
#scv_banner_recent_tag = True
svc_banner_main_ref = 'master'
scv_sort = ('semver', 'time')
scv_root_ref = 'master'
svc_priority = 'branches'
