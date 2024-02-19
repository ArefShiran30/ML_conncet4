import Gaming
import GamePlay
import connectfour

POLLING_HOST = 'woodhouse.ics.uci.edu'
POLLING_PORT = 4444


# User interface is the main part of the online part of this project.
# We check step by step each part of this function
# And looking for stable ground from time to time and be careful don't miss any part it

def _run_user_interface() -> None:
    '''
    Runs the console-mode user interface from start to finish.
    '''
    newBoard = connectfour.new_game()
    connection = Gaming.connect(POLLING_HOST, POLLING_PORT)
    print('CONNECTED')
    print()
    _show_welcome_banner() # showing welcome banner of the game that show us the game is start

    try:
        username = _ask_username()
        response = Gaming.welcome(connection, username)
        #print(response)

        if response == Gaming.WELCOME:
            Gaming.ai_game(connection)

            while True:
                move = GamePlay.ask_for_pop_or_drop()
                command1 = _ask_number()
                actionType_and_number = move +' '+str(command1) # This part is string that has action and number like "DROP 2"

                command2 = Gaming.drop_pop_action(connection,actionType_and_number)
                if  command2 == 'OKAY':
                    newBoard = drop_or_pop_check(actionType_and_number, newBoard)
                    GamePlay.showing_board(newBoard.board)
                    command3 = Gaming.server_drop_pop(connection)
                    newBoard = drop_or_pop_check(command3,newBoard)
                    GamePlay.showing_board(newBoard.board)
                    answer = Gaming._read_line(connection)
                    if answer == Gaming.READY:
                        continue
                    elif answer.startswith('WINNER_'):

                        print('WINNER IS PLAYER ' + answer[7:])

                        break

                elif command2 == 'INVALID':
                    #print('INVALID MOVE')
                    if Gaming.ready(connection) == Gaming.READY:
                        continue

                elif command2.startswith('WINNER_'):

                    print('WINNER IS ' + command2[7:])


    finally:

        Gaming.close(connection)




def drop_or_pop_check(move:str,newBoard:connectfour.GameState)->connectfour.GameState:
    '''This function just get action and number and do drop or pop '''

    if move.split()[0] == 'DROP':
        Board = GamePlay.drop_action(newBoard, int(move.split()[1]))
        return Board

    elif move.split()[0] == 'POP':
        Board = GamePlay.pop_action(newBoard, int(move.split()[1]))
        return Board



def _ask_number()-> int:
    '''Ask user for column number from user'''

    while True:
        try:
            drop_input = int(input('Please choose column number for drop'))
            if 1 <= drop_input <= 7:
                return drop_input
            else:
                print('Please choose number between 1  to 7')
        except:
            print('please put number')



def _ask_username() -> str:
    '''this function ask for username'''

    while True:
        username = input('Username: ').strip()

        if len(username.split()) == 1:

            print('Welcome to the connectfour Game ' + username)
            print()
            print('--------------------------------------------------------------------------------')
            return username


        else:
            print('Invalid username ,Please try again')



def _show_welcome_banner() -> None:
    '''
    Shows the welcome banner
    '''
    print('Welcome to the Gaming client!')
    print()
    print('Please select your username to start game ')
    print()


if __name__ == '__main__':
    _run_user_interface()