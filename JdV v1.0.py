import os
import random
player1 = ""
player2 = ""
letraPlayer1 = "O"
letraPlayer2 = "X"
x = ""
turno = 1
submenu = 0
posicao = ['*'] * 9
jogar = True
final = False
next = False
#Opções do MENU
def Menu(mopcoes = 0):
    print("JOGO DA VELHA\n")
    print("1. Jogar")
    print("2. Instruções")
    print("3. Sair")
    print("\n\nVersão 1.0")
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
    final = False
    while menu == 1 and final == False:
        if submenu == 0:
            submenu = SubMenu()

            #Calcular quem vai começar primeiro
            turno = random.randint(1, 2)
            #O primeiro a jogar sempre é representado como O
            if turno == 2:
                letraPlayer2 = "O"
                letraPlayer1 = "X"
            else:
                letraPlayer2 = "X"
                letraPlayer1 = "O"
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
                    if turno == 1:
                        #Definir X
                        while x != "1" and x != "2" and x != "3" and x != "4" and  x != "5" and x != "6" and x != "7" and x != "8" and x != "9":  
                                x = input()
                        x = int(x)
                        #Verificar se a posição escolhida do X ja está ocupada
                        while posicao[x - 1] == "X" or posicao[x - 1] == "O":
                            while x != "1" and x != "2" and x != "3" and x != "4" and  x != "5" and x != "6" and x != "7" and x != "8" and x != "9":  
                                x = input()
                            x = int(x)
                        posicao[x - 1] = letraPlayer1

                    #Se o X ou O ja estiver ganho, será impedido o O jogar
                    if posicao[0] == "X" and posicao[1] == "X" and posicao[2] == "X" or posicao[0] == "X" and posicao[4] == "X" and posicao[8] == "X" or posicao[0] == "X" and posicao[3] == "X" and posicao[6] == "X" or posicao[2] == "X" and posicao[4] == "X" and posicao[6] == "X" or posicao[2] == "X" and posicao[5] == "X" and posicao[8] == "X" or posicao[6] == "X" and posicao[7] == "X" and posicao[8] == "X" or posicao[1] == "X" and posicao[4] == "X" and posicao[7] == "X" or posicao[3] == "X" and posicao[4] == "X" and posicao[5] == "X":
                        True
                    elif posicao[0] == "O" and posicao[1] == "O" and posicao[2] == "O" or posicao[0] == "O" and posicao[4] == "O" and posicao[8] == "O" or posicao[0] == "O" and posicao[3] == "O" and posicao[6] == "O" or posicao[2] == "O" and posicao[4] == "O" and posicao[6] == "O" or posicao[2] == "O" and posicao[5] == "O" and posicao[8] == "O" or posicao[6] == "O" and posicao[7] == "O" and posicao[8] == "O" or posicao[1] == "O" and posicao[4] == "O" and posicao[7] == "O" or posicao[3] == "O" and posicao[4] == "O" and posicao[5] == "O":
                        True
                    #Se estiver empatado, será impedido o O jogar
                    elif posicao[0] != "*" and posicao[1] != "*" and posicao[2] != "*" and posicao[3] != "*" and posicao[4] != "*" and posicao[5] != "*" and posicao[6] != "*" and posicao[7] != "*" and posicao[8] != "*":
                        True
                    #Caso o X não estiver ganho e o jogo não estiver empatado, será a vez do O jogar
                    else:
                        x = random.randint(0, 8)
                        while posicao[x] == "X" or posicao[x] == "O":
                            x = random.randint(0, 8)
                        posicao[x] = letraPlayer2
                        if turno != 1:
                            turno = 1

                #Coop
                elif submenu == 2:
                    #Turno 1
                    if turno == 1:
                        #Definir X
                        x = int(input())
                        #Verificar se a posição escolhida do X ja está ocupada
                        while posicao[x - 1] == "X" or posicao[x - 1] == "O":
                            x = int(input())
                        posicao[x - 1] = letraPlayer1
                        #Após a jogada, será ativado o turno 2
                        turno = 2

                    #Turno 2
                    elif turno == 2:
                        #Definir O
                        x = int(input())
                        #Verificar se a posição escolhida do O ja está ocupada
                        while posicao[x - 1] == "X" or posicao[x - 1] == "O":
                            x = int(input())
                        posicao[x - 1] = letraPlayer2
                        #Após a jogada, será ativado o turno 1
                        turno = 1

        #Verificar se X venceu
        if posicao[0] == "X" and posicao[1] == "X" and posicao[2] == "X" or posicao[0] == "X" and posicao[4] == "X" and posicao[8] == "X" or posicao[0] == "X" and posicao[3] == "X" and posicao[6] == "X" or posicao[2] == "X" and posicao[4] == "X" and posicao[6] == "X" or posicao[2] == "X" and posicao[5] == "X" and posicao[8] == "X" or posicao[6] == "X" and posicao[7] == "X" and posicao[8] == "X" or posicao[1] == "X" and posicao[4] == "X" and posicao[7] == "X" or posicao[3] == "X" and posicao[4] == "X" and posicao[5] == "X":
            os.system('cls') or None
            #Mostrar como ficou o jogo após o encerramento da partida
            for i in range(0, 8, 3):
                print(f"{posicao[i]}   ",  end="")
                print(f"{posicao[i+1]}   ",  end="")
                print(posicao[i+2])

            #Single-Player
            if submenu == 1:
                if letraPlayer1 == "X":
                    player1 += "-"
                else:
                    player2 += "-"
                print("\nPlayer 1          BOT")
                print(f" [{player1}]               [{player2}]")
                if player1 == "--":
                    input("Pressione ENTER para voltar ao menu...")
                else:
                    input("Pressione ENTER para iniciar a proxima rodada...")

            #Coop
            elif submenu == 2:
                if letraPlayer1 == "X":
                    player1 += "-"
                else:
                    player2 += "-"
                print("\nPlayer 1          Player 2")
                print(f"  [{player1}]               [{player2}]\n")
                if player1 == "--":
                    input("Pressione ENTER para voltar ao menu...")
                else:
                    input("Pressione ENTER para iniciar a proxima rodada...")

            #Proxima rodada
            next = True
            os.system('cls') or None

        #Verificar se O venceu
        elif posicao[0] == "O" and posicao[1] == "O" and posicao[2] == "O" or posicao[0] == "O" and posicao[4] == "O" and posicao[8] == "O" or posicao[0] == "O" and posicao[3] == "O" and posicao[6] == "O" or posicao[2] == "O" and posicao[4] == "O" and posicao[6] == "O" or posicao[2] == "O" and posicao[5] == "O" and posicao[8] == "O" or posicao[6] == "O" and posicao[7] == "O" and posicao[8] == "O" or posicao[1] == "O" and posicao[4] == "O" and posicao[7] == "O" or posicao[3] == "O" and posicao[4] == "O" and posicao[5] == "O":
            os.system('cls') or None
            #Mostrar como ficou o jogo após o encerramento da partida
            for i in range(0, 8, 3):
                print(f"{posicao[i]}   ",  end="")
                print(f"{posicao[i+1]}   ",  end="")
                print(posicao[i+2])

            #Single-Player 
            if submenu == 1:
                if letraPlayer1 == "O":
                    player1 += "-"
                else:
                    player2 += "-"
                print("\nPlayer 1          BOT")
                print(f" [{player1}]               [{player2}]")
                if player2 == "--":
                    input("Pressione ENTER para voltar ao menu...")
                else:
                    input("Pressione ENTER para iniciar a proxima rodada...")

            #Coop
            elif submenu == 2:
                if letraPlayer1 == "O":
                    player1 += "-"
                else:
                    player2 += "-"
                print("Player 1          Player 2")
                print(f"  [{player1}]               [{player2}]\n")
                if player2 == "--":
                    input("Pressione ENTER para voltar ao menu...")
                else:
                    input("Pressione ENTER para iniciar a proxima rodada...")
        
            #Proxima rodada
            next = True
            os.system('cls') or None
        
        #Empate
        elif posicao[0] != "*" and posicao[1] != "*" and posicao[2] != "*" and posicao[3] != "*" and posicao[4] != "*" and posicao[5] != "*" and posicao[6] != "*" and posicao[7] != "*" and posicao[8] != "*":
            if submenu == 1:
                print("\nEmpate!\n")
                print("Player 1          BOT")
                print(f" [{player1}]               [{player2}]")
                input("Pressione ENTER para iniciar a proxima rodada...") 
               
            if submenu == 2:
                print("\nEmpate!\n")
                print("Player 1          Player 2")
                print(f"  [{player1}]               [{player2}]\n")
                input("Pressione ENTER para iniciar a proxima rodada...")

            #Proxima rodada
            next = True
            os.system('cls') or None

        #Resetar o jogo
        if next == True:
            if player1 == "--" or player2 == "--":
                final = True
                submenu = 0
            posicao = ['*'] * 9
            next = False

    #2. Instruções
    if menu == 2:
        print("- - INSTRUÇÕES - -\n")
        print("A vitória será decidida em uma melhor de 3.")
        print("O primeiro a jogar é escolhido aleatóriamente.")
        print("Escolha um numero que representará a posição da sua jogada. As posições são contadas por fila horizontalmente")
        print("Exemplo:\n")
        print("* * *             1 2 3\n* * *     -->     4 5 6\n* * *             7 8 9\n")
        input("Pressione ENTER para voltar...")
        os.system('cls') or None

    #3. Sair
    if menu == 3:
        print("Obrigado por jogar!")
        #Encerrar o programa
        jogar = False