import os
import random
player1, player2, jogada, ajuste, letraPlayer1, letraPlayer2 = "", "", "", "  ", "O", "X"
turno, submenu = 1, 0
posicao = ['*'] * 9
jogar, final, next = True, False, False

#Opções do MENU
def Menu(mopcoes = 0):
    print("JOGO DA VELHA v1.0.3\n")
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

def RandomizarPrimeiro(turno=0, letraPlayer1="", letraPlayer2=""):
    #Calcular quem vai começar primeiroz
    turno = random.randint(1, 2)
    #O primeiro a jogar sempre é representado como O
    if turno == 2:
        letraPlayer2 = "O"
        letraPlayer1 = "X"
    else:
        letraPlayer2 = "X"
        letraPlayer1 = "O"
        
    return turno, letraPlayer1, letraPlayer2

def Tela():
    #Mostrar a tela do jogo
    for i in range(0, 8, 3):
        print(f"       {posicao[i]}   ",  end="")
        print(f"{posicao[i+1]}   ",  end="")
        print(posicao[i+2])
     
def JogadaPlayer(jogada = ""):
    #Verificar se a jogada é um número
    while jogada != "1" and jogada != "2" and jogada != "3" and jogada != "4" and jogada != "5" and jogada != "6" and jogada != "7" and jogada != "8" and jogada != "9":  
        #Definir jogada
        jogada = input()
    jogada = int(jogada)
    #Verificar se a posição escolhida da jogada ja está ocupada
    while posicao[jogada - 1] == "X" or posicao[jogada - 1] == "O":
        while jogada != "1" and jogada != "2" and jogada != "3" and jogada != "4" and  jogada != "5" and jogada != "6" and jogada != "7" and jogada != "8" and jogada != "9":  
            jogada = input()
        jogada = int(jogada)
    return jogada

def SinglePlayer(turno, letraPlayer1, letraPlayer2, jogada = ""):
    os.system('cls') or None
    #Mostrar a tela do jogo
    for i in range(0, 8, 3):
        print(f"       {posicao[i]}   ",  end="")
        print(f"{posicao[i+1]}   ",  end="")
        print(posicao[i+2])
    
    #Após mostrar a tela, será definido a jogada do PLAYER e BOT
    if turno == 1:
        jogada = JogadaPlayer()
        posicao[jogada - 1] = letraPlayer1

    #Se o PLAYER ou BOT ja estiver ganho, o BOT não poderá jogar
    if posicao[0] == "X" and posicao[1] == "X" and posicao[2] == "X" or posicao[0] == "X" and posicao[4] == "X" and posicao[8] == "X" or posicao[0] == "X" and posicao[3] == "X" and posicao[6] == "X" or posicao[2] == "X" and posicao[4] == "X" and posicao[6] == "X" or posicao[2] == "X" and posicao[5] == "X" and posicao[8] == "X" or posicao[6] == "X" and posicao[7] == "X" and posicao[8] == "X" or posicao[1] == "X" and posicao[4] == "X" and posicao[7] == "X" or posicao[3] == "X" and posicao[4] == "X" and posicao[5] == "X":
        True
    elif posicao[0] == "O" and posicao[1] == "O" and posicao[2] == "O" or posicao[0] == "O" and posicao[4] == "O" and posicao[8] == "O" or posicao[0] == "O" and posicao[3] == "O" and posicao[6] == "O" or posicao[2] == "O" and posicao[4] == "O" and posicao[6] == "O" or posicao[2] == "O" and posicao[5] == "O" and posicao[8] == "O" or posicao[6] == "O" and posicao[7] == "O" and posicao[8] == "O" or posicao[1] == "O" and posicao[4] == "O" and posicao[7] == "O" or posicao[3] == "O" and posicao[4] == "O" and posicao[5] == "O":
        True
    #Se estiver empatado, o BOT não poderá jogar
    elif posicao[0] != "*" and posicao[1] != "*" and posicao[2] != "*" and posicao[3] != "*" and posicao[4] != "*" and posicao[5] != "*" and posicao[6] != "*" and posicao[7] != "*" and posicao[8] != "*":
        True
    #Caso o PLAYER não estiver ganho e o jogo não estiver empatado, será a vez do BOT jogar
    else:
        jogada = random.randint(0, 8)
        while posicao[jogada] == "X" or posicao[jogada] == "O":
            jogada = random.randint(0, 8)
        posicao[jogada] = letraPlayer2
        if turno != 1:
            turno = 1
    
    return turno
            
def Coop(turno, letraPlayer1, letraPlayer2, jogada = ""):
    if turno == 1:
        print("- - Turno do Player 1 - -\n")
        Tela()
        jogada = JogadaPlayer()
        posicao[jogada - 1] = letraPlayer1
        
        os.system('cls') or None
        #Após a jogada, será ativado o turno 2
        turno = 2

    elif turno == 2:
        print("- - Turno do Player 2 - -\n")
        Tela()
        jogada = JogadaPlayer()
        posicao[jogada - 1] = letraPlayer2
        
        os.system('cls') or None
        #Após a jogada, será ativado o turno 1
        turno = 1
    return turno
                
