"""Testing functions distance"""

import numpy as np

from distances.distance_computor.hausdorff import hausdorff
from distances.distance_computor.minimal import minimal


A_TESTS = np.array([
    ["-0.95", "-1.05"],
    ["-1.35", "-0.56"],
    ["0.75", "1.62"],
    ["-0.93", "0.88"],
    ["-0.44", "0.32"],
    ["-0.02", "1.31"],
    ["1.13", "0.26"],
    ["0.40", "-0.23"],
    ["0.86", "0.65"],
    ["1.70", "0.28"],
    ["0.19", "1.51"],
    ["-1.33", "2.75"],
    ["-1.66", "1.31"],
    ["0.90", "0.55"],
    ["2.46", "1.48"],
    ["0.70", "-0.58"],
    ["-0.54", "0.45"],
    ["0.67", "0.67"],
    ["0.67", "-0.72"],
    ["-0.70", "-0.58"],
    ["0.97", "0.87"],
    ["-0.30", "1.77"],
    ["-0.89", "0.16"],
    ["1.67", "1.09"],
    ["-0.70", "0.37"],
], dtype=float)

B_TESTS = np.array([
    ["0.27", "0.32"],
    ["0.62", "-0.18"],
    ["-0.78", "0.54"],
    ["-0.04", "-0.34"],
    ["-0.14", "0.17"],
    ["-0.11", "-2.03"],
    ["-1.42", "0.19"],
    ["-0.11", "0.31"],
    ["0.83", "0.01"],
    ["-1.53", "1.51"],
    ["-2.06", "1.33"],
    ["0.73", "0.98"],
    ["-0.95", "-1.43"],
    ["-0.17", "-1.02"],
    ["-0.55", "-0.39"],
    ["-0.45", "0.31"],
    ["0.04", "0.47"],
    ["-1.10", "-0.26"],
    ["-2.16", "-1.48"],
    ["-0.76", "-0.44"],
], dtype=float)


def test_distance_hausdorff():
    """Testing distance_hausdorff"""
    assert hausdorff(A_TESTS, B_TESTS) == 1.8008053753806934


def test_distance_min():
    """Testing distance_min"""
    assert minimal(A_TESTS, B_TESTS) == 0.014142135623730963
