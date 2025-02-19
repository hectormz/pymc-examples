import os

# -- Project information -----------------------------------------------------
project = "PyMC"
copyright = "2021, PyMC Community"
author = "PyMC Community"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "myst_nb",
    "ablog",
    "sphinx_design",
    "sphinxext.opengraph",
    "sphinx_copybutton",
    "sphinxcontrib.bibtex",
    "sphinx_codeautolink",
    "notfound.extension",
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "*import_posts*",
    "**/.ipynb_checkpoints/*",
    "extra_installs.md",
    "page_footer.md",
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

# theme options
html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/pymc-devs/pymc-examples",
            "icon": "fab fa-github-square",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/pymc_devs",
            "icon": "fab fa-twitter-square",
        },
        {
            "name": "Discourse",
            "url": "https://discourse.pymc.io",
            "icon": "fab fa-discourse",
        },
    ],
    "search_bar_text": "Search...",
    "navbar_end": ["search-field.html", "navbar-icon-links.html"],
    "external_links": [
        {"name": "Learning", "url": "https://docs.pymc.io/en/stable/learn.html"},
        {"name": "API", "url": "https://docs.pymc.io/en/stable/api.html"},
    ],
    "page_sidebar_items": ["postcard", "page-toc", "edit-this-page"],
    "google_analytics_id": "G-6KPRBTE6WV",
}
version = os.environ.get("READTHEDOCS_VERSION", "")
version = version if "." in version else "main"
doi_code = os.environ.get("DOI_READTHEDOCS", "10.5281/zenodo.5654871")
html_context = {
    "github_url": "https://github.com",
    "github_user": "pymc-devs",
    "github_repo": "pymc-examples",
    "github_version": version,
    "doc_path": "examples/",
    "sandbox_repo": f"pymc-devs/pymc-sandbox/{version}",
    "doi_url": f"https://doi.org/{doi_code}",
    "doi_code": doi_code,
}


html_favicon = "../_static/PyMC.ico"
html_logo = "../_static/PyMC.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["../_static"]
html_css_files = ["custom.css"]
templates_path = ["../_templates"]
html_sidebars = {
    "**": [
        # "sidebar-nav-bs.html",
        "postcard_categories.html",
        "tagcloud.html",
    ],
}

# ablog config
blog_baseurl = "https://docs.pymc.io/projects/examples/en/latest/"
blog_title = "PyMC Examples"
blog_path = "blog"
blog_authors = {
    "contributors": ("PyMC Contributors", "https://docs.pymc.io"),
}
blog_default_author = "contributors"
fontawesome_included = True
# post_redirect_refresh = 1
# post_auto_image = 1
# post_auto_excerpt = 2

# MyST config
myst_enable_extensions = ["colon_fence", "deflist", "dollarmath", "amsmath", "substitution"]
citation_code = f"""
```bibtex
@incollection{{citekey,
  author    = "<notebook authors, see above>"
  title     = "<notebook title>",
  editor    = "PyMC Team",
  booktitle = "PyMC examples",
  doi       = "{doi_code}"
}}
```
"""


myst_substitutions = {
    "pip_dependencies": "{{ extra_dependencies }}",
    "conda_dependencies": "{{ extra_dependencies }}",
    "extra_install_notes": "",
    "citation_code": citation_code,
}
jupyter_execute_notebooks = "off"

# bibtex config
bibtex_bibfiles = ["references.bib"]
bibtex_default_style = "unsrt"
bibtex_reference_style = "author_year"

# OpenGraph config
# use default readthedocs integration aka no config here

codeautolink_autodoc_inject = False
codeautolink_concat_default = True

# intersphinx mappings
intersphinx_mapping = {
    "aesara": ("https://aesara.readthedocs.io/en/latest/", None),
    "arviz": ("https://arviz-devs.github.io/arviz/", None),
    "bambi": ("https://bambinos.github.io/bambi/main", None),
    "einstats": ("https://xarray-einstats.readthedocs.io/en/stable/", None),
    "mpl": ("https://matplotlib.org/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "pymc": ("https://docs.pymc.io/en/latest/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference/", None),
    "xarray": ("http://xarray.pydata.org/en/stable/", None),
}
