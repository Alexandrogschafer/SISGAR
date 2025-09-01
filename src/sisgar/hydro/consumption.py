def daily_consumption_to_volume(lps: float) -> float:
    """Converte vazão média (L/s) em volume diário (m³)."""
    return lps * 86400.0 / 1000.0
