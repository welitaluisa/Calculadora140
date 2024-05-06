def somar_dois_numeros(num1, num2):
    return num1 + num2 

def subtrair_dois_numeros(num1, num2):
    return  num1 - num2

def dividir_dois_numeros(num1, num2):
    try: 
        return num1 / num2
    except(ZeroDivisionError):
        return 'Erro: Não é possivel dividir por zero'

def multiplicar_dois_numeros(num1, num2):
    return num1 * num2