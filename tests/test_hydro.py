from sisgar.hydro.consumption import daily_consumption_to_volume
from sisgar.hydro.depletion import simulate_depletion

def test_consumption_and_depletion():
    v = daily_consumption_to_volume(1.0)  # 1 L/s -> 86.4 m3/dia
    assert round(v, 1) == 86.4
    series = simulate_depletion(volume_m3=200.0, daily_out_m3=50.0, days=5)
    assert len(series) == 5
    assert series[-1] >= 0.0
