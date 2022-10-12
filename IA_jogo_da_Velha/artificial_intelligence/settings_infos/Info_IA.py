from time import sleep

option = {
    '1': 'Ver informações da IA(inforamções de Progresso)'
}
link_direct = {
    'random': 'IA_jogo_da_Velha/artificial_intelligence/moves/random.txt',
    'standard': 'IA_jogo_da_Velha/artificial_intelligence/moves/standard.txt',
    'updates_moves': 'IA_jogo_da_Velha/artificial_intelligence/moves/numbers_moves.txt'
}   

print('\nO que deseja fazer?\n\n'\
    f'1.{option.get("1")}\n'\
    f'2.Calcelar ações\n')
action = str(input("escolha sua ação: "))


if action == '1' or action == '':
    sleep(.7)

    lines_random, lines_standard, next_update = \
        len((open(link_direct.get("random"), 'r')).readlines()),\
        len((open(link_direct.get("standard"), 'r')).readlines()), \
        (open(link_direct.get("updates_moves"), 'r')).readlines()
    
    print(f'\n{"=-"*40}\nforam salvas no total de ({lines_random}) partidas.\n'\
        f'foram reconhecidas ({lines_standard}) jogadas.\n'\
        f'a próxima quantidade de jogadas para a IA estudar '\
        f'é ({next_update[0] if next_update != [] else 0}).\n{"=-"*40}\n')


elif action == '2':
    print('\nfoi cancelado qualquer tipo de ação.\n')
