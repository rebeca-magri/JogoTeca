import os
import random

def limpar_tela():
    """Função para limpar tela"""
    os.system("cls")

def escolher_palavra() -> str:
    """Escolhe e retorna uma palavra aleatória"""
    palavras = ["OI", "CASA", "GODOFREDO", "PAPEL", "URACILA", "CARBONO", "MEMÓRIA", "INDECENTE", "DESENVOLVER", "GARFO","CITOSINA","MONTANHOSA","BRAVO"]
    palavra_aleatoria = random.choice(palavras)
    #Retorna a palavra para quem chamou a função
    #Assim que ele "return" a função, ele não pode mais fazer nada, nem printar.
    return palavra_aleatoria

def desenhar_forca(erro:int):
    """Imprime o desenho da forca dependendo da quantidade de erros"""
    limpar_tela()
    if erro == 0:
        print(r"""
                --------
                |      !
                |
                |
                |
                |
              """)
        
    elif erro == 1:
        print(r"""
                --------
                |      !
                |    (.c.)
                |
                |
                |
              """)
        
    elif erro == 2:
        print(r"""
                --------
                |      !
                |    (.c.)
                |      |
                |
                |
              """)
        
    elif erro == 3:
        print(r"""
                --------
                |      !
                |    (.c.)
                |     _|
                |      |
                |
              """)
        
    elif erro == 4:
        print(r"""
                --------
                |      !
                |    (.c.)
                |     _|_
                |      |
                |
              """)
        
    elif erro == 5:
        print(r"""
                --------
                |      !
                |    (.c.)
                |     _|_
                |      |
                |     /
              """)
        
    elif erro == 6:
        print(r"""
                --------
                |      !
                |    (.c.)
                |     _|_
                |      |
                |     / \ 
              """)
        
    elif erro == 7:
        print(r"""
                --------
                |      !
                |    (xcx)
                |     _|_
                |      |
                |     / \ 
              """)

def gerar_tracos(palavra:str) -> list:
    """Gera e retorna uma lista contendo underlines na mesma quantidade que a letra da palavra"""
    qnt_letras=len(palavra)
    tracos = []
    contador = 0
    while contador < qnt_letras:
        tracos.append("_")
        contador += 1
    return tracos

def perguntar_letra():
    """Pergunto uma letra"""
    perguntar_letra = input("Qual a letra? ").upper()
    if perguntar_letra != 1:
        print('Eu disse UMA letra seu noob!')
        input("Qual a letra? ").upper()
    return perguntar_letra

def jogar_forca():
        print("""
        ____                            ___        ___________                          
        |    | ____   ____   ____     __| _/____    \_   _____/__________   ____ _____   
        |    |/  _ \ / ___\ /  _ \   / __ |\__  \    |    __)/  _ \_  __ \_/ ___  __  \  
    /\__|    (  <_> ) /_/  >  <_> ) / /_/ | / __ \_  |     \(  <_> )  | \/\  \___ / __ \_
    \________|\____/\___  / \____/  \____ |(____  /  \___  / \____/|__|    \___  >____  /
                /_____/               \/     \/       \/                    \/     \/ 

            """)
    
if __name__ == "__main__":
    jogar_forca()