from __future__ import annotations

import numpy as np


def simular_deplecao(
    volume_inicial_m3: float, evaporacao_m3_dia: np.ndarray, consumo_m3_dia: np.ndarray
) -> np.ndarray:
    """Série de volumes diários."""
    raise NotImplementedError("Implementar depleção V[t+1]=V[t]-evap-consumo (>=0)")
