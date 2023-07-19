import os
import random
player1 = ""
player2 = ""
turno = 1
submenu = 0
x = 0
posicao = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]
jogar = True
final = False
#Opções do MENU
def Menu(mopcoes = 0):
    print("JOGO DA VELHA\n")
    print("1. Jogar")
    print("2. Instruções")
    print("3. Sair")
    mopcoes = int(input())
    os.system('cls') or None
    return mopcoes

#Opções ao escolher JOGAR do MENU
def SubMenu(mopcoes = 0):
    print("1. Single-Player")
    print("2. Coop")
    mopcoes = int(input())
    os.system('cls') or None
    return mopcoes


while jogar == True:
    menu = Menu()
    #1. Jogar
    while menu == 1 and final == False:
        if submenu == 0:
            submenu = SubMenu()
        os.system('cls') or None

        #Mostrar a tela do jogo
        for i in range(0, 8, 3):
            print(f"{posicao[i]}   ",  end="")
            print(f"{posicao[i+1]}   ",  end="")
            print(posicao[i+2])
            
            #Após mostrar a tela, será definido onde o X e O vai ficar
            if i == 6:
                #Single-Player
                if submenu == 1:
                    #Definir X
                    x = int(input())
                    #Verificar se a posição escolhida do X ja está ocupada
                    while posicao[x - 1] == "X" or posicao[x - 1] == "O":
                        x = int(input())
                    posicao[x - 1] = "X"

                    #Se o X ja estiver ganho, será impedido o O jogar
                    if posicao[0] == "X" and posicao[1] == "X" and posicao[2] == "X" or posicao[0] == "X" and posicao[4] == "X" and posicao[8] == "X" or posicao[0] == "X" and posicao[3] == "X" and posicao[6] == "X" or posicao[2] == "X" and posicao[4] == "X" and posicao[6] == "X" or posicao[2] == "X" and posicao[5] == "X" and posicao[8] == "X" or posicao[6] == "X" and posicao[7] == "X" and posicao[8] == "X" or posicao[1] == "X" and posicao[4] == "X" and posicao[7] == "X":
                        True
                    elif posicao[0] == "O" and posicao[1] == "O" and posicao[2] == "O" or posicao[0] == "O" and posicao[4] == "O" and posicao[8] == "O" or posicao[0] == "O" and posicao[3] == "O" and posicao[6] == "O" or posicao[2] == "O" and posicao[4] == "O" and posicao[6] == "O" or posicao[2] == "O" and posicao[5] == "O" and posicao[8] == "O" or posicao[6] == "O" and posicao[7] == "O" and posicao[8] == "O" or posicao[1] == "O" and posicao[4] == "O" and posicao[7] == "O":
                        True
                    #Se estiver empatado, será impedido o O jogar
                    elif posicao[0] != "*" and posicao[1] != "*" and posicao[2] != "*" and posicao[3] != "*" and posicao[4] != "*" and posicao[5] != "*" and posicao[6] != "*" and posicao[7] != "*" and posicao[8] != "*":
                        True
                    #Caso o X não estiver ganho e o jogo não estiver empatado, será a vez do O jogar
                    else:
                        x = random.randint(0, 8)
                        while posicao[x] == "X" or posicao[x] == "O":
                            x = random.randint(0, 8)
                        posicao[x] = "O"

                #Coop
                elif submenu == 2:
                    #Turno 1
                    if turno == 1:
                        #Definir X
                        x = int(input())
                        #Verificar se a posição escolhida do X ja está ocupada
                        while posicao[x - 1] == "X" or posicao[x - 1] == "O":
                            x = int(input())
                        posicao[x - 1] = "X"
                        #Após a jogada, será ativado o turno 2
                        turno = 2

                    #Turno 2
                    elif turno == 2:
                        #Definir O
                        x = int(input())
                        #Verificar se a posição escolhida do O ja está ocupada
                        while posicao[x - 1] == "X" or posicao[x - 1] == "O":
                            x = int(input())
                        posicao[x - 1] = "O"
                        #Após a jogada, será ativado o turno 1
                        turno = 1

        #Verificar se X venceu
        if posicao[0] == "X" and posicao[1] == "X" and posicao[2] == "X" or posicao[0] == "X" and posicao[4] == "X" and posicao[8] == "X" or posicao[0] == "X" and posicao[3] == "X" and posicao[6] == "X" or posicao[2] == "X" and posicao[4] == "X" and posicao[6] == "X" or posicao[2] == "X" and posicao[5] == "X" and posicao[8] == "X" or posicao[6] == "X" and posicao[7] == "X" and posicao[8] == "X" or posicao[1] == "X" and posicao[4] == "X" and posicao[7] == "X":
            os.system('cls') or None
            #Mostrar como ficou o jogo após o encerramento da partida
            for i in range(0, 8, 3):
                print(f"{posicao[i]}   ",  end="")
                print(f"{posicao[i+1]}   ",  end="")
                print(posicao[i+2])

            #Vitória contra BOT
            if submenu == 1:
                player1 += "-"
                print("\nVocê Venceu!!!!!\n")
                print("Player 1          BOT")
                print(f" [{player1}]              [{player2}]")
                input("Pressione ENTER para voltar ao MENU...")

            #Vitória contra PLAYER 2
            elif submenu == 2:
                player1 += "-"
                print("\nPlayer 1 Venceu!\n")
                print("Player 1          Player 2")
                print(f" [{player1}]             [{player2}]")
                input("Pressione ENTER para voltar ao MENU...")

            #Encerrar partida
            final = True
            os.system('cls') or None

        #Verificar se O venceu
        elif posicao[0] == "O" and posicao[1] == "O" and posicao[2] == "O" or posicao[0] == "O" and posicao[4] == "O" and posicao[8] == "O" or posicao[0] == "O" and posicao[3] == "O" and posicao[6] == "O" or posicao[2] == "O" and posicao[4] == "O" and posicao[6] == "O" or posicao[2] == "O" and posicao[5] == "O" and posicao[8] == "O" or posicao[6] == "O" and posicao[7] == "O" and posicao[8] == "O" or posicao[1] == "O" and posicao[4] == "O" and posicao[7] == "O":
            os.system('cls') or None
            #Mostrar como ficou o jogo após o encerramento da partida
            for i in range(0, 8, 3):
                print(f"{posicao[i]}   ",  end="")
                print(f"{posicao[i+1]}   ",  end="")
                print(posicao[i+2])

            #Derrota contra BOT    
            if submenu == 1:
                player2 += "-"
                print("\nVocê Perdeu!\n")
                print("Player 1          BOT")
                print(f" [{player1}]             [{player2}]")
                input("Pressione ENTER para voltar ao MENU...")

            #Vitória contra PLAYER 1
            elif submenu == 2:
                player2 += "-"
                print("\nPlayer 2 Venceu!\n")
                print("Player 1          Player 2")
                print(f" [{player1}]             [{player2}]")
                input("Pressione ENTER para voltar ao MENU...")
        
            #Encerrar partida
            final = True
            os.system('cls') or None
        
        #Empate
        elif posicao[0] != "*" and posicao[1] != "*" and posicao[2] != "*" and posicao[3] != "*" and posicao[4] != "*" and posicao[5] != "*" and posicao[6] != "*" and posicao[7] != "*" and posicao[8] != "*":
            print("\nEmpate!\n")
            print("Player 1          Player 2")
            print(f" [{player1}]             [{player2}]")
            input("Pressione ENTER para voltar ao MENU...")
            os.system('cls') or None

    #Resetar o jogo
    if final == True:
        final = False
        for i in range(0, 9):
            posicao[i] = "*" 

    #2. Instruções
    if menu == 2:
        print("- - INSTRUÇÕES - -\n")
        print("A vitória será decidida em uma melhor de 3.")
        print("Escolha um numero que representará a posição da sua jogada. As posições são contadas por fila horizontalmente")
        print("O primeiro a jogar é escolhido aleatóriamente.\n")
        input("Pressione ENTER para voltar...")
        os.system('cls') or None

    #3. Sair
    if menu == 3:
        print("Obrigado por jogar!")
        #Encerrar o programa
        jogar = False