from j02_adivinhe_numero.adivinha_numero import jogar_adivinha_numero
from j01_mad_libs.historia_maluca import jogar_mad_libs
from j03_tabuada.tabuada import jogar_tabuada
from j04_cara_or_coroa.cara_or_coroa import jogar_cara_coroa
from j05_impar_or_par.game_impar_or_par import jogar_impar_par
from j06_jogo_das_tres_coisas.jogo_das_tres_coisas import jogar_jogo_tres_coisas
from j02_adivinhe_numero.adivinha import jogar_adivinha_2

while True:

    print("""
        
         ▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄     ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄ 
        █   █       █       █       █   █       █       █       █      █
        █   █   ▄   █   ▄▄▄▄█   ▄   █   █▄     ▄█    ▄▄▄█       █  ▄   █
    ▄   █   █  █ █  █  █  ▄▄█  █ █  █     █   █ █   █▄▄▄█     ▄▄█ █▄█  █
    █ █▄█   █  █▄█  █  █ █  █  █▄█  █    █   █ █    ▄▄▄█    █  █      █
    █       █       █  █▄▄█ █       █    █   █ █   █▄▄▄█    █▄▄█  ▄   █
    █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█    █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄█ █▄▄█
        
       .--..--..--..--..--..--.
      .' \  (`._   (_)     _   \
     .'    |  '._)         (_)  |
     \ _.')\      .----..---.   /
     |(_.'  |    /    .-\-.  \  |
     \     0|    |   ( O| O) | o|
      |  _  |  .--.____.'._.-.  |
       \ (_) | o         -` .-`  |
        |    \   |`-._ _ _ _ _\ /
        \    |   |  `. |_||_|   |
        | o  |    \_      \     |     -.   .-.
        |.-.  \     `--..-'   O |     `.`-' .'
    _.'  .' |     `-.-'      /-.__   ' .-'
    .' `-.` '.|='=.='=.='=.='=|._/_ `-'.'
    `-._  `.  |________/\_____|    `-.'
    .'   ).| '=' '='\/ '=' |
    `._.`  '---------------'
            //___\   //___\
                ||       ||
                ||_.-.   ||_.-.
                (_.--__) (_.--__)
        
    ############################################################
    ##                                                        ##
    ##                  0 - SAIR                              ##
    ##                  1 - Mad Libs                          ##
    ##                  2 - Adivinhe o número                 ##
    ##                  3 - Tabuada                           ##
    ##                  4 - Cara ou Coroa                     ##
    ##                  5 - Impar ou Par                      ##
    ##                  6 - Jogo das três coisas              ##
    ##                  7 - Adivinha 2.0                      ##
    ##                                                        ##
    ############################################################
        """)


    escolha = int(input("Com qual jogo iremos nos divertir?"))
    if escolha == 1:
        jogar_mad_libs()
    elif escolha == 2:
        jogar_adivinha_numero()
    elif escolha == 3:
        jogar_tabuada()
    elif escolha == 4:
        jogar_cara_coroa()
    elif escolha == 5:
        jogar_impar_par()
    elif escolha == 6:
        jogar_jogo_tres_coisas()
    elif escolha == 7:
        jogar_adivinha_2()
    elif escolha == 0:
        print("Foi bom jogar com você!")
        break