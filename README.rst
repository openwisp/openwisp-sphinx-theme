openwisp-sphinx-theme
=====================

A `Sphinx theme`_ for OpenWISP docs, based on the `Read The Docs`_
default theme (sphinx_rtd_theme_).

**Live demo:** https://openwisp-sphinx-theme.readthedocs.io/en/latest/

.. figure:: https://user-images.githubusercontent.com/56113566/221259494-d7f5ecb9-8ed2-4187-a3dc-8ae51ed1d324.png
  :align: center

Installation
------------

This theme is distributed on PyPI as openwisp-sphinx-theme_ and can be
installed with ``pip``:

.. code:: console

    $ python3 -m pip install openwisp-sphinx-theme

To use the theme in your Sphinx project, you will need to
add the following to your ``conf.py`` file:

.. code:: python

    # add this extension
    extensions = [...,
    'openwisp.sphinx.theme',
    ...
    ]
    html_theme = "openwisp-sphinx-theme"

Development
-----------

.. code:: bash

    python3 -m pip install -e .
    make clean # Not always needed, but better to be cautious
    make html
    open build/html/index.html

Need help?
----------

- If any help regarding installing and using `sphinx` and
  `reStructured Text` is required then please visit this
  `link <http://www.sphinx-doc.org/en/stable/tutorial.html>`_.

- Feel free to post any doubt or comment through our `support channels
  <http://openwisp.org/support.html>`_.

.. _Sphinx theme: https://www.sphinx-doc.org/en/master/development/theming.html
.. _Read The Docs: https://readthedocs.org
.. _sphinx_rtd_theme: https://github.com/readthedocs/sphinx_rtd_theme
.. _openwisp-sphinx-theme: https://pypi.org/project/openwisp-sphinx-theme/
.. _configuration options: https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html
