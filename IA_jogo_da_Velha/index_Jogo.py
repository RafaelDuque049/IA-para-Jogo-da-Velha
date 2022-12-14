
# Bots/IA
from artificial_intelligence.IA_Player import IA
from Bot.IA_Bot import IA_Player_Bot


repet = Ia = Bot = int()
plays, folder = list(), open('IA_jogo_da_Velha\Game\Function_game\plays.txt', 'r')
none = [plays.append([int(line[n])-1 for n in [1, 5, 9]]) \
    if line.startswith('_') else None for line in folder.readlines()]

try:
    from random import choice
    from time import sleep

    from Game.Function_game.tools_game import visual_game, winner
    
    
    test = True if "Y" == (input('play normal game? [Y/N]:')).upper() else False
    repet_game = 10 if test is True else 5000
    print(f'\n{repet_game} games will be played.\n')

    while repet != repet_game:
        symb_game = choice(['x', 'o', 'o', 'x'])
        game = list([''] for x in range(9))
        
        if test:
            print(f'\nBOT recebeu: {symb_game}\nIA recebeu: {"x" if symb_game == "o" else "o"}')

        while True:
            part = 0

            if test is True: 
                sleep(1)
            
            IA(game, symb="x" if symb_game == "o" else "o")
             
            if test is True: 
                visual_game(game)

            if winner("x" if symb_game == "o" else "o", game, plays) is True:
                Ia += 1
                
                if test is True: 
                    visual_game(game)
                IA(game, status=True)
                IA_Player_Bot(won=True)
                break


            for posi in game:
                if '' not in posi:
                    part += 1
                    
            if part == len(game):
                if test is True:
                    print('no one won.\n')
                break
            
            
            if test is True: 
                sleep(1)
                
            IA_Player_Bot(game, symb_game)
            
            if test is True: 
                visual_game(game)

            if winner(symb_game, game, plays) is True:
                Bot += 1
                IA_Player_Bot(won=True)
                IA(game, status=True)

                if test is True:
                    visual_game(game)
                break
        
        repet += 1
        if repet != repet_game:
            print(f'\r{repet}', end='')
        test = (True if repet == repet_game-1 else test)
        
except KeyboardInterrupt:
    print('\ninterrupted program.')

finally:
    print(f'\ngames played: {repet}\nIA: {Ia}\nbot: {Bot}')
