from time import sleep

option = {
    '1': 'Ver informações da IA(inforamções de Progresso)',
    '2': 'Resetar a IA(Deletar progresso)'
}
link_direct = {
    'random': 'IA_jogo_da_Velha/artificial_intelligence/moves/random.txt',
    'standard': 'IA_jogo_da_Velha/artificial_intelligence/moves/standard.txt',
    'updates_moves': 'IA_jogo_da_Velha/artificial_intelligence/moves/numbers_moves.txt'
}   

print('\nO que deseja fazer?\n\n'\
    f'1.{option.get("1")}\n'\
    f'2.{option.get("2")}\n'\
    f'3.Calcelar ações\n')
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
    sleep(.5)
    lines_random, lines_standard = \
        len((open(link_direct.get("random"), 'r')).readlines()),\
        len((open(link_direct.get("standard"), 'r')).readlines())
    
    confirm = str(input(f'\n{"=-"*40}\nserá deletado ao todo {lines_random+lines_standard} '
        'informações(progresso) da IA. deseja mesmo prosseguir? [S/N]: '))

    if confirm.upper() == 'S':
        sleep(.7)
        
        try:
            del_random = (open(link_direct.get("random"), 'w')).close()
            del_standard = (open(link_direct.get("standard"), 'w')).close()
            del_next_update = (open(link_direct.get("updates_moves"), 'w')).close()

        finally:
            print(f'\ninformações de IA deletada com sucesso.\n{"=-"*40}')

    else:
        print(f'\nfoi cancelado qualquer tipo de ação de deletar informações.'\
            f'nenhuma informação foi deletada.\n{"=-"*40}\n')


elif action == '3':
    print('\nfoi cancelado qualquer tipo de ação.\n')
