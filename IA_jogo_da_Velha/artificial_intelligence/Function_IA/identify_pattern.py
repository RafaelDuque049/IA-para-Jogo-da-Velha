
# Função que chama a IA para fazer a jogada;
# Function that calls the AI to make the move
def move_IA(game, simb):
    num_cases = sum([(1 if numb[0] == 'x' or numb[0] == 'o' else 0) for numb in game])
        
    if num_cases != 9:
        with open('IA_jogo_da_Velha/artificial_intelligence/moves/standard.txt', 'r') as moves:

            for line in moves.readlines():
                if game[int(line[0])][0] == simb and \
                        game[int(line[1])][0] == simb and game[int(line[2])][0] == '':
                    game[int(line[2])][0] = 'x'
                    break        
        return game


# Função para traduzir a lista recebida para o metodo que a IA compreende;
# Function to translate the received list to the method that the AI understands
def read_game(game_p):
    play = str()

    for word in game_p:
        if word[0] == 'x' or word[0] == 'o':
            play += ('1' if word[0] == 'x' else '0')
            
        elif word[0] == 'xXx' or word[0] == 'oOo':
            play += ('1' if word[0] == 'xXx' else '0')
                   
        elif word[0] == '': 
            play += ('2')
            
    return (play+'\n')


# Função para apagar jogadas desnecessarias;
# Function to delete unnecessary moves
def del_wrong_plays(game):
    moves_save, standard = str(), ('IA_jogo_da_Velha/artificial_intelligence/moves/standard.txt')
        
    with open(standard, 'r') as moves_del:
        for line in moves_del.readlines():
            _pass2_ = True
                
            for simbl in ['x', 'o']:
                if game[int(line[0])][0] == simbl and\
                        game[int(line[1])][0] == simbl and game[int(line[2])][0] == simbl:
                    _pass2_ = False
                        
            if _pass2_ is True:
                moves_save += line
        
    with open(standard, 'w') as moves_del:
        moves_del.write(moves_save)


# Função para retornar as 3 posições mais repetidas;
# Function to return the 4 most repeated positions
def position(lista):                                          
    bigs, list_copy, new_list, num_posi = list(), lista[:], str(), 3

    for x in range(num_posi):
        pos = number = int()

        for posi, posi_2 in enumerate(list_copy):
            if posi_2[1] > number:
                number, pos = posi_2[1], posi

        bigs.append(list_copy[pos][1]), list_copy.pop(list_copy.index(list_copy[pos]))

    for num in bigs:
        for posis, numb in enumerate(lista):
            
            if numb[1] == num:
                new_list += str(posis)

    new_list = (new_list[:num_posi-1] if len(new_list) > num_posi else new_list)
    
    return (new_list+'\n')


# Função para identificar as posições mais repetidas e salvar em forma de lista.
# Function to identify the most repeated positions and save as a list.
def identify():
    moves, moves_in_list = str(), str()
    
    link_direct = {
        'standard_2': 'IA_jogo_da_Velha/artificial_intelligence/moves/standard.txt',
        'random': 'IA_jogo_da_Velha/artificial_intelligence/moves/random.txt'
    }
    
    with open(link_direct.get("standard_2"), 'r') as fold:
        moves_in_list = fold.read()
        
    with open(link_direct.get("random"), 'r') as folder_m:
        no_repet = list()
        
        for move in folder_m.readlines():
            if move not in no_repet:
                list_pos = list([word, 0] for word in move)
                list_pos.pop(-1), no_repet.append(move)

                with open(link_direct.get("random"), 'r') as folder_s:
                    for numbs in folder_s:
                        
                        for pos, case in enumerate(list_pos):
                            list_pos[pos][1] += 1 if case[0] == numbs[pos] else 0
                        nump = position(list_pos)

                        if len(nump) != 4: 
                            None
                        elif nump not in moves and\
                                nump not in moves_in_list:
                            moves += nump

        standard = open(link_direct.get("standard_2"), 'r').read()
        with open(link_direct.get("standard_2"), 'w') as stand:
            stand.write(standard + moves)
