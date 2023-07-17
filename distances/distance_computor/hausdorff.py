"""Distance Hausdorff"""

import numpy as np
from scipy.spatial.distance import directed_hausdorff


def hausdorff(coords_a: np.array, coords_b: np.array) -> float:
    """Compute Hausdorff distance"""

    res_1 = directed_hausdorff(coords_a, coords_b)[0]
    res_2 = directed_hausdorff(coords_b, coords_a)[0]
    return max(res_1, res_2)
