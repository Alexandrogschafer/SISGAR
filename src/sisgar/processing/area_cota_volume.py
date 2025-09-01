from __future__ import annotations

from typing import Tuple

import numpy as np


def area_e_volume(mask_agua: np.ndarray, pixel_area_m2: float) -> Tuple[float, float]:
    """Retorna (area_m2, volume_m3) a partir da máscara de água.
    Por ora, considere volume como placeholder (p.ex. area * fator).
    """
    raise NotImplementedError("Implementar cálculo de área (e volume provisório)")
