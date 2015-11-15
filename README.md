# dakhli

## Landratsamt Aichach Portal

* `Source code @ GitHub <https://github.com/a25kk/dakhli>`_
* `Releases @ PyPI <http://pypi.python.org/pypi/dakhli>`_
* `Documentation @ ReadTheDocs <http://dakhli.readthedocs.org>`_
* `Continuous Integration @ Travis-CI <http://travis-ci.org/kreativkombinat/dakhli>`_


## Installation

This buildout is intended to be used via the development profile to provide
a ready to work on setup. The relevant steps to get started with a new
development environment would be:

``` bash
$ virtualenv-2.7 dakhli
$ cd ./dakhli
$ git clone git@github.com:username/dakhli.git buildout.dakhli
$ cd ./buildout.dakhli
$ python bootstrap.py -c development.cfg
$ bin/buildout -Nc development.cfg
```
