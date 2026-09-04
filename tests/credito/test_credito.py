import pytest

from app.credito.credito import classificar_credito

@pytest.mark.parametrize(
    "renda_mensal, score_credito, restrito, retorno_esperado",
    {
    # Renda inválida
    (-1000, 500, True, "renda invalida"),
    # Renda Negativa
    (-1000, -1, True, "renda invalida"),
    # Score negativo
    (1000, -10, False, "score invalido"),
    # Score acima do limite
    (1000, 1001, False, "score invalido"),
    # Cliente com restrição
    (1000, 500, True, "reprovado"),
    # Score baixo
    (1000, 300, False, "reprovado"),
    # Score médio
    (1000, 500, False, "aprovado padrao"),
    # Score alto
    (1000, 800, False, "aprovado premium"),
    }
)
def test_classificar_credito_caixa_preta(
    renda_mensal, score_credito, restrito, retorno_esperado
):
    assert classificar_credito(renda_mensal, score_credito, restrito) == retorno_esperado