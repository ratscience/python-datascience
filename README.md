# ratscience: Python Datascience Packages

[![made-with-markdown](https://img.shields.io/badge/Made%20with-Markdown-2d2d2d.svg?style=flat-square)](http://commonmark.org)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-204A6A.svg?style=flat-square)](https://www.python.org/)

---

[![Build Status](https://travis-ci.org/ratscience/python-datascience.svg?branch=master)](https://travis-ci.org/ratscience/python-datascience)

---

This repository contains `requirements.txt` file with a periodically updated list of packages and their versions.
The main task of this repository is to instantly synchronize packages and versions between different projects or team members.

**This file is updated as a [rolling release](https://ru.wikipedia.org/wiki/Rolling_release) ASAP. Please see Usage section for freeze current requirements.**

Provides:

* [jupyterlab](https://github.com/jupyterlab/jupyterlab)
* [jupytext](https://github.com/mwouts/jupytext)
* [lightgbm](https://github.com/microsoft/LightGBM)
* [matplotlib](https://github.com/matplotlib/matplotlib)
* [numpy](https://github.com/numpy/numpy)
* [pandas](https://github.com/pandas-dev/pandas)
* [scikit-learn](https://github.com/scikit-learn/scikit-learn)
* [scipy](https://github.com/scipy/scipy)
* [seaborn](https://github.com/mwaskom/seaborn)
* [statsmodels](https://github.com/statsmodels/statsmodels)
* [sympy](https://github.com/sympy/sympy)
* [tabulate](https://github.com/astanin/python-tabulate)
* [tqdm](https://github.com/tqdm/tqdm)
* [xgboost](https://github.com/dmlc/xgboost)

## Usage

### Install

#### Method 1. Install directly from URL raw file

Run this script:

```bash
pip3 install --user -U -r https://raw.githubusercontent.com/ratscience/python-datascience/master/requirements.txt
```

or if you use [virtualenv](https://github.com/pypa/virtualenv):

```bash
pip3 install -U -r https://raw.githubusercontent.com/ratscience/python-datascience/master/requirements.txt
```

#### Method 2. Clone repo

Clone this repository as `git clone https://github.com/ratscience/python-datascience.git`, then go to the repo directory and run:

```bash
pip3 install --user -U -r requirements.txt
```

or if you use [virtualenv](https://github.com/pypa/virtualenv):

```bash
pip3 install -U -r requirements.txt
```

### Update

For update, simply re-run any of install scripts. If you clone git repo, please run `git pull` first.

## Acknowledgements

This project is actively uses this awesome packages:

* [pur](https://github.com/alanhamlett/pip-update-requirements)
* [pip-check](https://github.com/bartTC/pip-check)
* [pre-commit](https://github.com/pre-commit/pre-commit)

## License

[![License: Unlicense](https://img.shields.io/badge/License-Unlicense-green.svg?style=flat-square)](https://unlicense.org/)

This project is licensed under the terms of the [Unlicense](https://unlicense.org/) (see [LICENSE](<https://github.com/ratscience/python-datascience/blob/master/LICENSE>) file).
