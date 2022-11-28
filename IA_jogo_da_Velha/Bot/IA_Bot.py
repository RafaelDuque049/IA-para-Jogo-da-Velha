# "BOT_Player"

def IA_Player_Bot(game=[], simb='x', won=False):
    """
    :param: recebe como parâmetro a situação atual da partida.
    :param: receives the current status of the game as a parameter.
    
    :return: ele retorna uma resposta que se adequa a uma das jogadas salvas.
    :return: it returns an answer that fits one of the saved rolls.
    """
    
    if won is False:
        Folder_move = open('IA_jogo_da_Velha/Game/Function_game/plays.txt', 'r')
        x_o, simb_en, passs = simb, 'o' if simb == 'x' else 'x', True
        
        # Função de ataque
        for line in Folder_move.readlines():
            if line.startswith('_'):
                if x_o in game[int(line[1])-1] and \
                        x_o in game[int(line[5])-1] and '' in game[int(line[9])-1]:
                    game[int(line[9])-1][0], passs = x_o, False
                    break
        Folder_move.seek(0)

        # Função de defesa
        if passs is True:
            for line in Folder_move.readlines():
                if line.startswith('_'):
                    if simb_en in game[int(line[1])-1] and \
                            simb_en in game[int(line[5])-1] and '' in game[int(line[9])-1]:
                        game[int(line[9])-1][0], passs = x_o, False
                        break
        Folder_move.close()

        # Função de jogada aleatória
        if passs is True:
            from random import randint
            
            while True:
                move = randint(0, 8)
                if simb_en not in game[move][0] and x_o not in game[move][0]:
                    game[move][0] = x_o
                    break
