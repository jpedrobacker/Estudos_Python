import Jogo
import random

def carrega_palavra_secreta():
    with open('palavras_forca.txt') as arquivo:
        palavras = [linha.strip() for linha in arquivo]
        
    arquivo.closed
    
    n = random.randrange(0,len(palavras))

    palavra_secreta = palavras[n].upper()
    return palavra_secreta

def iniaciliza_lista(palavra_secreta):
    lista = ["_"]*len(palavra_secreta)
    return lista

def pede_chute():
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
    return chute

def chute_certo(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1

def ganhou(letras_acertadas):
    print(letras_acertadas)
    print("Fim de Jogo, você ganhou!")

def perdeu (letras_acertadas):
    print(letras_acertadas)
    print("Forca, você perdeu!")

def chute_errado(erros, letras_erradas, chute):
    letras_erradas.append(chute) 
    print("Você errou, {} tentativa(s) de 6. Letras erradas:{}".format(erros , letras_erradas))
    return letras_erradas

def reiniciar_parar():
    print("Deseja jogar novamente ou mudar de jogo?")
    jogar_novamente = int(input("(1) Jogar nomavamente (2)Mudar de jogo: "))
            
    if(jogar_novamente == 1):
        jogar()
                
    elif (jogar_novamente == 2):
        Jogo.escolha_jogos()

def jogar():
    
    print("Bem-Vindo ao jogo da Forca")
    
    palavra_secreta = carrega_palavra_secreta()
    
    letras_acertadas = iniaciliza_lista(palavra_secreta)
    
    acertou  = False
    enforcou = False
    erros = 0
    letras_erradas = []

    while (not enforcou and not acertou):
        
        print(letras_acertadas)
        chute = pede_chute()
        
        if (chute in palavra_secreta):
            print("Letras erradas:",letras_erradas)
            
            chute_certo(palavra_secreta,chute,letras_acertadas)
                
        else:
            erros += 1
            chute_errado(erros,letras_erradas, chute)
                
        if (erros == 6):
            perdeu(letras_acertadas)
            break
        
        elif ("_" not in letras_acertadas):
            ganhou(letras_acertadas)
            break

    reiniciar_parar()

if(__name__ == "__main__"):
    jogar()