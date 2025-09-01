from __future__ import annotations

import numpy as np


def mascara_agua(indice: np.ndarray, threshold: float = 0.2) -> np.ndarray:
    """Gera máscara booleana (True=água) a partir de um índice (ex.: NDWI)."""
    raise NotImplementedError("Implementar máscara d'água por limiar")
