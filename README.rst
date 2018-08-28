========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
        | |landscape| |codeclimate|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-flip-flop-operator/badge/?style=flat
    :target: https://readthedocs.org/projects/python-flip-flop-operator
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/techdragon/python-flip-flop-operator.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/techdragon/python-flip-flop-operator

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/techdragon/python-flip-flop-operator?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/techdragon/python-flip-flop-operator

.. |requires| image:: https://requires.io/github/techdragon/python-flip-flop-operator/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/techdragon/python-flip-flop-operator/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/techdragon/python-flip-flop-operator/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/techdragon/python-flip-flop-operator

.. |landscape| image:: https://landscape.io/github/techdragon/python-flip-flop-operator/master/landscape.svg?style=flat
    :target: https://landscape.io/github/techdragon/python-flip-flop-operator/master
    :alt: Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/techdragon/python-flip-flop-operator/badges/gpa.svg
   :target: https://codeclimate.com/github/techdragon/python-flip-flop-operator
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/flip-flop-operator.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/flip-flop-operator

.. |commits-since| image:: https://img.shields.io/github/commits-since/techdragon/python-flip-flop-operator/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/techdragon/python-flip-flop-operator/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/flip-flop-operator.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/flip-flop-operator

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/flip-flop-operator.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/flip-flop-operator

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/flip-flop-operator.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/flip-flop-operator


.. end-badges

An award winning flip flop operator implementation for python.

* Free software: MIT license

Installation
============

::

    pip install flip-flop-operator

Documentation
=============

https://python-flip-flop-operator.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
