import numpy as np
import pytest

from sisgar.processing.area_cota_volume import area_e_volume


@pytest.mark.xfail(reason="Área/volume ainda não implementado", raises=NotImplementedError)
def test_area_volume_api():
    mask = np.zeros((5, 5), dtype=bool)
    area, vol = area_e_volume(mask, pixel_area_m2=100.0)
    assert isinstance(area, float) and isinstance(vol, float)
