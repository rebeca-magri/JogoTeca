import random

print("""
 _______  ______   ___   __   __  ___   __    _  __   __  _______    _______    __    _  __   __  __   __  _______  ______    _______ 
|   _   ||      | |   | |  | |  ||   | |  |  | ||  | |  ||       |  |       |  |  |  | ||  | |  ||  |_|  ||       ||    _ |  |       |
|  |_|  ||  _    ||   | |  |_|  ||   | |   |_| ||  |_|  ||    ___|  |   _   |  |   |_| ||  | |  ||       ||    ___||   | ||  |   _   |
|       || | |   ||   | |       ||   | |       ||       ||   |___   |  | |  |  |       ||  |_|  ||       ||   |___ |   |_||_ |  | |  |
|       || |_|   ||   | |       ||   | |  _    ||       ||    ___|  |  |_|  |  |  _    ||       ||       ||    ___||    __  ||  |_|  |
|   _   ||       ||   |  |     | |   | | | |   ||   _   ||   |___   |       |  | | |   ||       || ||_|| ||   |___ |   |  | ||       |
|__| |__||______| |___|   |___|  |___| |_|  |__||__| |__||_______|  |_______|  |_|  |__||_______||_|   |_||_______||___|  |_||_______|

NÍVEIS:
1 - Noob (de 1 à 10)   
2 - Médio (de 1 à 20)   
3 - Profissional (de 1 à 50)   
4 - SENAI (de 1 à 200)   

""")

Nível=int(input("Escolha um nível, de 1 a 4: "))
    
#Noob
if Nível == 1:
    numero_aleatorio = random.randrange(1,11)
    escolha=int(input("Escolha um número aleatório de 1 a 10: "))
    if numero_aleatorio == escolha:
        print("Parabéns você acertou!")
    else:
        print ("OPS! Não foi dessa vez, tente novamente!")
        print(f"A resposta era {numero_aleatorio}!")


#Médio
elif Nível == 2:
    Mnumero_aleatorio = random.randrange(1,21)
    Mescolha=int(input("Escolha um número aleatório de 1 a 20: "))
    if Mnumero_aleatorio == Mescolha:
        print("Parabéns você acertou!")
    else:
        print ("OPS! Não foi dessa vez, tente novamente!")
        print(f"A resposta era {Mnumero_aleatorio}!")


#Profissional
elif Nível == 3:
    Pnumero_aleatorio = random.randrange(1,51)
    Pescolha=int(input("Escolha um número aleatório de 1 a 50: "))
    if Pnumero_aleatorio == Pescolha:
        print("Parabéns você acertou!")
    else:
        print ("OPS! Não foi dessa vez, tente novamente!")
        print(f"A resposta era {Pnumero_aleatorio}!")


#SENAI
elif Nível == 4:
    Snumero_aleatorio = random.randrange(1,201)
    Sescolha=int(input("Escolha um número aleatório de 1 a 200: "))
    if Snumero_aleatorio == Sescolha:
        print("Parabéns você acertou!")
    else:
        print ("OPS! Não foi dessa vez, tente novamente!")
        print(f"A resposta era {Snumero_aleatorio}!")
else:
    print("Esse nível não existe")