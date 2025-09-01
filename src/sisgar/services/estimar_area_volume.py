from __future__ import annotations

import numpy as np

from sisgar.processing.area_cota_volume import area_e_volume
from sisgar.processing.indices import ndwi
from sisgar.processing.watermask import mascara_agua


def fluxo_area_volume(
    green: np.ndarray, nir: np.ndarray, pixel_area_m2: float, limiar_ndwi: float = 0.2
):
    """Orquestra NDWI -> máscara -> área/volume."""
    ndwi_img = ndwi(green, nir)  # NotImplementedError até o bolsista preencher
    mask = mascara_agua(ndwi_img, threshold=limiar_ndwi)
    return area_e_volume(mask, pixel_area_m2)
