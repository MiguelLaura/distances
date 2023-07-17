"""Minimum distance"""

import numpy as np
from scipy.spatial.distance import cdist


def minimal(coords_a: np.array, coords_b: np.array) -> float:
    """Compute minimum distance"""

    res = cdist(coords_a, coords_b, "euclidean")
    return res.min()
