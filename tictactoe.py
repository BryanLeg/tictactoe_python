# empty list to create the board
board = [" " for _ in range(9)]
# initial state to define player turn
player = 1
# initial state to define if the games is in progress
in_progress = True


def show_board(board: list) -> list:
    """Takes an empty list, returns a list to show a board

    Args:
        board (list): an empty list

    Returns:
        list: a list to show the board
    """
    print("     0)  1)  2)")
    print("   -------------")
    print("0)", end='')
    for i in range(3):
        print(" | "+str(board[i]), end='')
    print(" |")
    print("   -------------")
    print("1)", end='')
    for i in range(3):
        print(" | "+str(board[i+3]), end='')
    print(" |")
    print("   -------------")
    print("2)", end='')
    for i in range(3):
        print(" | "+str(board[i+6]), end='')
    print(" |")
    print("   -------------")

# Show the initial board
show_board(board)
print("Player 1 takes X and player 2 takes O", end="\n - \n")

def turn(board: list, player: int) -> list:
    """Takes a list and the number of current player, return a list with the action of the current player

    Args:
        board (list): a list wich symbolises the board
        player (int): current player turn

    Returns:
        list: the board with the action of the player
    """
    print(f'Turn of player {str(player)}: ', end="\n - \n")
    column= input("Type column number for your next action: ")
    raw= input("Type raw number for your next action: ")
    print(f"You decided to play in case: ({column}, {raw})", end="\n - \n")

    # In case the player try to play in a position already occupied
    while board[int(column)+int(raw)*3] != " ":
        show_board(board)
        print("This position is already occupied! Type a new one please")
        column= input("Type column number for your next action: ")
        raw= input("Type raw number for your next action: ")
        print(f"You decided to play in case: ("+column+", "+raw+")")

    # Select symbol of current player
    if player == 1:
        board[int(column)+int(raw)*3]="X"
    if player == 2:
        board[int(column)+int(raw)*3]="O"

    show_board(board)

def winner(board:list) -> bool:
    """Takes a list, return true if 3 symbols are align

    Args:
        board (list): a list wich symbolises the board

    Returns:
        bool: return true if 3 symbols are align
    """
    # check raws
    if board[0] == board[1] == board[2] != " ":
        return True
    if board[3] == board[4] == board[5] != " ":
        return True
    if board[6] == board[7] == board[8] != " ":
        return True

    # check columns
    if board[0] == board[3] == board[6] != " ":
        return True
    if board[1] == board[4] == board[7] != " ":
        return True
    if board[2] == board[5] == board[8] != " ":
        return True
    
    # check diagonals
    if board[0] == board[4] == board[8] != " ":
        return True
    if board[2] == board[4] == board[6] != " ":
        return True

def draw(board: list) -> bool:
    """Takes a list, return true if the board is full

    Args:
        board (list): a list wich symbolizes the board

    Returns:
        bool: return true if the board is full, or return false
    """

    for i in range(9):
        if board[i] == " ":
            return False
    return True
    
while in_progress:
    turn(board, player)
    if winner(board):
        print(f"Player {player} wins the game")
        in_progress = False
    else:
        if draw(board):
            print("No more space, it's a draw!")
            in_progress = False
    if player == 1:
        player = 2
    else:
        player = 1
