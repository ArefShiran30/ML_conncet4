from collections import namedtuple
import socket

WELCOME = 0
ERROR = 1
READY = 2
OKAY = 3
INVALID = 4




class GamingProtocolError (Exception):
    pass

GamingConnection = namedtuple(
    'PollingConnection',
    ['socket', 'input', 'output'])




def connect(host: str, port: int)->GamingConnection:
    '''This function connect our program to the server'''
    gaming_socket = socket.socket()

    gaming_socket.connect((host, port))

    polling_input = gaming_socket.makefile('r')
    polling_output = gaming_socket.makefile('w')

    return GamingConnection(socket=gaming_socket,input=polling_input,output=polling_output)


def welcome(connection: GamingConnection, username: str)-> WELCOME :
    '''This function is for the WELCOME respond'''
    _write_line(connection, 'I32CFSP_HELLO ' + username)
    respond = _read_line(connection)
    if respond == 'WELCOME'+' '+username:
        return WELCOME
    else:
        print("ERROR")
        raise  GamingProtocolError #raise ERROR if respond not WELCOME



def ai_game(connection:GamingConnection)->READY:
    '''when player type AI_GAME
    respond is going to be ready '''
    _write_line(connection, 'AI_GAME')
    respond = _read_line(connection)
    if respond == 'READY':
        return READY
    else:
        raise GamingProtocolError #raise ERROR if respond not READY


# I use basic idea in this part of my program and that
# Idea is to make one pop and drop function for server and one for human user
# this idea make sense with drop or pop check function in Gaming_ui file
# with this idea program be more clean and professional.





def drop_pop_action(connection:GamingConnection,move:str)->str:
    '''This function is for drop and pop input from user,
    respond that these function could take  '''
    _write_line(connection,move)
    respond = _read_line(connection)
    print(respond)

    if respond == 'OKAY':
        return respond
    elif respond == 'INVALID':
        return respond
    elif respond.startswith('WINNER_'):
        #print(respond)
        return respond
    elif respond.startswith('ERROR'):
        print('ERROR')
        raise GamingProtocolError #raise ERROR if respond not OKAY, INVALID , WINNER





def server_drop_pop(connection: GamingConnection) -> str:
    '''Function handel sever action in this program'''
    respond = _read_line(connection)
    print(respond)
    if respond.startswith('DROP'):

        return respond
    elif respond.startswith('POP'):
        return respond
    else:
        print('ERROR')
        raise GamingProtocolError



def ready(connection: GamingConnection) -> READY:
    respond = _read_line(connection)
    if respond == 'READY':
        return READY



##############################################################################################

def _read_line(connection: GamingConnection) -> str:
    '''
    Reads a line of text sent from the server and returns it without
    a newline on the end of it
    '''
    line = connection.input.readline()[:-1]
    return line


def _write_line(connection: GamingConnection, line: str) -> None:
    '''
    Writes a line of text to the server, including the appropriate
    newline sequence, and ensures that it is sent immediately.
    '''
    connection.output.write(line + '\r\n')
    connection.output.flush()



###########################################################################################################


def close(connection: GamingConnection) -> None:
    'Closes the connection to the Polling server'

    # To close the connection, we'll need to close the two pseudo-file
    # objects and the socket object.
    connection.input.close()
    connection.output.close()
    connection.socket.close()
