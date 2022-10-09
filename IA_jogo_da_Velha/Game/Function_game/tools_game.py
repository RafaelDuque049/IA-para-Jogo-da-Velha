# visual do jogo davelha

def visual_game(game):
    s = (f'{" " * 7}')
    print(f'\n{s}|{s}|{s}\n{game[0][0]:^7}|{game[1][0]:^7}|{game[2][0]:^7}\n'
        f'{s}|{s}|{s}\n{"=" * 23}\n{s}|{s}|{s}\n{game[3][0]:^7}|{game[4][0]:^7}'
        f'|{game[5][0]:^7}\n{s}|{s}|{s}\n{"=" * 23}\n{s}|{s}|{s}\n{game[6][0]:^7}'
        f'|{game[7][0]:^7}|{game[8][0]:^7}\n{s}|{s}|{s}\n')



def winner(p, game, combo):
    for number in combo:
        if p in game[number[0]] and p in game[number[1]]and p in game[number[2]]:
            none = [game.pop(number[n]) and game.insert(number[n],\
                ['oOo' if p == 'o' else 'xXx']) for n in range(3)]
            return True

