#Design the board
def print_tic_t_t(values):
    print("\n")
    print("\t      |      |")
    print("\t  {}   |  {}   |   {}".format(values[0],values[1],values[2]))
    print('\t------|------|------')

    print("\t      |      |")
    print("\t  {}   |  {}   |   {}".format(values[3],values[4],values[5]))
    print('\t------|------|------')

    print("\t      |      |")

    print("\t  {}   |  {}   |   {}".format(values[6],values[7],values[8]))
    print("\t      |      |")
    print("\n")

#function to print the score -board for the game
def print_scoreboard(score_board):
    print("\t-----------------------------------------------")
    print("\t               SCOREBOARD FOR TIC TAC TOE      ") 
    print("\t-----------------------------------------------") 

    players=list(score_board.keys())
    print( "\t ", players[0],   "\t ", score_board[players[0]])
    print( "\t ", players[1],  "\t ", score_board[players[1]])

    print("\t-----------------------------------------------\n")

#function to check if any players has won the game
def check_winner(player_position, current_player):

    #All possible winning combinations for the players

    soln= [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

    #loop to check if any winning combination is satisfied or not
    for x in soln:            
        if all(y in player_position[current_player] for y in x):  
           
            # Return True if any winning combination satisfies in the iteration
            return True

            
    #Return False if the above combination is not satisfied
    return False

#function to check if the game is a draw
def check_draw(player_position):
    if len(player_position['X']) + len(player_position['O']) == 9:
        return True
    return False

#function for a single Tic tac toe game
def single_game(current_player):

    # represents the Tic tac toe
    values = [' ' for x in range(9)]# space character defines that no players have  occupied that position.

    # stores the positions occupied by X and O
    player_position={'X':[], 'O': []}

    # Game Loop for a single game of Tic Tac Toe
    while True:
        print_tic_t_t(values)
        # try exception block for Move input
        try:
              print("player ", current_player, "turn. which box? :",end="")
              inp=int(input("enter the number 1-9:"))
        except ValueError:
            print("Wrong input!!! try Again")
            continue

          # sanity check for Move inout  
        if inp < 1 or inp > 9:
            print("please choose the right number between 1 to 9")
            continue

         # Check if the cell is occupied or not
        if values[inp-1] != ' ':
            print("The Place you have chosen is already filled.Try again!!")
            continue

        # Update game status
        # updating board status
        values[inp-1]= current_player

        # Updating player positions
        player_position[current_player].append(inp)

        # function call for checking winner
        if check_winner(player_position, current_player):
            print_tic_t_t(values)
            print("player ", current_player, "has won the game!!")
            print("\n")
            return current_player


        # function call for checking draw game

        if check_draw(player_position):
            print_tic_t_t(values)
            print("Game is a Draw")
            print("\n")
            return 'D'


        # switch player moves
        if current_player =='X':
            current_player ='O'
        else:
            current_player ='X'
if __name__ == "__main__": 

    print(" player 1 Details ")
    play1 = input("enter the name of the Player : ")
    print("\n")


    print("Player 2 details ")
    play2 = input("enter the name of the Player :")
    print("\n")

    #Stores the player who chooses X and O
    current_player=play1

    #stores the choice of players character
    player_choice = {'X': "",'O': ""}

    #Stores the options
    options = ['X','O']


    #stores the scoreboard details
    score_board = {play1: 0, play2: 0}
    print_scoreboard(score_board)

    # Game Loop for a series of Tia tac toe
    # the loop runs until either of the players choose to quit
    while True:

        # Player choice Menu
        print("Turn to choose for ", current_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit") 

        # Try exception for CHOICE input
        try:
            choice = int(input())
        except ValueError:
            print("wrong Input!!!  Try Again\n")
            continue

        # Conditions for player choice
        if choice == 1:
            player_choice['X'] = current_player
            if current_player == play1:
                player_choice['O'] = play2
            else:
                player_choice['O'] = play1 

        elif choice == 2:
            player_choice['O'] = current_player
            if current_player == play1:
                player_choice['X'] = play2
            else:
                player_choice['X'] = play1    

        elif choice == 3:
            print("final Scores")
            print_scoreboard(score_board)
            break
        else:
            print("wrong choice !!! Try Again\n")

        # stores the winner in a single game of Tic Tac Toe
        winner= single_game(options[choice-1])

        # scoreboard edits according to the winner
        if winner !='D': ##'D' stand for draw.
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1

        print_scoreboard(score_board)
        # switch player who chooses X or O
        if current_player == play1:
            current_player = play2 

        else:
            current_player = play1


























