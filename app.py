# -*- coding: utf-8 -*-
from datetime import datetime

# i use dictionary to give possibility for entering the coordinates
field = {
    '1 1': ' ', '1 2': ' ', '1 3': ' ',
    '2 1': ' ', '2 2': ' ', '2 3': ' ',
    '3 1': ' ', '3 2': ' ', '3 3': ' '
}

field_entries = []

allowed_coordinates = [
    '1 1', '1 2', '1 3',
    '2 1', '2 2', '2 3',
    '3 1', '3 2', '3 3'
]

# to check if input has only digits and spaces
allowed_inputs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']

now = str(datetime.now())[:16]

# loop for updating field
for entry in field:
    field_entries.append(entry)


def create_field():
    print('---------')
    print('| ' + field['1 1'] + ' ' + field['1 2'] + ' ' + field['1 3'] + ' |')
    print('| ' + field['2 1'] + ' ' + field['2 2'] + ' ' + field['2 3'] + ' |')
    print('| ' + field['3 1'] + ' ' + field['3 2'] + ' ' + field['3 3'] + ' |')
    print('---------')


def winner_check(sign):
    # horizontal check
    if field['1 1'] == field['1 2'] == field['1 3'] == sign:
        return True

    elif field['2 1'] == field['2 2'] == field['2 3'] == sign:
        return True

    elif field['3 1'] == field['3 2'] == field['3 3'] == sign:
        return True

    # vertical check
    elif field['1 1'] == field['2 1'] == field['3 1'] == sign:
        return True

    elif field['1 2'] == field['2 2'] == field['3 2'] == sign:
        return True

    elif field['1 3'] == field['2 3'] == field['3 3'] == sign:
        return True

    # diagonal check
    elif field['1 1'] == field['2 2'] == field['3 3'] == sign:
        return True

    elif field['1 3'] == field['2 2'] == field['3 1'] == sign:
        return True

    else:
        return False


def check_names(check_name):
    if len(check_name) < 3:
        return False

    try:
        check_name.encode(encoding='utf-8').decode('ascii')
        file_to_read = open('stats.txt', 'r')
        lines = file_to_read.readlines()
        len_of_name = len(check_name)
        new_lines = [x[:len_of_name] for x in lines]

        if bool(check_name in new_lines) == False:
            output = check_name + ' - 0 - 0 - 0'
            file_to_write = open('stats.txt', 'a')
            file_to_write.write('\n' + output)
            file_to_write.close()
        
        file_to_read.close()

        return True
    except UnicodeDecodeError:
        return False

def write_to_file(player_one, player_two, player_won, date):
    file_to_write = open('results.txt', 'a')
    output = player_one + ' : ' + player_two + ' - ' + date + ' - ' + player_won 
    file_to_write.write('\n' + output)
    file_to_write.close()


def stats(player_one, win_first, player_two, win_second):
    file_to_read = open('stats.txt', 'r')
    lines = file_to_read.readlines()
    
    players = []
    for item in lines:
        player_name = item.split(' - ')[0]
        wins = item.split(' - ')[1]
        losses = item.split(' - ')[2]
        draws = item.split(' - ')[3]

        player = {
            'name' : player_name,
            'wins': wins,
            'losses': losses,
            'draws': draws
        }

        players.append(player)

    if win_first == True:
        for e in players:
            if e['name'] == player_one:
                num_of_wins = int(e['wins']) + 1
                e.update({'wins' : num_of_wins})
            if e['name'] == player_two:
                num_of_losses = int(e['losses']) + 1
                e.update({'losses' : num_of_losses})

    if win_second == True:
        for e in players:
            if e['name'] == player_two:
                num_of_wins = int(e['wins']) + 1
                e.update({'wins' : num_of_wins})
            if e['name'] == player_one:
                num_of_losses = int(e['losses']) + 1
                e.update({'losses' : num_of_losses})

    if win_first == False and win_second == False:
        for e in players:
            if e['name'] == player_one:
                num_of_draws = str(int(e['draws']) + 1) + '\n'
                e.update({'draws' : num_of_draws})
            if e['name'] == player_two:
                num_of_draws = str(int(e['draws']) + 1) + '\n'
                e.update({'draws' : num_of_draws})

    file_to_read.close()
    file_to_write = open('stats.txt', 'w')

    statistics = []
    for a in players:
        output = a['name'] + ' - ' + str(a['wins']) + ' - ' + str(a['losses']) + ' - ' + str(a['draws'])
        statistics.append(output)

    for z in statistics:
        file_to_write.write(z)

    file_to_write.close()


# main game function
def tic_tac_toe():
    while True:
        ask = input('Which action? (play/last-games/statistics): ')

        if ask.lower() == 'p':

            name_one = input('Please enter name of the first player: ')
            name_two = input('Please enter name of the second player: ')

            if check_names(name_one) == True and check_names(name_two) == True:

                player = 'X'
                turns = 0

                while turns < 9:
                    create_field()

                    if player == 'X':
                        move = input(name_one + ' (X), enter the coordinates: ')
                    else:
                        move = input(name_two + ' (O), enter the coordinates: ')
                    digits_check = all(c in allowed_inputs for c in move)

                    # input check
                    if digits_check == False:
                        print('You should enter numbers!')
                        continue

                    else:
                        if move not in allowed_coordinates:
                            print('Coordinates should be from 1 to 3!')
                            continue
                    
                    # to check if cell is free
                    if field[move] == ' ':
                        field[move] = player
                        turns += 1

                    else:
                        print('This cell is occupied! Choose another one!')
                        continue

                    # minimal amount of moves needed to win
                    if turns >= 5:
                        if winner_check(player):
                            create_field()

                            if player == 'X':
                                winner = name_one + " (" + player + ") wins."
                                print(winner)
                                stats(name_one, True, name_two, False)
                            else:
                                winner = name_two + " (" + player + ") wins."
                                print(winner)
                                stats(name_one, False, name_two, True)

                            write_to_file(name_one, name_two, winner, now)
                            play_again()
                    
                    # if nobody won and moves count = 9, program says it's draw
                    if turns == 9:
                        create_field()
                        winner = 'Draw'
                        print(winner)

                        write_to_file(name_one, name_two, winner, now)
                        stats(name_one, False, name_two, False)
                        play_again()

                    # to change player every move
                    if player == 'X':
                        player = 'O'
                    else:
                        player = 'X'
            
            else:
                print('Names should contain only latin characters and should be at least 3 characters long.')
                continue

        elif ask.lower() == 'l':
            file_to_read = open('results.txt', 'r')
            lines = file_to_read.readlines()
            last_lines = lines[-10:]

            for i in last_lines:
                print(i)

            file_to_read.close()
            continue

        elif ask.lower() == 's':
            file_to_read = open('stats.txt', 'r')
            lines = file_to_read.readlines()
            
            for item in lines:
                items = item.split(' - ')
                output = items[0] + ' - ' + items[1] + ' wins' + ' - ' + items[2] + ' losses' + ' - ' + items[3].rstrip() + ' draws.'
                print(output)
            
        else:
            print('There is no such action.')
            continue


def play_again():
    play_again = input("Do you want to play again? Y/N: ")

    # here i clear the field by replacing all keys with space symbol
    if play_again.lower() == "y":
        for key in field_entries:
            field[key] = ' '
        tic_tac_toe()
        
    else:
        exit()


if __name__ == '__main__':
    tic_tac_toe()
