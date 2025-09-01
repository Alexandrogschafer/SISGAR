import numpy as np
import pytest

from sisgar.processing.indices import ndwi


@pytest.mark.xfail(reason="NDWI ainda não implementado", raises=NotImplementedError)
def test_ndwi_shape():
    g = np.ones((10, 10))
    n = np.zeros((10, 10))
    out = ndwi(g, n)
    assert out.shape == g.shape
