import time

import pytest

from app.faturamento.cobranca import processar_cobranca


@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso, retorno_esperado",
    {
        # Entradas inválidas
        (0, "BRONZE", 0, -1.0),
        (-100, "PRATA", 0, -1.0),
        (100, "OURO", -1, -1.0),

        # Planos inválidos
        (100, "", 0, -2.0),

        # Planos válidos sem atraso
        (100, "BRONZE", 0, 100.0),
        (100, "PRATA", 0, 85.0),
        (100, "OURO", 0, 75.0),

        # Normalização
        (100, "bronze", 0, 100.0),
        (100, "  PRATA  ", 0, 85.0),

        # Atraso moderado
        (100, "BRONZE", 1, 108.4),
        (100, "PRATA", 20, 99.8),

        # Atraso severo
        (100, "BRONZE", 21, 146.8),
        (100, "OURO", 21, 117.6),

        # Arredondamento
        (123.45, "PRATA", 7, 115.87),
    }
)
def test_processar_cobranca_caixa_preta(
    valor_base, plano, dias_atraso, retorno_esperado
):
    assert processar_cobranca(
        valor_base, plano, dias_atraso
    ) == retorno_esperado


def test_processar_cobranca_desempenho():
    inicio = time.perf_counter()
    processar_cobranca(100, "OURO", 10)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert tempo_decorrido <= 0.08