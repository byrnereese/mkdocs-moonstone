from setuptools import setup, find_packages

VERSION = '0.1.0'

setup(
    name="mkdocs-ringcentral",
    version=VERSION,
    url='https://git.ringcentral.com/byrnereese/mkdocs-ringcentral/',
    description='RingCentral theme for MkDocs',
    author='Byrne Reese',
    author_email='byrne.reese@ringcentral.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'mkdocs>=1.0',
        'mkdocs-git-committers-plugin>=0.1.3',
        'mkdocs-bootstrap4>=0.1.2',
        'mkdocs-bootstrap-tables-plugin>=0.1.0',
        'mkdocs-material>=3.0'
    ],
    python_requires='>=2.7.9,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    entry_points={
        'mkdocs.themes': [
            'ringcentral = mkdocs_ringcentral',
        ]
    },
    zip_safe=False
)
