#!/usr/bin/env python
import os
from typing import List

from setuptools import setup, find_packages

# Package name used to install via pip (shown in `pip freeze` or `conda list`)
MODULE_NAME = 'girard'

# How this module is imported in Python (name of the folder inside `src`)
MODULE_NAME_IMPORT = 'girard'

# Repository name
REPO_NAME = 'girard'

# File to get direct dependencies from (used by pip)
REQUIREMENTS_FILE = 'requirements.txt'


def get_version() -> str:
    with open(os.path.join('src', MODULE_NAME_IMPORT, 'resources',
                           'VERSION')) as f:
        return f.read().strip()


def requirements_from_pip(filename: str) -> List[str]:
    with open(filename, 'r') as pip:
        return [l.strip() for l in pip if not l.startswith('#') and l.strip()]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

SETUP_ARGS = {
    'name': MODULE_NAME,
    'description': 'Python package for approximating solid angles in high dimensions',
    'long_description': long_description,
    'long_description_content_type': "text/markdown",
    'url': 'https://github.com/gnsantos/{:s}'.format(REPO_NAME),
    'author': 'Gervásio Protásio dos Santos Neto',
    'package_dir': {'': 'src'},
    'packages': find_packages('src'),
    'version': get_version(),
    'install_requires': requirements_from_pip(REQUIREMENTS_FILE),
    'extras_require': {
        'test_deps': requirements_from_pip('requirements_test.txt')},
    'include_package_data': True,
    'zip_safe': False,
    'classifiers': [
        'Programming Language :: Python :: 3.6']
}

if __name__ == '__main__':
    setup(**SETUP_ARGS)
