def player_input():

    '''

    OUTPUT = (PLAYER 1 , PLAYER 2)
    :return:
    '''

    marker = " "

    while marker != 'X' and marker != "O":
        marker = input("Player1: Choose X or O").upper()

    if marker == 'X':

        return ('X','O')
    else:
        return ("O", "x")


player1_marker , player2_marker = player_input()
print(player1_marker)