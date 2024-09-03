"""
2) Escreva um programa que verifique, em uma string, a existência da letra 'a', seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
"""

def verificar_letra_a(texto):
    # Converte o texto para minúsculas para simplificar a contagem
    texto_lower = texto.lower()
    
    # Conta quantas vezes a letra 'a' aparece no texto
    contagem = texto_lower.count('a')
    
    # Verifica se a letra 'a' existe no texto e exibe a mensagem correspondente
    if contagem > 0:
        print(f"A letra 'a' aparece {contagem} vezes no texto.")
    else:
        print("A letra 'a' não aparece no texto.")

# Solicita ao usuário que informe uma string
texto = input("Informe um texto para verificar a existência da letra 'a': ")

# Chama a função para verificar a letra 'a'
verificar_letra_a(texto)
