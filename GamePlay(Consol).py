# This program is the Console part of our program and that could play buy two player
##################################################################################################

import connectfour
format_list = ['.','R','Y']

newBoard = connectfour.new_game()
def define_color(num:int)->str:
    '''this function define number to color 1 = RED, 2 = YELLOW, 0 = NONE'''
    if num == 1:
        return 'RED'
    elif num == 2:
        return 'YELLOW'
    else:
        return 'NONE'

def change_board_format(dot: int) -> str:
    '''This function change format of board
    from (0,1) base to ('R','Y','.')'''

    if dot == 0:

        return '.'

    elif dot == 1:

        return 'R'

    elif dot == 2:

        return 'Y'


def ask_for_pop_or_drop()->str:
    '''This function ask user about what
    action they try to do pop or drop?'''
    while True:
        command = input('Type DROP for drop action and POP for pop action ?(DROP/POP)')

        if command.strip().upper() == 'DROP'  :
            return command.strip().upper()
        elif command.strip().upper() == 'POP':
            return command.strip().upper()
        else:
            print('Invalid input please choose between "POP" and "DROP" ')



def showing_board(board:[[int]]) -> None:
    '''This function print board for player that can
    help them to understand what is going on in game'''

    row_num = ''
    for num in range(connectfour.BOARD_COLUMNS):
        row_num += str(num + 1) + '   '
    print(row_num)#This part print 1 to 7 on top of the board
    for row in range(connectfour.BOARD_ROWS):
        row_str = ''
        for col in range(connectfour.BOARD_COLUMNS):
            row_str += change_board_format(board[col][row]) + '   '

        print(row_str[:-1])


def take_column_number()->int:
    '''This function take cloumn number fro user '''
    try:
        command = input('Select Columns that you want to drop in (selection is number is between 1 to 7)')
        if 1 <= int(command) <= 7:
            return command

        else:
            print('Please choose number between 1 to 7')
    except ValueError:
        print('Invalid input; Please choose number')



def drop_action(newBoard:connectfour.GameState,dropNum:int)->connectfour.GameState:
    '''This function handel drop action '''
    action = connectfour.drop(newBoard,int(dropNum) - 1)#(-1) is because list index is start with '0'.
    return action

def pop_action(newBoard:connectfour.GameState,dropNum:int)->connectfour.GameState:
    '''This function handel pop action'''

    action = connectfour.pop(newBoard,int(dropNum) - 1)#(-1) is because list index is start with '0'.
    return action















def user_interface():
    '''This is user interface function, everything that player see is in here '''
    newBoard1 = connectfour.new_game()
    while True:
        if newBoard1.turn == 1:
            print("***********************************************************************************\n                  ******  RED TURN ****** \n")
        elif newBoard1.turn == 2:
            print("***********************************************************************************\n                  ******  YELLOW TURN ******\n ")

        try:
            action = ask_for_pop_or_drop()
            if action == 'DROP':
                number1 = take_column_number()
                newBoard1 = drop_action(newBoard1,number1)
                showing_board(newBoard1.board)
            elif action == 'POP':
                number2 = take_column_number()
                newBoard1 = pop_action(newBoard1,number2)
                showing_board(newBoard1.board)

            if connectfour.winner(newBoard1) == connectfour.YELLOW or connectfour.winner(newBoard1) == connectfour.RED :
                print('#########################################################################')
                print('Winner Is Player', define_color(connectfour.winner(newBoard1)))
                print('#########################################################################')
                print('GAME OVER')
                break


        except connectfour.InvalidMoveError:
            print('Invalid Move')





if __name__ == '__main__':

    user_interface()

