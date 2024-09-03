"""
1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores "
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
"""

def is_fibonacci(num):
    # Inicializa os dois primeiros números da sequência de Fibonacci
    fib1, fib2 = 0, 1
    
    # Caso o número seja 0 ou 1, ele pertence à sequência
    if num == fib1 or num == fib2:
        return True
    
    # Gera a sequência de Fibonacci até o número ser maior ou igual ao informado
    while fib2 < num:
        fib1, fib2 = fib2, fib1 + fib2
    
    # Verifica se o número informado é igual ao último número gerado da sequência
    return num == fib2

# Solicita ao usuário que informe um número
numero = int(input("Informe um número para verificar se ele pertence à sequência de Fibonacci: "))

# Verifica se o número pertence à sequência de Fibonacci
if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
