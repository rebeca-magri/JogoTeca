import random

def jogar_adivinha_2():
    contador = 0
    while True:
        print("""
         _______  ______   ___   __   __  ___   __    _  __   __  _______    _______    __    _  __   __  __   __  _______  ______    _______ 
        |   _   ||      | |   | |  | |  ||   | |  |  | ||  | |  ||       |  |       |  |  |  | ||  | |  ||  |_|  ||       ||    _ |  |       |
        |  |_|  ||  _    ||   | |  |_|  ||   | |   |_| ||  |_|  ||    ___|  |   _   |  |   |_| ||  | |  ||       ||    ___||   | ||  |   _   |
        |       || | |   ||   | |       ||   | |       ||       ||   |___   |  | |  |  |       ||  |_|  ||       ||   |___ |   |_||_ |  | |  |
        |       || |_|   ||   | |       ||   | |  _    ||       ||    ___|  |  |_|  |  |  _    ||       ||       ||    ___||    __  ||  |_|  |
        |   _   ||       ||   |  |     | |   | | | |   ||   _   ||   |___   |       |  | | |   ||       || ||_|| ||   |___ |   |  | ||       |
        |__| |__||______| |___|   |___|  |___| |_|  |__||__| |__||_______|  |_______|  |_|  |__||_______||_|   |_||_______||___|  |_||_______|

        Nível 1 - de 0 à 100  
        ATENÇÃO: Você tem 3 vidas! 
        """)

        numero_aleatorio = random.randrange(0,101)
        escolha=int(input("Escolha um número aleatório de 0 a 100: "))

        if numero_aleatorio == escolha:
            print("Parabéns você acertou!") 
            break
        else:
            print ("OPS! Não foi dessa vez, tente novamente!")
            print(f"A resposta era {numero_aleatorio}!")
            if numero_aleatorio > escolha:
                print(f"{numero_aleatorio} é maior que {escolha}")
            else:
                print(f"{numero_aleatorio} é menor que {escolha}")
        contador += 1

        if contador == 3:
            print("Suas vidas acabaram. Foi bom jogar com você!")
            break


if __name__ == "__main__":
    jogar_adivinha_2()