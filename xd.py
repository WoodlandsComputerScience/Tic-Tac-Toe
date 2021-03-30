import copy

def printBoard(board):
	print(*board,sep='\n')

def checkWin(board): 
	# a tuple - (if win exists, 1 if player wins 0 if CPU wins)
	for i in range(3):
		if(board[i][0] != " " and board[i][0]==board[i][1] and board[i][1]==board[i][2]):
			return (1, board[i][0] == 'X')
		if(board[0][i] != " " and board[0][i]==board[1][i] and board[1][i]==board[2][i]):
			return (1, board[0][i] == 'X')
	if(board[0][0] != " " and board[0][0]==board[1][1] and board[1][1]==board[2][2]):
		return (1, board[1][1] == 'X')
	if(board[0][2] != " " and board[0][2]==board[1][1] and board[1][1]==board[2][0]):
		return (1, board[1][1] == 'X')
	return (0, 0) 

def movesLeft(board):
	res = 0 
	for i in range(3):
		for j in range(3):
			res += board[i][j]==" "
	return res>0

def minimax(board, depth, player):
	win, result = checkWin(board)
	if(win): 
		if(result == 1): return 100 - depth 
		else: return -100 + depth 
	elif not movesLeft(board): 
		return 0
	if(player==0): # 0 -> player
		bestScore = -float('inf')
		for i in range(1,10):
			if(board[(i-1)//3][i%3-1] ==" "): 
				tmp = copy.deepcopy(board)
				tmp[(i-1)//3][i%3-1] = "X"
				bestScore = max(bestScore, minimax(tmp, depth+1, 1))
		return bestScore
	else:
		bestScore = float('inf')
		for i in range(1,10):
			if(board[(i-1)//3][i%3-1]==" "): 
				tmp = copy.deepcopy(board) 
				tmp[(i-1)//3][i%3-1] = "O"
				bestScore = min(bestScore, minimax(tmp, depth+1, 0))
		return bestScore

def bestMove(board):
	move, val = -1, float('inf')
	for i in range(1, 10): 
		if(board[(i-1)//3][i%3-1]==" "):
			tmp = copy.deepcopy(board)
			tmp[(i-1)//3][i%3-1]="O"
			score = minimax(tmp, 0, 0)
			if(score<val):
				move, val = i, score 
	return move

def convert(pos): 
	return pos%3-1, (pos-1)//3 

board = [[" " for i in range(3)] for i in range(3)]
print('''Board Layout: 
1 | 2 | 3 
4 | 5 | 6 
7 | 8 | 9''')

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