# "artificial intelligence".
# "IA_Player"

"""—→ inteligência artifial para jogar jogo da velha (versão 2.0)."""
def IA_Player_Bot(game=[], simb='x', won=False):
    """
    :param: recebe como parâmetro a situação atual da partida.
    :return: ele retorna uma resposta de jogada segundo o parâmetro.
    """     
    from random import randint

    # print('um momento, IA calculando jogada', end='') 
    # for num in range(3):
        # print('.', end='', flush=True), sleep(0)
    # print()    

    if won is False:
        x_o, simb_en, passs = simb, 'o' if simb == 'x' else 'x', True
        
        # Função de ataque
        Folder_move = open('IA_jogo_da_Velha\Game\Function_game\plays.txt', 'r')
        for line in Folder_move.readlines():
            if line.startswith('_'):
                if x_o in game[int(line[1])-1] and \
                        x_o in game[int(line[5])-1] and '' in game[int(line[9])-1]:
                    game[int(line[9])-1][0], passs = x_o, False
                    break
        Folder_move.close()

        # Função de defesa
        if passs is True:
            Folder_move = open('IA_jogo_da_Velha\Game\Function_game\plays.txt', 'r')
            for line in Folder_move.readlines():
                if line.startswith('_'):
                    if simb_en in game[int(line[1])-1] and \
                            simb_en in game[int(line[5])-1] and '' in game[int(line[9])-1]:
                        game[int(line[9])-1][0], passs = x_o, False
                        break
            Folder_move.close()

        # Função de jogada aleatória
        if passs is True:
            while True:
                move = randint(0, 8)
                if simb_en not in game[move][0] and x_o not in game[move][0]:
                    game[move][0] = x_o
                    break
    
        # print('belo jogo, parabéns.\n')
