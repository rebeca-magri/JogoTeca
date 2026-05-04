#Alvin, Simon e Theodore
import random

def jogar_jogo_tres_coisas():

    print("""

    ███████ ███████  ██████  ██████  ██      ██   ██  █████       ██████       █████  ██     ██    ██ ██ ███    ██        ███████ ██ ███    ███  ██████  ███    ██      ██████  ██    ██     ████████ ██   ██ ███████  ██████  ██████   ██████  ██████  ███████ 
    ██      ██      ██      ██    ██ ██      ██   ██ ██   ██     ██    ██     ██   ██ ██     ██    ██ ██ ████   ██        ██      ██ ████  ████ ██    ██ ████   ██     ██    ██ ██    ██        ██    ██   ██ ██      ██    ██ ██   ██ ██    ██ ██   ██ ██      
    █████   ███████ ██      ██    ██ ██      ███████ ███████     ██    ██     ███████ ██     ██    ██ ██ ██ ██  ██        ███████ ██ ██ ████ ██ ██    ██ ██ ██  ██     ██    ██ ██    ██        ██    ███████ █████   ██    ██ ██   ██ ██    ██ ██████  █████   
    ██           ██ ██      ██    ██ ██      ██   ██ ██   ██     ██    ██     ██   ██ ██      ██  ██  ██ ██  ██ ██             ██ ██ ██  ██  ██ ██    ██ ██  ██ ██     ██    ██ ██    ██        ██    ██   ██ ██      ██    ██ ██   ██ ██    ██ ██   ██ ██      
    ███████ ███████  ██████  ██████  ███████ ██   ██ ██   ██      ██████      ██   ██ ███████  ████   ██ ██   ████ ▄█     ███████ ██ ██      ██  ██████  ██   ████      ██████   ██████         ██    ██   ██ ███████  ██████  ██████   ██████  ██   ██ ███████                                                                                                                                                                                                                                                           

    Classificação:
    ALVIN = 1
    SIMON = 2
    THEODORE = 3

    """)

    my_escolha= input("Você escolhe o Alvin, Simon ou Theodore? ").upper()
    numero_aleatorio = random.choice(["ALVIN", "SIMON", "THEODORE"])
    print(f"O computador escolheu {numero_aleatorio}")

    if my_escolha == numero_aleatorio:
        print("Deu empate, tenta de novo")
        exit()
    elif my_escolha == "ALVIN" and numero_aleatorio == "SIMON": #1 e 2
        print("Voce perdeu, o SIMON é maior")
    elif my_escolha == "SIMON"  and numero_aleatorio == "THEODORE": #2 e 3
        print("Voce perdeu, o THEODORE é maior")
    elif my_escolha == "ALVIN" and numero_aleatorio == "THEODORE": #1 E 3
        print ("Voce perdeu, o THEODORE é maior")
    elif my_escolha == "THEODORE" and numero_aleatorio == "ALVIN": #3 E 1
        print ("Voce ganhou, o ALVIN é menor")
    elif my_escolha == "THEODORE" and numero_aleatorio == "SIMON": #3 E 2
        print ("Voce ganhou, o SIMON é menor")
    else:
        print ("Voce ganhou, o ALVIN é menor")

