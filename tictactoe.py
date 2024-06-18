from random import random


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    # Function to handle player's move
    while True:
        move = input("Enter your move (1-9): ")

        # Check move validity
        if not move.isdigit() or int(move) <= 0 or int(move) > 9:
            print("Invalid move. Please enter a number between 1 and 9.")
            continue #keep prompting user

        move = int(move)  # Convert move to integer

        free_fields = make_list_of_free_fields(board)
        validmove = False
        for (row, col) in free_fields:
            if board[row][col] == str(move):
                board[row][col] = "O"
                validmove = True
                break
        if validmove:
            break
        else:
            print("Field occupied or invalid. Please choose an empty square")


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ["X", "O"]:
                free_fields.append((row, col))
    return free_fields



def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    for conditions in win_conditions:
        if conditions == [sign, sign, sign]:
            return True
    return False
def draw_move(board, difficulty):
    # The function draws the Computer's move and updates the board.
    from random import randrange
    free_fields = make_list_of_free_fields(board)
    if difficulty == "easy":
        activation_probability = 0.3
    elif difficulty == "medium":
        activation_probability = 0.5
    elif difficulty == "hard":
        activation_probability = 0.7
    else:
        raise ValueError("Invalid difficulty. Please choose between 'easy' and 'medium' and 'hard'")

    # Check if BingAI should be activated, alternatively it would js be a random generator
    if random() < activation_probability:
        # BingAI activated 🦾🤖
        # Check for winning move
        for (row, col) in free_fields:
            board[row][col] = "X"
        # Check for computer victory
            if victory_for(board, "X"):
                print(f"The Computer has made a move on box number {row * 3 + col + 1}")
                return
        # Undo the move if no victory
            board[row][col] = str(row * 3 + col + 1)

        # Check for blocking move to block player from winning
        for (row, col) in free_fields:
            board[row][col] = "O"
        # Check for player victory
            if victory_for(board, "O"):
                print(f"The Computer has made a move on box number {row * 3 + col + 1}")
                board[row][col] = "X"
                return
        # Undo the move if no block
            board[row][col] = str(row * 3 + col + 1)

        # Make random move as a last resort
        if free_fields:
            ranrow, rancol = free_fields[randrange(len(free_fields))]
            print(f"The Computer has made a move on box number {board[ranrow][rancol]}")
            board[ranrow][rancol] = "X"  # Update the board with computer move (X)
            return
    else:
        # Dumb computer 🧠❌ (Make a random move without BingAI)
        if free_fields:
            ranrow, rancol = free_fields[randrange(len(free_fields))]
            print(f"The Computer has made a move on box number {board[ranrow][rancol]}")
            board[ranrow][rancol] = "X"  # Update the board with computer move (X)
            return


def stalemate_check(board):
    if len(make_list_of_free_fields(board)) == 0:
        return True

def BingAI_difficulty(board):
    # Function to prompt user for difficulty and return activation probability
    difficulty = input("What difficulty would you like to play? (Easy/Medium/Hard): ").lower()
    if difficulty == "easy":
        return "easy"
    elif difficulty == "medium":
        return "medium"
    elif difficulty == "hard":
        return "hard"
    else:
        print("Invalid difficulty level. Defaulting to Medium.")
        return "medium"

def first_turn(board):
    import random
    playerbet = str(input("Heads or Tails: ")).lower()
    coin = ["heads", "tails"]
    coinflip = random.choice(coin)
    print(f"Coinflip: {coinflip}!")
    if playerbet == coinflip:
        print("Player starts first")
        return True
    else:
        return False

# Game program
# Game board below
board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]
# Display initial board
print("Welcome to Bing Hang's Tic Tac Toe!")
display_board(board)

# Determine BingAI difficulty
difficulty = BingAI_difficulty(board)

# Perform first turn
if first_turn(board):
    enter_move(board)
    display_board(board)
else:
    board[1][1] = "X"
    print("The Computer has made a move on box number 5")
    display_board(board)

while True:
    # Receive and perform player move/check free fields
    enter_move(board)

    # Check player victory
    if victory_for(board,"O"):
        display_board(board)
        print("You've won! Game over")
        break


    # Check stalemate
    if stalemate_check(board):
        print("Stalemate. Game over")
        break

    # Perform computer move and display move
    draw_move(board, difficulty)
    display_board(board)

    # Check computer victory
    if victory_for(board, "X"):
        print("The Computer won! Game over")
        break

    # Check stalemate
    if stalemate_check(board):
        print("Stalemate. Game over")
        break