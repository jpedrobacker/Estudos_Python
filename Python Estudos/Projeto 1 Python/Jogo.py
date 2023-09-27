import Forca
import Adivinhacao

def escolha_jogos():
    
    print("Escolha seu Jogo!")

    print("(1) Jogo de Adivinhação ou (2) Jogo da Forca")

    jogo = int(input("Selecione seu jogo: "))

    if(jogo == 1):
        print("Você escolheu o jogo de Adivinhação")
        Adivinhacao.jogar()
        
    elif (jogo == 2):
        print("Você escolheu o jogo da Forca")
        Forca.jogar()
        
if(__name__ == "__main__"):
    escolha_jogos()