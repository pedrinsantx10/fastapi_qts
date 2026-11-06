VALOR_BASE_PONTO = 10.0
VALOR_MINIMO_BONUS = 20.0

TABELA_BONUS_CATEGORIA = {
    "ouro": 12,
    "premium": 5,
}


def calcular_pontos_compra(valor_gasto: float, categoria: str) -> int:
    if valor_gasto <= 0:
        return 0

    pontos_base = int(valor_gasto // VALOR_BASE_PONTO)
    categoria_normalizada = categoria.strip().lower() if categoria else ""

    bonus = 0

    if categoria_normalizada == "ouro" and valor_gasto >= 40:
        bonus = 12
    elif categoria_normalizada == "premium" and valor_gasto > 20:
        bonus = 5

    return pontos_base + bonus