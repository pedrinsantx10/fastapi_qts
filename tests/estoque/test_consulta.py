import time

import pytest

from app.estoque.consulta import consultar_almoxarifado


@pytest.mark.parametrize(
    "codigo_produto, estoque_esperado",
    [
        ("", -3),
        ("P", -3),
        ("P123", -3),
        ("1234567", -3),
        ("A123456", -3),
        ("P0001", 17),
        ("P0002", 0),
        ("P9999", 7),
    ],
)
def test_consultar_almoxarifado(codigo_produto, estoque_esperado):
    assert consultar_almoxarifado(codigo_produto) == estoque_esperado


def test_tempo_consulta():
    inicio = time.process_time()

    consultar_almoxarifado("P0001")

    fim = time.process_time()
    tempo_execucao = fim - inicio

    assert tempo_execucao < 0.3
