# coding: utf-8

from setuptools import setup, find_packages

PACKAGE_ROOT = 'src'
PACKAGE_NAME = 'po_file_checker'

setup(
    name=PACKAGE_NAME,
    version='0.6',
    description='Check that po-files have no untranslated keys',
    author_email='chapson@yandex-team.ru',
    keywords="po-file, build-tools, sanity check",
    package_dir={'': PACKAGE_ROOT},
    packages=find_packages(PACKAGE_ROOT, exclude=['tests']),
    install_requires=[
        'polib',
        'mock',
        'nose',
    ]
)
