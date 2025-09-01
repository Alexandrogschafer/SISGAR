import numpy as np

def threshold_mask(index: np.ndarray, thr: float = 0.2) -> np.ndarray:
    """Máscara binária simples a partir de um índice (ex.: NDWI)."""
    return (index >= thr).astype(np.uint8)
