import random

print("""
    __        ___.                     .___       
_/  |______ \_ |__  __ _______     __| _/____   
\   __\__  \ | __ \|  |  \__  \   / __ |\__  \  
 |  |  / __ \| \_\ \  |  // __ \_/ /_/ | / __ \_
 |__| (____  /___  /____/(____  /\____ |(____  /
           \/    \/           \/      \/     \/ 
                                    
    """)

numero_aleatorio1 = random.randrange(1,21)
numero_aleatorio2 = random.randrange(1,21)
equaç= numero_aleatorio1 * numero_aleatorio2
print(f"O numero 1 é {numero_aleatorio1}")
print(f"O numero 2 é {numero_aleatorio2}")
resul=int(input("Multiplique os dois números, e escreva o resultado aqui: "))
if resul == equaç:
    print("Está correto!")
else:
    print("Está errado, tente novamente!")
    print(f"O resultado correto é {equaç}!")