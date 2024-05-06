# 1 - bibliotecas, framworks e referencias externas
import pytest

from calculadora.calculadora import somar_dois_numeros, subtrair_dois_numeros, dividir_dois_numeros, multiplicar_dois_numeros
from utils.utils import ler_csv

# 2 - Testes

def test_somar_dois_numeros():
    
    # Padrão / Standard AAA( Se diz Tiple A / 3 A) = Arrange, Act, Assert
    # Prepara / Configura
    # Dados de entradas do Testes

    num1 = 5
    num2 = 7 
    resultado_esperado = 12

    # Act / Executa
    resultado_obtido = somar_dois_numeros(num1, num2)

    # Assert / Valida

    assert resultado_esperado == resultado_obtido

def test_subtrair_dois_numeros():

    num1 = 7
    num2 = 5 
    resultado_esperado = 2

    # Act / Executa
    resultado_obtido = subtrair_dois_numeros(num1, num2)

    # Assert / Valida

    assert resultado_esperado == resultado_obtido

def test_dividir_dois_numeros():

    num1 = 8
    num2 = 4 
    resultado_esperado = 2

    # Act / Executa
    resultado_obtido = dividir_dois_numeros(num1, num2)

    # Assert / Valida

    assert resultado_esperado == resultado_obtido

def test_multiplicar_dois_numeros():

    num1 = 2
    num2 = 4 
    resultado_esperado = 8

    # Act / Executa
    resultado_obtido = multiplicar_dois_numeros(num1, num2)

    # Assert / Valida

    assert resultado_esperado == resultado_obtido

def test_dividir_por_zero():

    num1 = 8
    num2 = 0 
    resultado_esperado = 'Erro: Não é possivel dividir por zero'

    # Act / Executa
    resultado_obtido = dividir_dois_numeros(num1, num2)

    # Assert / Valida

    assert resultado_esperado == resultado_obtido

# Test Baseados em Dados = Data Driven Tests (DDT) --> Massa de Testes
    # Dados em uma lista
    # dados em um arquivo, varios formatos: csv ( texto separado por virgulas), json , xml, dat
@pytest.mark.parametrize('num1, num2, resultado_esperado', 
                            [ # array / matriz
                                (5, 7, 12), # tupla / registro
                                (0, 8, 8),
                                (10, -15, -5),
                                (6, 0.75, 6.75)
                            ]
                        )

def test_somar_dois_numeros_lista(num1, num2, resultado_esperado):

    # Act / Executa
    resultado_obtido = somar_dois_numeros(num1, num2)

    # Assert / Valida

    assert resultado_esperado == resultado_obtido

@pytest.mark.parametrize('num1, num2, resultado_esperado',
                            ler_csv('./fixtures/massa_somar.csv')
                        )

def test_somar_dois_numeros_csv(num1, num2, resultado_esperado):

    # Padrão / Standard AAA (se diz Tiple A / 3A) = Arrange, Act, Assert

    # Arrange / Prepara / Configura
    # Dados entrada e saída fornecidos pela massa de teste em formato de lista

    # Act / Executa
    resultado_obtido = somar_dois_numeros(float(num1), float(num2))

    # Assert / Valida
    assert float(resultado_esperado) == resultado_obtido

