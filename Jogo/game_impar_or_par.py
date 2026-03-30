import random

("""

      ██╗ ██████╗  ██████╗  ██████╗     ██████╗  ██████╗     ██╗███╗   ███╗██████╗  █████╗ ██████╗      ██████╗ ██╗   ██╗    ██████╗  █████╗ ██████╗ 
     ██║██╔═══██╗██╔════╝ ██╔═══██╗    ██╔══██╗██╔═══██╗    ██║████╗ ████║██╔══██╗██╔══██╗██╔══██╗    ██╔═══██╗██║   ██║    ██╔══██╗██╔══██╗██╔══██╗
     ██║██║   ██║██║  ███╗██║   ██║    ██║  ██║██║   ██║    ██║██╔████╔██║██████╔╝███████║██████╔╝    ██║   ██║██║   ██║    ██████╔╝███████║██████╔╝
██   ██║██║   ██║██║   ██║██║   ██║    ██║  ██║██║   ██║    ██║██║╚██╔╝██║██╔═══╝ ██╔══██║██╔══██╗    ██║   ██║██║   ██║    ██╔═══╝ ██╔══██║██╔══██╗
╚█████╔╝╚██████╔╝╚██████╔╝╚██████╔╝    ██████╔╝╚██████╔╝    ██║██║ ╚═╝ ██║██║     ██║  ██║██║  ██║    ╚██████╔╝╚██████╔╝    ██║     ██║  ██║██║  ██║
 ╚════╝  ╚═════╝  ╚═════╝  ╚═════╝     ╚═════╝  ╚═════╝     ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝  ╚═════╝     ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝
                                                                                                                                                    
 """)

numero_aleatorio = random.randrange(0,11)

par_ou_impar= input("Voce escolhe par ou ímpar? ").upper()
numero_escol=int(input("Escolha um número de 0 a 10: "))
if numero_escol > 10:
    print (f"Você não tem {numero_escol} dedos. Começe novamente!")
    exit()

comp=print(f"O número do computador é {numero_aleatorio}")

conta = (numero_escol+numero_aleatorio)%2

if conta == 0 and par_ou_impar == "PAR":
    print("Parabéns você venceu. O resultado da conta é um número par!")

elif conta == 0 and par_ou_impar == "ÍMPAR":
    print("OPS, não foi dessa vez, tente novamente!")

elif conta != 0 and par_ou_impar == "ÍMPAR":
    print("Parabéns você venceu. O resultado da conta é um número ímpar!")

else:
    print("OPS, não foi dessa vez, tente novamente!")