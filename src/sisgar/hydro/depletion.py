def simulate_depletion(volume_m3: float, daily_out_m3: float, daily_in_m3: float = 0.0, days: int = 30):
    """Simulação linear simples de depleção (stub)."""
    series = []
    v = volume_m3
    for d in range(days):
        v = max(0.0, v + daily_in_m3 - daily_out_m3)
        series.append(v)
    return series
