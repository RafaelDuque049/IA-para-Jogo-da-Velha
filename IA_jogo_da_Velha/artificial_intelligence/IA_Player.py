# inteligência arficial.

def IA(game, _won_=None):
    # quando a váriavel "show_moves" recebendo True, ele vai mostrar as decições tomadas pela IA;
    # "show moves" when it will receive True, it will make decisions for the AI;
    show_moves = False
    
    
    link_direct = {
        'm_random': 'IA_jogo_da_Velha/artificial_intelligence/moves/random.txt',
        'n_moves': 'IA_jogo_da_Velha/artificial_intelligence/moves/numbers_moves.txt'
    }
    
    num_random = len((open(link_direct.get("m_random"), 'r')).readlines())
    random, num = open(link_direct.get("m_random"), 'r').read(), int()
    inicial_game  = str(game)[:]

    # traduz e salva o jogo em uma linguegem compreensível para a IA;
    # translate and save the game in a language incomprehensible to the AI;
    if _won_ != None:
        from artificial_intelligence.moves.identify_pattern import read_game
        
        with open(link_direct.get("m_random"), 'w') as fold:
            fold.write(random), fold.write(read_game(game_p=game))

    if _won_ is False:
        from artificial_intelligence.moves.identify_pattern import del_wrong_plays
        
        del_wrong_plays(game=game)

    # atualizar o numero que define a quantidade de linhas para haver atualização de aprendizado;
    # update the number that defines the number of lines to have a learning update;
    with open(link_direct.get("n_moves"), 'r') as numb:
        
        # verificar se pasta com os numeros de movimentos não está vazia e corrige para evitar erro;
        # check if the folder with the movement numbers is not empty and correct it to avoid errors;
        if len(numb.read()) == 0:
            with open(link_direct.get("n_moves"), 'w') as moves:
                moves.write('2000')     
        
        with open(link_direct.get("n_moves")) as numpt:
            num = numpt.readlines()[0]
        
        if int(num) >= (4000):
            with open(link_direct.get("m_random"), 'w') as close: 
                del close
            with open(link_direct.get("n_moves"), 'w') as moves:
                moves.write('2000')
    
    # verifica a partida e faz um movimento a partir dele;
    # checks the match and makes a move from it;
    if _won_ == None:
        from artificial_intelligence.moves.identify_pattern import move_IA
        
        _pass_ = True
        
        for action in ['x', 'o']:
            if _pass_:
                move_game = move_IA(game_game=game, simb=action)
                
            if str(move_game) != inicial_game:
                if show_moves: 
                    print('attack;' if action == 'x' else 'defense;')
                _pass_ = False
                return move_game

        if _pass_:
            from random import randint as rd
            
            while True:
                num_posi, play_move = int(), rd(0, 8)

                for numb in move_game:
                    if numb[0] == 'x' or numb[0] == 'o':
                        num_posi += 1
 
                if 'o' not in game[play_move][0] and \
                        'x' not in game[play_move][0] or num_posi == 9:
                    game[play_move][0] = 'x'
                    
                    if show_moves: 
                        print('random play;')
                    break
                
            return game

    # define o novo limite de linha;
    # sets the new line boundary
    if num_random >= int(num):
        from artificial_intelligence.moves.identify_pattern import identify 
        
        with open(link_direct.get("n_moves"), 'w') as moves:
            moves.write(str(int(num) + 2000))
        identify()
