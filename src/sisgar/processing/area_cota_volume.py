from dataclasses import dataclass
import numpy as np

@dataclass
class AreaVolume:
    area_m2: float
    volume_m3: float

def area_from_mask(mask: np.ndarray, pixel_area_m2: float) -> float:
    return float(mask.sum()) * float(pixel_area_m2)

def mm_to_m3(area_m2: float, depth_mm: float) -> float:
    """Converte lâmina d’água (mm) em volume (m³)."""
    return area_m2 * (depth_mm / 1000.0)
