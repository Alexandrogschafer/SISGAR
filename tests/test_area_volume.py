from sisgar.processing.area_cota_volume import area_from_mask, mm_to_m3
import numpy as np

def test_area_and_volume_conversions():
    mask = (np.ones((10, 10))).astype(int)
    area = area_from_mask(mask, pixel_area_m2=1.0)
    assert area == 100.0
    vol = mm_to_m3(area_m2=100.0, depth_mm=10.0)
    assert vol == 1.0  # 100 m² * 0.01 m
