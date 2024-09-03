"""
4) Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, ___
b) 2, 4, 8, 16, 32, 64, ____
c) 0, 1, 4, 9, 16, 25, 36, ____
d) 4, 16, 36, 64, ____
e) 1, 1, 2, 3, 5, 8, ____
f) 2,10, 12, 16, 17, 18, 19, ____
"""

# a) 1, 3, 5, 7, ___
def next_element_a():
    sequence = [1, 3, 5, 7]
    next_element = sequence[-1] + 2
    return next_element

# b) 2, 4, 8, 16, 32, 64, ____
def next_element_b():
    sequence = [2, 4, 8, 16, 32, 64]
    next_element = sequence[-1] * 2
    return next_element

# c) 0, 1, 4, 9, 16, 25, 36, ____
def next_element_c():
    sequence = [0, 1, 4, 9, 16, 25, 36]
    next_element = (len(sequence)) ** 2
    return next_element

# d) 4, 16, 36, 64, ____
def next_element_d():
    sequence = [4, 16, 36, 64]
    next_par = 2 * (len(sequence) + 1)  # O próximo número par
    next_element = next_par ** 2
    return next_element

# e) 1, 1, 2, 3, 5, 8, ____
def next_element_e():
    sequence = [1, 1, 2, 3, 5, 8]
    next_element = sequence[-1] + sequence[-2]
    return next_element

# f) 2, 10, 12, 16, 17, 18, 19, ____
def next_element_f():
    sequence = [2, 10, 12, 16, 17, 18, 19]
    next_element = sequence[-1] + 1
    return next_element

# Imprimindo os próximos elementos de cada sequência
print(f"a) Próximo elemento: {next_element_a()}")
print(f"b) Próximo elemento: {next_element_b()}")
print(f"c) Próximo elemento: {next_element_c()}")
print(f"d) Próximo elemento: {next_element_d()}")
print(f"e) Próximo elemento: {next_element_e()}")
print(f"f) Próximo elemento: {next_element_f()}")
