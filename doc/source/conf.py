"""testci documentation configuration."""
from datetime import (
    datetime,
)

import testci

project = "testci"
author = "Josh Mayer"
copyright = f"{datetime.now().year}, {author}"

version = testci.__version__
release = testci.__version__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]

templates_path = ["_templates"]

source_suffix = ".rst"

master_doc = "index"

language = None

exclude_patterns = ["conf.py"]

pygments_style = None

html_theme = "sphinx_rtd_theme"

html_static_path = ["_static"]

htmlhelp_basename = f"{project}doc"

latex_elements = {}

latex_documents = [
    (master_doc, f"{project}.tex", f"{project} Documentation", author, "manual"),
]

man_pages = [(master_doc, project, f"{project} Documentation", [author], 1)]

texinfo_documents = [
    (
        master_doc,
        project,
        f"{project} Documentation",
        author,
        project,
        "{project} - testcio",
        "Miscellaneous",
    ),
]

intersphinx_mapping = {
}

todo_include_todos = True
