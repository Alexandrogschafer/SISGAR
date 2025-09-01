import numpy as np
import pytest

from sisgar.hydro.depletion import simular_deplecao


@pytest.mark.xfail(reason="Depleção ainda não implementada", raises=NotImplementedError)
def test_deplecao_api():
    v = simular_deplecao(1_000.0, np.zeros(3), np.zeros(3))
    assert v.shape[0] == 3
