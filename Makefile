# convenience makefile to boostrap & run buildout
# use `make options=-v` to run buildout with extra options

python = python2.7
options =

all: docs tests

coverage: htmlcov/index.html

htmlcov/index.html: README.rst src/dakhli/dakhli/*.py bin/coverage
	@bin/coverage run --source=./src/dakhli/dakhli/ --branch bin/test
	@bin/coverage html -i
	@touch $@
	@echo "Coverage report was generated at '$@'."

docs: docs/html/index.html

docs/html/index.html: docs/*.rst src/dakhli/dakhli/*.py src/dakhli/dakhli/browser/*.py src/dakhli/dakhli/tests/*.py bin/sphinx-build
	bin/sphinx-build -W docs docs/html
	@touch $@
	@echo "Documentation was generated at '$@'."

bin/sphinx-build: .installed.cfg
	@touch $@

.installed.cfg: bin/buildout buildout.cfg buildout.d/*.cfg setup.py
	bin/buildout $(options)

bin/buildout: bin/python buildout.cfg bootstrap.py
	bin/python bootstrap.py
	@touch $@

bin/python:
	virtualenv -p $(python) --no-site-packages .
	@touch $@

tests: .installed.cfg
	@bin/test
	@bin/flake8 setup.py
	@bin/flake8 src/dakhli/dakhli
	@for pt in `find src/dakhli/dakhli -name "*.pt"` ; do bin/zptlint $$pt; done
	@for xml in `find src/dakhli/dakhli -name "*.xml"` ; do bin/zptlint $$xml; done
	@for zcml in `find src/dakhli/dakhli -name "*.zcml"` ; do bin/zptlint $$zcml; done

clean:
	@rm -rf .coverage .installed.cfg .mr.developer.cfg bin docs/html htmlcov parts develop-eggs \
		src/dakhli.dakhli.egg-info lib include .Python

.PHONY: all docs tests clean
