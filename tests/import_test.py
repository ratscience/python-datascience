#!/usr/bin/env python

"""Smoke tests."""

import unittest


class TestSmoke(unittest.TestCase):
    """Some smoke tests."""

    def test_import_all(self):
        """Import all modules."""
        import jupyterlab
        import jupytext
        import lightgbm
        import matplotlib
        import numpy
        import pandas
        import sklearn
        import scipy
        import seaborn
        import statsmodels
        import sympy
        import tabulate
        import tqdm
        import xgboost

        return 0


if __name__ == "__main__":
    unittest.main()
