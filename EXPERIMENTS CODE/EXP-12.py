board = ["X", "O", "X",
         "O", "X", "O",
         "O", "X", "X"]

print("Tic-Tac-Toe Board:")

for i in range(0, 9, 3):
    print(board[i], board[i+1], board[i+2])

if board[0] == board[4] == board[8]:
    print("Winner:", board[0])
elif board[2] == board[4] == board[6]:
    print("Winner:", board[2])
else:
    print("Game Completed")
