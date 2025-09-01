import numpy as np

def ndwi(green: np.ndarray, nir: np.ndarray) -> np.ndarray:
    denom = (green + nir)
    with np.errstate(divide='ignore', invalid='ignore'):
        out = (green - nir) / denom
    out[~np.isfinite(out)] = 0.0
    return out
