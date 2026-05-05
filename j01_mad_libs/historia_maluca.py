def jogar_mad_libs():

  print("""
    ▄█    █▄     ▄█     ▄████████     ███      ▄██████▄     ▄████████  ▄█     ▄████████        ▄▄▄▄███▄▄▄▄      ▄████████  ▄█       ███    █▄   ▄████████    ▄████████ 
    ███    ███   ███    ███    ███ ▀█████████▄ ███    ███   ███    ███ ███    ███    ███      ▄██▀▀▀███▀▀▀██▄   ███    ███ ███       ███    ███ ███    ███   ███    ███ 
    ███    ███   ███▌   ███    █▀     ▀███▀▀██ ███    ███   ███    ███ ███▌   ███    ███      ███   ███   ███   ███    ███ ███       ███    ███ ███    █▀    ███    ███ 
  ▄███▄▄▄▄███▄▄ ███▌   ███            ███   ▀ ███    ███  ▄███▄▄▄▄██▀ ███▌   ███    ███      ███   ███   ███   ███    ███ ███       ███    ███ ███          ███    ███ 
  ▀▀███▀▀▀▀███▀  ███▌ ▀███████████     ███     ███    ███ ▀▀███▀▀▀▀▀   ███▌ ▀███████████      ███   ███   ███ ▀███████████ ███       ███    ███ ███        ▀███████████ 
    ███    ███   ███           ███     ███     ███    ███ ▀███████████ ███    ███    ███      ███   ███   ███   ███    ███ ███       ███    ███ ███    █▄    ███    ███ 
    ███    ███   ███     ▄█    ███     ███     ███    ███   ███    ███ ███    ███    ███      ███   ███   ███   ███    ███ ███▌    ▄ ███    ███ ███    ███   ███    ███ 
    ███    █▀    █▀    ▄████████▀     ▄████▀    ▀██████▀    ███    ███ █▀     ███    █▀        ▀█   ███   █▀    ███    █▀  █████▄▄██ ████████▀  ████████▀    ███    █▀  
                                                            ███    ███                                                     ▀                                            
        """)

  verbo= input("Qual o verbo escolhido?")
  animal= input("Qual o animal escolhido?")
  adj= input("Qual o adjetivo escolhido?")
  obj= input("Qual o objeto escolhido?")
  lugar= input("Qual o lugar escolhido?")
  emoção= input("Qual a emoção escolhida?")
  print(f"""
  Era uma vez um(a) {animal} que gostava de {verbo} um {obj}. 
  Certo dia ele procurou seu/sua {obj} e não encontrou, então ele foi até a sala de estar e telefonou para sua amiga abelha que era muito/a {adj}. 
  Então ela disse a ele/a que, ele/a deveria comprar outro/a {obj}, até por que aquele {obj} já havia se perdido pela cidade, 
  sendo assim sua amiga abelha muito {adj} o/a aconcelhou a buscar em outra cidade, por que assim, as chances dele/a encontrar um {obj} identico ao seu eram grandes.
  Sabendo disso o/a {animal} se mudou para o/a {lugar}, lugar em que existiam muitos {obj} como aquele que o/a {animal} havia perdido.
  Enfim, o/a {animal} e seu/a {obj} sentiram muito/a {emoção}.
  """)

if __name__ == "__main__":
  jogar_mad_libs()