while jogar == True:
    if final == True:
        final = False
    menu = Menu()
    #1. Jogar
    while menu == 1 and final == False:
        #Opções ao escolher JOGAR do MENU
        if submenu == 0:
            submenu = SubMenu()
            
            #Resetar variaveis na primeira rodada
            turno, letraPlayer1, letraPlayer2 = RandomizarPrimeiro()
            player1, player2 = "", ""
            ajuste = "  "
        
        #Single-Player
        if submenu == 1:
            turno = SinglePlayer(turno, letraPlayer1, letraPlayer2)
        #Coop
        elif submenu == 2:
            turno = Coop(turno, letraPlayer1, letraPlayer2)

        #Verificar se X venceu
        if posicao[0] == "X" and posicao[1] == "X" and posicao[2] == "X" or posicao[0] == "X" and posicao[4] == "X" and posicao[8] == "X" or posicao[0] == "X" and posicao[3] == "X" and posicao[6] == "X" or posicao[2] == "X" and posicao[4] == "X" and posicao[6] == "X" or posicao[2] == "X" and posicao[5] == "X" and posicao[8] == "X" or posicao[6] == "X" and posicao[7] == "X" and posicao[8] == "X" or posicao[1] == "X" and posicao[4] == "X" and posicao[7] == "X" or posicao[3] == "X" and posicao[4] == "X" and posicao[5] == "X":
            os.system('cls') or None
            Tela()
            #Single-Player
            if submenu == 1:
                #Ajuste no texto de pontuação
                if letraPlayer1 == "X":
                    if player1 == "-":
                        ajuste = " "
                    elif player1 == "--":
                        ajuste = ""
                    player1 += "-"
                else:
                    player2 += "-"
                print("\nPlayer 1          BOT")
                print(f"  [{player1}]           {ajuste}[{player2}]\n")
                if player1 == "--":
                    input("Pressione ENTER para voltar ao menu...")
                else:
                    input("Pressione ENTER para iniciar a proxima rodada...")

            #Coop
            elif submenu == 2:
                #Ajuste no texto de pontuação
                if letraPlayer1 == "X":
                    if player1 == "-":
                        ajuste = " "
                    elif player1 == "--":
                        ajuste = ""
                    player1 += "-"
                else:
                    player2 += "-"
                print("\nPlayer 1          Player 2")
                print(f"  [{player1}]             {ajuste}[{player2}]\n")
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
            Tela()
            #Single-Player 
            if submenu == 1:
                #Ajuste no texto de pontuação
                if letraPlayer1 == "O":
                    if player1 == "-":
                        ajuste = " "
                    elif player1 == "--":
                        ajuste = ""
                    player1 += "-"
                else:
                    player2 += "-"
                print("\nPlayer 1          BOT")
                print(f"  [{player1}]           {ajuste}[{player2}]\n")
                if player2 == "--":
                    input("Pressione ENTER para voltar ao menu...")
                else:
                    input("Pressione ENTER para iniciar a proxima rodada...")

            #Coop
            elif submenu == 2:
                #Ajuste no texto de pontuação
                if letraPlayer1 == "O":
                    if player1 == "-":
                        ajuste = " "
                    elif player1 == "--":
                        ajuste = ""
                    player1 += "-"
                else:
                    player2 += "-"
                print("Player 1          Player 2")
                print(f"  [{player1}]             {ajuste}[{player2}]\n")
                if player2 == "--":
                    input("Pressione ENTER para voltar ao menu...")
                else:
                    input("Pressione ENTER para iniciar a proxima rodada...")
        
            #Proxima rodada
            next = True
            os.system('cls') or None
        
        #Empate
        elif posicao[0] != "*" and posicao[1] != "*" and posicao[2] != "*" and posicao[3] != "*" and posicao[4] != "*" and posicao[5] != "*" and posicao[6] != "*" and posicao[7] != "*" and posicao[8] != "*":
            #Single-Player
            if submenu == 1:
                print("\nEmpate!\n")
                print("Player 1          BOT")
                print(f"  [{player1}]           {ajuste}[{player2}]\n")
                input("Pressione ENTER para iniciar a proxima rodada...") 
            
            #Coop   
            if submenu == 2:
                print("\nEmpate!\n")
                print("Player 1          Player 2")
                print(f"  [{player1}]             {ajuste}[{player2}]\n")
                input("Pressione ENTER para iniciar a proxima rodada...")

            #Proxima rodada
            next = True
            os.system('cls') or None

        #Resetar o jogo
        if next == True:
            if player1 == "--" or player2 == "--":
                final = True
                submenu = 0
            turno, letraPlayer1, letraPlayer2 = RandomizarPrimeiro()
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