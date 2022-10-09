# inteligência arficial.

def IA(game, _won_=None):
    # com a váriavel "deep_learning" recebendo True, a IA vai receber mais dados para identificar\
    # padrão e aprender a jogar, fazendo ela aprender mais com menos verificações;
    
    # ALERT: com essa função ativa, o tempo de verificação é aumentado drasticamente;
    deep_learning = False
    # quando a váriavel "show_moves" recebendo True, ele vai mostrar as decições tomadas pela IA;
    show_moves = False
    
    
    link_direct = {
        'm_random': 'IA_jogo_da_Velha/artificial_intelligence/moves/random.txt',
        'n_moves': 'IA_jogo_da_Velha/artificial_intelligence/moves/numbers_moves.txt'
    }
    
    num_random, random, num = len((open(link_direct.get("m_random"), 'r')).readlines()),\
        open(link_direct.get("m_random"), 'r').read(), int()
    inicial_game  = str(game)[:]

    # traduz e salva o jogo em uma linguegem compreensível para a IA;
    if _won_ != None:
        from artificial_intelligence.moves.iden_padrão import read_game
        
        with open(link_direct.get("m_random"), 'w') as fold:
            fold.write(random), fold.write(read_game(game_p=game))

    # verifica se no jogo que foi perdido, tem uma jogada aprendida salva. se houver será deletada;
    if _won_ is False:
        from artificial_intelligence.moves.iden_padrão import del_wrong_plays
        del_wrong_plays(game=game)

    # atualizar o numero que define a quantidade de linhas para haver atualização de aprendizado;
    with open(link_direct.get("n_moves"), 'r') as numb:
        
        # verificar se pasta com os movimentos não está vazia para evitar qualquer erro,
        # se estiver vazia é preenchida;
        if len(numb.read()) == 0:
            with open(link_direct.get("n_moves"), 'w') as moves:
                moves.write('4000' if deep_learning else '2000')     
        
        # a váriavel "num" recebi o numero de jogadas aleatórias salvas;
        with open(link_direct.get("n_moves")) as numpt:
            num = numpt.readlines()[0]
        
        # limpa o histórico salvo de partidas aleatórias e reseta o numero de jogos salvos;
        if int(num) >= (16000 if deep_learning is True else 4000):
            with open(link_direct.get("m_random"), 'w') as close: del close
            with open(link_direct.get("n_moves"), 'w') as moves:
                moves.write('4000' if deep_learning else '2000')
    
    # verifica a partida e faz um movimento a partir dele;
    if _won_ == None:
        from artificial_intelligence.moves.iden_padrão import move_IA
        
        _pass_ = True
        
        for action in ['x', 'o']:
            if _pass_:
                move_game = move_IA(game_game=game, simb=action)
                
            if str(move_game) != inicial_game:
                if show_moves: 
                    print('attack;' if action == 'x' else 'defense;')
                _pass_ = False
                return move_game

        # jogada aleatória caso o jogo não se adequa a nenhuma jogada salva;
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

    # soma a quantidade a qauntidade de linhas atual mais um numero pré definido
    # para impor limite para a próxima atualização.
    if num_random >= int(num):
        from artificial_intelligence.moves.iden_padrão import identificar
        
        with open(link_direct.get("n_moves"), 'w') as moves:
            moves.write(str(int(num)+(4000 if deep_learning else 2000)))
        identificar()
