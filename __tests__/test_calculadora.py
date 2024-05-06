# 1 - bibliotecas, framworks e referencias externas
import pytest

from calculadora.calculadora import somar_dois_numeros, subtrair_dois_numeros, dividir_dois_numeros, multiplicar_dois_numeros

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
