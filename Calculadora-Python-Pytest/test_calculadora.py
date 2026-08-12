import pytest
from calculadora import Calculadora


@pytest.fixture
def calc():
    return Calculadora()


# TESTES DE SOMA

def test_soma_positivos(calc):
    assert calc.soma(5, 3) == 8


def test_soma_negativos(calc):
    assert calc.soma(-5, -3) == -8


def test_soma_com_zero(calc):
    assert calc.soma(5, 0) == 5


# TESTES DE SUBTRAÇÃO

def test_subtracao_positivos(calc):
    assert calc.subtracao(10, 4) == 6


def test_subtracao_negativos(calc):
    assert calc.subtracao(-5, -3) == -2


def test_subtracao_com_zero(calc):
    assert calc.subtracao(5, 0) == 5


# TESTES DE MULTIPLICAÇÃO

def test_multiplicacao_positivos(calc):
    assert calc.multiplicacao(4, 3) == 12


def test_multiplicacao_negativos(calc):
    assert calc.multiplicacao(-4, 3) == -12


def test_multiplicacao_com_zero(calc):
    assert calc.multiplicacao(5, 0) == 0


# TESTES DE DIVISÃO

def test_divisao_positivos(calc):
    assert calc.divisao(10, 2) == 5


def test_divisao_negativos(calc):
    assert calc.divisao(-10, 2) == -5


def test_divisao_resultado_decimal(calc):
    assert calc.divisao(7, 2) == 3.5


def test_divisao_por_zero(calc):
    with pytest.raises(ValueError, match="Não é possível dividir por zero!"):
        calc.divisao(10, 0)