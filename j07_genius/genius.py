import os
import time
import random

def jogar_genius():

    contador = 0

    dicionario_cores = {"Verde":"20",
                        "Azul":"90",
                        "Amarelo":"60",
                        "Vermelho":"C0",
                        "Lilás":"D0"}
    
    lista_sequencia = []

    def limpar_tela():
        os.system("color 07")
        os.system("cls")

    def mudar_cor(cor):                           # OS PARAMENTROS/VARIAVEIS QUE ESTAO DENTRO DAS FUNÇÕES, SÓ EXISTEM ENQUANTO AS FUNÇÕES ESTÃO SENDO EXECUTADAS
        codigo_cor = dicionario_cores[cor]
        os.system(f"color {codigo_cor}")
        time.sleep(1)

    print("""
                
            ██████╗ ███████╗███╗   ██╗██╗██╗   ██╗███████╗
            ██╔════╝ ██╔════╝████╗  ██║██║██║   ██║██╔════╝
            ██║  ███╗█████╗  ██╔██╗ ██║██║██║   ██║███████╗
            ██║   ██║██╔══╝  ██║╚██╗██║██║██║   ██║╚════██║
            ╚██████╔╝███████╗██║ ╚████║██║╚██████╔╝███████║
            ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚══════╝                               
        
        ###################################################
        #            REPITA AS CORES SEM ERRAR            #
        ###################################################
        """)

    input("Pressione ENTER para continuar...")
    limpar_tela()

    while True:
        lista_cores = ["Verde","Azul","Amarelo","Vermelho","Lilás"]
        cor_aleatoria = random.choice(lista_cores)
        lista_sequencia.append(cor_aleatoria)

        for cor_lista in lista_sequencia:
            mudar_cor(cor_lista)

        limpar_tela()

        print("""
                V - Verde
                A - Azul
                M - Amarelo
                B - Vermelho
                L - Lilás
            """)
        print(f"Fase {contador}")
        resposta = input("Digite a sequencia correta: ").upper()

        dicionario_abreviacoes = {"V":"Verde",
                                "A":"Azul",
                                "M":"Amarelo",
                                "B":"Vermelho",
                                "L":"Lilás"}
        lista_respostas = []

        for letra in resposta:
            cor = dicionario_abreviacoes.get(letra)
            lista_respostas.append(cor)
        
        contador +=1
        
        if lista_sequencia != lista_respostas:
            print("Você NÃO é brabo")
            print("A sequência era:")
            print(*lista_sequencia)
            print(f"Voce perdeu na fase {contador-1}")
            break
        else:
            print("Você é o bixão mesmo né??")
            print("Vamos subir de nível, seu FARMADOR DE AURA??")
            print("Pressione ENTER quando estiver pronto...")
            limpar_tela()

if __name__ == "__main__":
    jogar_genius()