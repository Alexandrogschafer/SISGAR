import numpy as np
from sisgar.processing.indices import ndwi

def test_ndwi_basic():
    g = np.array([[0.6, 0.2],[0.4, 0.1]])
    n = np.array([[0.1, 0.2],[0.4, 0.1]])
    res = ndwi(g, n)
    assert res.shape == g.shape
    assert np.isfinite(res).all()
