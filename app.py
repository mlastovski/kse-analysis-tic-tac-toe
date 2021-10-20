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
print(now)

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
        return True
    except UnicodeDecodeError:
        return False

def write_to_file(player_one, player_two, player_won, date):
    file_to_write = open('results.txt', 'a')
    output = player_one + ' : ' + player_two + ' - ' + date + ' - ' + player_won 
    file_to_write.write('\n' + output)
    file_to_write.close()


# main game function
def tic_tac_toe():
    while True:
        ask = input('Which action? (play/last-games/statistics): ')

        if ask.lower() == 'play':

            name_one = input('Please enter name of the first player: ')
            name_two = input('Please enter name of the second player: ')

            if check_names(check_name=name_one) == True and check_names(check_name=name_two) == True:

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
                            else:
                                winner = name_two + " (" + player + ") wins."
                                print(winner)
                            write_to_file(name_one, name_two, winner, now)
                            play_again()
                    
                    # if nobody won and moves count = 9, program says it's draw
                    if turns == 9:
                        create_field()
                        winner = 'Draw'
                        write_to_file(name_one, name_two, winner, now)
                        print('Draw')
                        play_again()

                    # to change player every move
                    if player == 'X':
                        player = 'O'
                    else:
                        player = 'X'
            
            else:
                print('Names should contain only latin characters and should be at least 3 characters long.')
                continue

        elif ask.lower() == 'last-games':
            print('last-games is used')

        elif ask.lower() == 'statistics':
            print('statistics is used')

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
