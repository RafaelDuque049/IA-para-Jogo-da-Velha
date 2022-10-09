
# Bots/IA
from artificial_intelligence.IA_Player import IA
from Bot.IA_Bot import IA_Player_Bot


repet = Ia = Bot = int()
plays, folder = list(), open('IA_jogo_da_Velha\Game\Function_game\plays.txt', 'r')
none = [plays.append([int(line[n])-1 for n in [1, 5, 9]]) \
    if line.startswith('_') else None for line in folder.readlines()]

try:
    from time import sleep
    from Game.Function_game.tools_game import visual_game, winner

    test = True if "Y" == (input('play normal game? Y/N:')).upper() else False
    repet_game = 10 if test is True else 50000
    print(f'\n{repet_game} games will be played.\n')

    while repet != repet_game:
        game = list([''] for num in range(9))

        while True:
            part = 0

            if test is True: 
                sleep(1.5)
            IA(game)
            if test is True: 
                visual_game(game)

            if winner('x', game, plays) is True:
                Ia += 1
                if test is True: 
                    visual_game(game)
                IA(game, _won_=True), IA_Player_Bot(won=True)
                break


            for posi in game:
                if '' not in posi:
                    part += 1
                    
            if part == len(game):
                if test is True:
                    print('no one won.\n')
                break
            
            if test is True: 
                sleep(1.5)
            IA_Player_Bot(game, 'o')
            if test is True: 
                visual_game(game)

            if winner('o', game, plays) is True:
                Bot += 1

                if test is True:
                    visual_game(game)
                
                IA_Player_Bot(won=True), IA(game, _won_=False)
                break
        
        repet += 1
        if repet != repet_game:
            print(f'\r{repet}', end='')
        test = True if repet == repet_game-1 else test
        
except KeyboardInterrupt:
    print('\ninterrupted program.')

finally:
    print(f'\ngames played: {repet}\nIA: {Ia}\nbot: {Bot}')
