def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a winning combination
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Check rows
            return True
        if all(board[j][i] == player for j in range(3)):  # Check columns
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):  # Check diagonals
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0
    
    while True:
        print_board(board)
        print("Player", players[current_player])
        
        # Get player's move
        while True:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if board[row][col] == " ":
                board[row][col] = players[current_player]
                break
            else:
                print("That position is already taken!")
        
        # Check for a winner
        if check_winner(board, players[current_player]):
            print_board(board)
            print("Player", players[current_player], "wins!")
            break
        
        # Check for a draw
        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = (current_player + 1) % 2

tic_tac_toe()
