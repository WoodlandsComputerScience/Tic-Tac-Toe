import copy

def printBoard(board):
	print(*board,sep='\n')

def checkWin(board):
    # a tuple - (if win exists, returns 1 if player1 wins 0 if player2/CPU wins)
    # check rows and cols
    for i in range(3):
        if(board[i][0] != 0 and board[i][0]==board[i][1] and board[i][1]==board[i][2]):
            return (1, board[i][0] == 1)
        if(board[0][i] != 0 and board[0][i]==board[1][i] and board[1][i]==board[2][i]):
            return (1, board[0][i] == 1)

    # check diagonals
    if(board[0][0] != 0 and board[0][0]==board[1][1] and board[1][1]==board[2][2]):
        return (1, board[1][1] == 1)
    if(board[0][2] != 0 and board[0][2]==board[1][1] and board[1][1]==board[2][0]):
        return (1, board[1][1] == 1)

    return (0, 0)

def botMove(board, depth):
	bestScore = float('inf') # bot wants to minimize score, player wants to maximize
	row, col = -1, -1

	gameWon, player = checkWin(board) # check if game is already won first
	if(gameWon):
		return row, col

	for i in range(3):
		for j in range(3):
			if(board[i][j] == 0): 				# visit each available cell
				temp = copy.deepcopy(board) 	# duplicate original board
				temp[i][j] = 2					# simulate the bot moving to that cell
				score = minimax(temp, depth-1, False)
				if(score < bestScore):
					bestScore = score
					row, col = i, j

	return row, col

def minimax(board, depth, bot):

	gameWon, player = checkWin(board)
	if(gameWon): 
		if(player == 1): return 1 * (depth+1)	# positive score if player wins, negative if bot wins
		else: return -1 * (depth+1)				# multiply by depth to win in the fewest moves possible (+1 to avoid multiplying by 0)

	elif(depth == 0):							# tie score set as 0
		return 0

	if(bot): # bot's turn (minimizing)
		bestScore = float('inf')
		for i in range(3):
			for j in range(3):
				if(board[i][j] == 0):
					temp = copy.deepcopy(board)
					temp[i][j] = 2
					bestScore = min(bestScore, minimax(temp, depth-1, False))
	else: # player's turn (maximizing)
		bestScore = float('-inf')
		for i in range(3):
			for j in range(3):
				if(board[i][j] == 0):
					temp = copy.deepcopy(board)
					temp[i][j] = 1
					bestScore = max(bestScore, minimax(temp, depth-1, True))

	return bestScore


'''
while movesLeft(board): 
	pos = int(input("Which square would you like to mark?\n"))
	x, y = convert(pos) 
	while(board[y][x]!=" "):
		pos = int(input("Which (empty) square would you like to mark?\n"))
		x, y = convert(pos)
	board[y][x] = 'X'
	printBoard(board)
	if(checkWin(board)[0]):
		print("You win!")
		break
	if not movesLeft(board):
		print("It's a tie!")
		break
	cpuMove = bestMove(board)
	print("CPU moves at position:",cpuMove)
	board[(cpuMove-1)//3][cpuMove%3-1] = 'O'
	printBoard(board)
	if(checkWin(board)[0]):
		print("You lose!")
		break
'''

'''
test function to make bot play itself (comment game above)
random is kinda useless (just check if first is each of 9 positions but wtv)
set position only needs to test once 

def test(rand, output): 
	board = [[" " for i in range(3)] for i in range(3)]
	# optional random move 
	if(rand):
		r = __import__("random").randint(1, 9)
		board[(r-1)//3][r%3-1]='X'
	if(output):
		printBoard(board)
		print()
	while movesLeft(board): 
		cpuMove = bestMove(board) 
		board[(cpuMove-1)//3][cpuMove%3-1] = ['X','O'][rand]
		if(output): 
			printBoard(board)
			print()
		if(checkWin(board)[0]): return 0
		cpuMove = bestMove(board) 
		board[(cpuMove-1)//3][cpuMove%3-1] = ['O','X'][rand]
		if(output): 
			printBoard(board)
			print()
		if(checkWin(board)[0]): return 0
		if not movesLeft(board): return 1
for i in range(50):
	assert(test(0, 1)) 
	assert(test(1, 1))
	print(i)
print("Done tests")
''' 