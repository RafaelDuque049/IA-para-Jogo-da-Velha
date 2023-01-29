# artificial intelligence for tic-tac-toe

def IA(game, symb='x', status=None):
    """
    :param-game: receives the current status of the game as a parameter.
    :param-symb: receive which symbol received to play.
    :param-status: receives the information whether the match was won or not.
    
    :return: returns a best move at the moment according to the AI's decision.
    """
    
    # quando a váriavel "show_moves" recebendo True, ele vai mostrar as decições tomadas pela IA;
    # "show moves" when it will receive True, it will make decisions for the AI;
    show_moves = False
    
    
    link_direct = {
        'moves_random': 'artificial_intelligence/moves/random.txt'
    }
    
    num_random = len((open(link_direct["moves_random"], 'r')).readlines())
    random = open(link_direct["moves_random"], 'r').read()
    inicial_game  = str(game)[:]

    # traduz e salva o jogo em uma linguegem compreensível para a IA;
    # translate and save the game in a language incomprehensible to the AI;
    if status != None:
        from artificial_intelligence.Function_IA.identify_pattern import read_game
        
        with open(link_direct["moves_random"], 'w') as fold:
            fold.write(random)
            fold.write(read_game(game_p=game))

    # Deletar jogadas erradas aprendidas;
    # Delete learned wrong moves
    if status is True:
        from artificial_intelligence.Function_IA.identify_pattern import del_wrong_plays
        
        del_wrong_plays(game=game)
            

    # verifica a partida e faz um movimento a partir dele;
    # checks the match and makes a move from it;
    if status == None:
        from artificial_intelligence.Function_IA.identify_pattern import move_IA

        move_game, _pass_ = list(), True
        
        for action in ['x', 'o']:
            
            if _pass_:
                move_game = move_IA(game=game, symb=symb, check_symb=action)
                
            if str(move_game) != inicial_game:
                if show_moves: 
                    print('attack;' if action == 'x' else 'defense;')
                    
                _pass_ = False
                
                return move_game

        if _pass_:
            from random import randint as rd
            
            while True:
                num_posi, play_move = int(), rd(0, 8)

                for numb in move_game or []:
                    if numb[0] == 'x' or numb[0] == 'o':
                        num_posi += 1
 
                if 'o' not in game[play_move][0] and \
                        'x' not in game[play_move][0] or num_posi == 9:
                    game[play_move][0] = symb
                    
                    if show_moves: 
                        print('random play;')
                    break
                
            return game

    # Função para a IA analisar o histórico de partidas e receber novos resultados para a aprendizagem;
    # Function for AI to analyze match history and receive new results for learning;
    if num_random >= 500:
        from artificial_intelligence.Function_IA.identify_pattern import identify 
        
        identify()  
        with open(link_direct["moves_random"], 'w') as close: 
            del close
