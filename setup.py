from setuptools import setup, find_packages

VERSION = '0.1.17'

setup(
    name="mkdocs-moonstone",
    version=VERSION,
    url='https://github.com/byrnereese/mkdocs-moonstone/',
    description='Moonstone theme for MkDocs',
    author='Byrne Reese',
    author_email='byrne@majordojo.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'mkdocs>=1.0',
        'mkdocs-git-committers-plugin>=0.2.1',
        'mkdocs-bootstrap4>=0.1.5',
        'mkdocs-bootstrap-tables-plugin>=0.1.1',
        'mkdocs-material>=3.0'
    ],
    python_requires='>=2.7.9,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    entry_points={
        'mkdocs.themes': [
            'moonstone = mkdocs_moonstone',
        ]
    },
    zip_safe=False
)
