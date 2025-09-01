from __future__ import annotations

import numpy as np


def ndwi(green: np.ndarray, nir: np.ndarray) -> np.ndarray:
    """Calcula NDWI a partir das bandas GREEN e NIR.
    Retorna array float32 no mesmo shape.
    """
    raise NotImplementedError("Implementar NDWI (green, nir) -> ndarray")
