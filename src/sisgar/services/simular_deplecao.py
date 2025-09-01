"""
Serviço para simulação de depleção do reservatório.
Orquestra chamadas aos módulos de hidro (evaporação, consumo) e integra resultados.
"""

from sisgar.hydro.consumption import calcular_consumo
from sisgar.hydro.depletion import simular_deplecao
from sisgar.hydro.evaporation import calcular_evaporacao


def fluxo_deplecao(volume_inicial, parametros_evap, parametros_consumo, passos=30):
    """
    Fluxo completo:
    1. Calcula evaporação
    2. Calcula consumo
    3. Simula depleção do volume ao longo do tempo
    """
    evap = calcular_evaporacao(volume_inicial, **parametros_evap)
    cons = calcular_consumo(volume_inicial, **parametros_consumo)
    resultados = simular_deplecao(volume_inicial, evap, cons, passos=passos)
    return resultados
