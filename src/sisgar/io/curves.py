from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class ElevationVolumeCurve:
    points: List[Tuple[float, float]]  # (cota, volume_m3)
