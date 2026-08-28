import time


def consultar_almoxarifado(codigo_produto: str) -> int:
    """Consulta a quantidade de itens no almoxarifado a partir de um código."""

    if not codigo_produto or len(codigo_produto) != 5:
        return -3

    if not codigo_produto.startswith("P"):
        return -3

    # Simula o tempo de consulta em um banco de dados legado
    time.sleep(0.06)

    if codigo_produto == "P0001":
        return 17

    if codigo_produto == "P0002":
        return 0

    if codigo_produto == "P9999":
        return 7

    return -3
