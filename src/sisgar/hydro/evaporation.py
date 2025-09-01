def pan_evaporation_to_volume(area_m2: float, pan_mm: float, coeff: float = 0.7) -> float:
    """Converte leitura de tanque (mm) em volume (m³) usando coeficiente."""
    return area_m2 * (pan_mm * coeff) / 1000.0
