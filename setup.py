from pathlib import Path

from setuptools import setup

repo = Path(__file__).resolve().parent
version_path = repo / 'lib/openwisp/sphinx/theme/VERSION'
readme_path = repo / 'README.rst'

with version_path.open(encoding='utf-8') as version_file:
    __version__ = version_file.readline().strip()

setup(
    name='openwisp-sphinx-theme',
    version=__version__,
    license='GPL3',
    author='Aryaman',
    author_email='support@openwisp.io',
    description='OpenWISP documentation sphinx theme',
    long_description=readme_path.read_text(encoding='utf-8'),
    packages=['openwisp.sphinx.theme'],
    package_dir={'': 'lib'},
    # Includes files listed in MANIFEST.in as package data files, see
    # <https://packaging.python.org/guides/using-manifest-in/>.
    include_package_data=True,
    # See <http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package>
    entry_points={
        'sphinx.html_themes': [
            'openwisp-sphinx-theme = openwisp.sphinx.theme',
        ]
    },
    install_requires=[
        'sphinx_rtd_theme >=1.0.0',
        'sphinx-copybutton',
    ],
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
