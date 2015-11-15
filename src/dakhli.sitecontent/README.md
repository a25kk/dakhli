# dakhli.sitecontent

## Sitecontent package containing folderish content pages

* `Source code @ GitHub <https://github.com/potzenheimer/dakhli.sitecontent>`_
* `Releases @ PyPI <http://pypi.python.org/pypi/dakhli.sitecontent>`_
* `Documentation @ ReadTheDocs <http://dakhlisitecontent.readthedocs.org>`_
* `Continuous Integration @ Travis-CI <http://travis-ci.org/potzenheimer/dakhli.sitecontent>`_

## How it works

This package provides a Plone addon as an installable Python egg package.

The generated Python package hold the necessary scaffold to add content types
via the 'contenttype' template and to add functionality.

In order to get productive you still need to generate a contenttype

```bash
$ cd dakhli.sitecontent/src/dakhli/sitecontent/
$ mrbob --config ~/.mrbob.ini -O example_type bobtemplates:contenttype

```


## Installation

To install `dakhli.sitecontent` you simply add ``dakhli.sitecontent``
to the list of eggs in your buildout, run buildout and restart Plone.
Then, install `dakhli.sitecontent` using the Add-ons control panel.
