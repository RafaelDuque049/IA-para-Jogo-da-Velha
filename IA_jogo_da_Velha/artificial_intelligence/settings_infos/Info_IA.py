from time import sleep


def zero_file(name_folder):
    with open(name_folder, 'w') as delete:
        del delete


def number_lines(name_folder):
    with open(name_folder, 'r') as lines:
        return len(lines.readlines())


link_direct = {
    'random': r'IA_jogo_da_Velha/artificial_intelligence/moves/random.txt',
    'standard': r'IA_jogo_da_Velha/artificial_intelligence/moves/standard.txt'
}   

option = {
    '1': 'Ver informações da IA(inforamções de Progresso)',
    '2': 'Resetar a IA(Deletar progresso)',
    '3': 'deletar informações separadamente'
}

print('\nO que deseja fazer?\n\n'\
    f'1.{option.get("1")}\n'\
    f'2.{option.get("2")}\n'\
    f'3.{option.get("3")}\n'\
    f'4.Calcelar ações\n')

action = str(input("escolha sua ação: "))


if action == '1' or action == str():
    lines_random = number_lines(link_direct.get("random"))
    lines_standard = number_lines(link_direct.get("standard"))
    
    sleep(.7)
    print(f'\n{"=-"*40}\nestão salvas no total de ({lines_random}) partidas.\n'\
        f'foram reconhecidas ({lines_standard}) jogadas.\n{"=-"*40}\n')


elif action == '2':
    lines_random = number_lines(link_direct.get("random"))
    lines_standard = number_lines(link_direct.get("standard"))
    
    sleep(.3)
    while True: 
        confirm = str(input(f'\n{"=-"*40}\nserá deletado ao todo {(lines_random+lines_standard)} '
            'informações(progresso) da IA. deseja mesmo prosseguir? [S/N]: '))
        

        if confirm.upper() == 'S':
            zero_file(link_direct.get("random"))
            zero_file(link_direct.get("standard"))
            
            sleep(.7)
            print(f'\ninformações de IA deletada com sucesso.\n{"=-"*40}')
            break

        elif confirm.upper() == 'N':
            sleep(.3)
            print(f'\nfoi cancelado qualquer tipo de ação de deletar informações.'\
                f'nenhuma informação foi deletada.\n{"=-"*40}\n')
            break


elif action == '3':
    info = {
        '1': link_direct.get("random"),
        '2': link_direct.get("standard")
    }
    
    print(f'\n{"=-"*40}\nopções para deletar:\n\n'
        '1.partidas que foram salvas\n'\
        '2.jogadas identificadas pela IA')

    while True:
        choices = str(input('\n(separado por virgula, desta forma: 2, 1)'\
            ' escolha quais informações deletar(Digite o numero zero para cancelar.): '))
        
        if choices == '0':
            sleep(.3)
            print('\nFoi cancelado ações de deletar progresso da IA.\n')
            break

        try:
            if len(choices) != 1:
                choices = (choices.replace(' ', '')).split(',')

            for choice in choices:
                zero_file(info.get(choice))
                
        except (TypeError or IndexError):
            print('\n/ERRO/\nDigite corretamente quais das opções aparentes deseja deletar.')
            
        else:
            sleep(.4)
            print('\ninformações deletada com sucesso.\n')
            break


elif action == '4':
    print('\nfoi cancelado qualquer tipo de ação.\n')
