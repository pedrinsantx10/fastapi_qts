from app.fidelidade.pontos import calcular_pontos_compra


def test_compra_comum_de_cinquenta_reais_gera_cinco_pontos():
    resultado = calcular_pontos_compra(valor_gasto=50.0, categoria="padrao")
    assert resultado == 5


def test_compra_com_valor_zero_ou_negativo_gera_zero_pontos():
    assert calcular_pontos_compra(valor_gasto=0.0, categoria="padrao") == 0
    assert calcular_pontos_compra(valor_gasto=-27.0, categoria="padrao") == 0


def test_cliente_premium_recebe_cinco_pontos_de_bonus_acima_de_vinte_reais():
    resultado = calcular_pontos_compra(valor_gasto=30.0, categoria="premium")
    assert resultado == 8


def test_cliente_premium_com_compra_baixa_nao_recebe_bonus():
    resultado = calcular_pontos_compra(valor_gasto=15.0, categoria="premium")
    assert resultado == 1


def test_cliente_ouro_recebe_dez_pontos_de_bonus():
    resultado = calcular_pontos_compra(valor_gasto=42.0, categoria="ouro")
    assert resultado == 16