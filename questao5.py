"""
5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. 
Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. 
Seu objetivo é descobrir qual interruptor controla qual lâmpada. 
Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?  
"""

# Simulação das lâmpadas e interruptores
lampadas = {"A": False, "B": False, "C": False}  # Todas as lâmpadas estão inicialmente desligadas
temperaturas = {"A": "fria", "B": "fria", "C": "fria"}  # Todas as lâmpadas estão inicialmente frias

def ligar_interruptor(interruptor):
    lampadas[interruptor] = True  # Liga a lâmpada
    temperaturas[interruptor] = "quente"  # A lâmpada aquece após algum tempo

def desligar_interruptor(interruptor):
    lampadas[interruptor] = False  # Desliga a lâmpada

# Passo 1: Ligue o interruptor A por alguns minutos
ligar_interruptor("A")

# Simula o tempo passando, aquece a lâmpada
# Aqui já vamos assumir que a lâmpada aquecerá após o tempo
# Não faremos uma pausa no código para não complicar a simulação

# Passo 2: Desligue o interruptor A
desligar_interruptor("A")

# Passo 3: Ligue o interruptor B e vá até a sala das lâmpadas
ligar_interruptor("B")

# Simulação de visitar a sala das lâmpadas
def verificar_lampadas():
    for lampada, acesa in lampadas.items():
        estado = "acesa" if acesa else "apagada"
        temperatura = temperaturas[lampada]
        print(f"Lâmpada {lampada}: {estado}, {temperatura}")

verificar_lampadas()

# Análise do resultado:
# Lâmpada acesa -> Controlada pelo interruptor B
# Lâmpada apagada e quente -> Controlada pelo interruptor A
# Lâmpada apagada e fria -> Controlada pelo interruptor C
