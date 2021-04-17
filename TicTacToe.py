import pygame, sys, random, math
from BotMoves import botMove

pygame.init()

# size of board (min: 2)
boardSize = 15

# max number of moves (for checking for draws)
maxMoves = boardSize**2

# number of pieces in a row to win (min: 2)
winCondition = 5

# whether or not the bot is activated
botActive = False

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (180, 180, 180)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(WHITE)

def newBoard():
    return [[0] * boardSize for i in range(boardSize)]

# keeps track of the tic-tac-toe board
board = newBoard()
# keep track of how many turns have elapsed
turn = 0

gameEnd = False

score_o = 0
score_x = 0

def renderScore():
    font = pygame.font.SysFont("Source Code Pro", 40)
    label_o = font.render(f"{score_o}", 1, RED)
    screen.blit(label_o, (10, 10))
    label_x = font.render(f"{score_x}", 1, BLUE)
    screen.blit(label_x, (10, 40))
    
# draws a grid onto the screen based on board size
def setup(lineColor, lineWidth):
    for v in range(1, boardSize):
        pygame.draw.line(screen, lineColor, ((SCREEN_WIDTH/boardSize)*v, 0), ((SCREEN_WIDTH/boardSize)*v, SCREEN_HEIGHT), lineWidth)
    for h in range(1, boardSize):
        pygame.draw.line(screen, lineColor, (0, (SCREEN_HEIGHT/boardSize)*h), (SCREEN_WIDTH, (SCREEN_HEIGHT/boardSize)*h), lineWidth)
    renderScore()

def resetBoard():
    global board, turn
    board = newBoard()
    turn = 0
    screen.fill(WHITE)
    setup(BLACK, 5);

def displayBoard():
    for x in range(boardSize):
        print('|', end = '')
        for y in range(boardSize):
            cur = board[x][y]
            print('_' if cur == 0 else ('X' if cur == 1 else 'O'), end = '|')
        print()

# draws X
def drawX(row, col):
    # x pos and y pos both divided by board size to fit
    linePos1 = (((SCREEN_WIDTH*col + 225) / boardSize, (SCREEN_WIDTH*row + 225) / boardSize),
                ((SCREEN_WIDTH*col + 675) / boardSize, (SCREEN_WIDTH*row + 675) / boardSize))
    linePos2 = (((SCREEN_WIDTH*col + 675) / boardSize, (SCREEN_WIDTH*row + 225) / boardSize),
                ((SCREEN_WIDTH*col + 225) / boardSize, (SCREEN_WIDTH*row + 675) / boardSize))
    pygame.draw.line(screen, BLUE, linePos1[0], linePos1[1], 150 // boardSize)
    pygame.draw.line(screen, BLUE, linePos2[0], linePos2[1], 150 // boardSize)

# draws O
def drawO(row, col):
    pygame.draw.circle(screen, RED, ((SCREEN_WIDTH*col + 450) / boardSize,
                                     (SCREEN_WIDTH*row + 450) / boardSize), 320 / boardSize)
    pygame.draw.circle(screen, WHITE, ((SCREEN_WIDTH*col + 450) / boardSize,
                                       (SCREEN_WIDTH*row + 450) / boardSize), 203 / boardSize)

# draws rectangle at the center of the screen using given colour
def drawEndRectangle(colour):
    s = pygame.Surface((750, 225))  # the size of your rect
    s.set_alpha(200)                # alpha level
    s.fill((colour))                # this fills the entire surface
    screen.blit(s, (75, 337))       # (0,0) are the top-left coordinates
    pygame.draw.rect(screen, BLACK, pygame.Rect(75, 337, 750, 225), 6)

# displays message at the center of the screen
def displayMessage(message, y):
    font = pygame.font.SysFont("Source Code Pro", 60)
    displayText = font.render(message, 1, BLACK)
    displayPosition = displayText.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + y))
    screen.blit(displayText, displayPosition)

def checkWin(board, winCondition): 
    # a tuple - (if win exists, returns 1 if player1 wins 0 if player2/CPU wins)
    # check rows and cols
    for i in range(boardSize):
        streak = 0
        if(board[i][0] != 0):
            streak = 1
        for m in range(1, boardSize):
            if(board[i][m] == 0):
                streak = 0
            elif(board[i][m] != board[i][m - 1]):
                streak = 1
            else:
                streak += 1
                if(streak == winCondition):
                    print("Horizontal Win")
                    return (1, board[i][m] == 1)
        streak = 0
        if(board[0][i] != 0):
            streak = 1
        for n in range(1, boardSize):
            if(board[n][i] == 0):
                streak = 0
            elif(board[n][i] != board[n - 1][i]):
                streak = 1
            else:
                streak += 1
                if(streak == winCondition):
                    print("Vertical Win")
                    return (1, board[n][i] == 1)
    # check diagonals
    for i in range(boardSize):
        streak = 0
        if(board[i][0] != 0):
            streak = 1
        for m in range(1, boardSize - i):
            if(board[i + m][m] == 0):
                streak = 0
            elif(board[i + m][m] != board[i + m - 1][m - 1]):
                streak = 1
            else:
                streak += 1
                if(streak == winCondition):
                    print("Left diagonal win 1")
                    return (1, board[i + m][m] == 1)
    for i in range(boardSize):
        streak = 0
        if(board[0][i] != 0):
            streak = 1
        for n in range(1, boardSize - i):
            if(board[n][i + n] == 0):
                streak = 0
            elif(board[n][i + n] != board[n - 1][i + n - 1]):
                streak = 1
            else:
                streak += 1
                if(streak == winCondition):
                    print("Right diagonal win 1")
                    return (1, board[n][i + n] == 1)
    for i in range(boardSize):
        streak = 0
        if(board[i][0] != 0):
            streak = 1
        for m in range(1, i + 1):
            if(board[i - m][m] == 0):
                streak = 0
            elif(board[i - m][m] != board[i - m + 1][m - 1]):
                streak = 1
            else:
                streak += 1
                if(streak == winCondition):
                    print("Left diagonal win 2")
                    return (1, board[i - m][m] == 1)
    for i in range(boardSize):
        streak = 0
        if(board[boardSize - 1][i] != 0):
            streak = 1
        for m in range(2, boardSize - i + 1):
            if(board[boardSize - m][i + m - 1] == 0):
                streak = 0
            elif(board[boardSize - m][i + m - 1] != board[boardSize - m + 1][i + m - 2]):
                streak = 1
            else:
                streak += 1
                if(streak == winCondition):
                    print("Right diagonal win 2")
                    return (1, board[boardSize - m][i + m - 1] == 1)
    return (0, 0) 

setup(BLACK, 5);
pygame.display.update()

while(True):
    for ev in pygame.event.get():
        if(ev.type == pygame.QUIT):
            sys.exit()
        # check if the game has ended and is waiting to restart
        if(gameEnd and ev.type == pygame.MOUSEBUTTONDOWN):
            gameEnd = False
            resetBoard()
        # game still active, user clicks on screen
        elif(ev.type == pygame.MOUSEBUTTONDOWN):
            x = ev.pos[0]
            y = ev.pos[1]
            
            # calculate where in the 3x3 grid the user clicked
            row = y // math.ceil((SCREEN_HEIGHT / boardSize))
            col = x // math.ceil((SCREEN_WIDTH / boardSize))
            
            # check that the spot in the board is empty
            if(board[row][col] == 0):
                print(str(row) + " " + str(col))
                if(botActive):
                    # X
                    drawX(row, col)
                    board[row][col] = 1
                    turn += 1

                    # O
                    botRow, botCol = botMove(board, maxMoves-turn, boardSize, winCondition)
                    if(botRow != -1):
                        drawO(botRow, botCol)
                        board[botRow][botCol] = 2
                        turn += 1
                else:
                    if(turn % 2):
                        drawO(row, col)
                        board[row][col] = 2
                    else:
                        drawX(row, col)
                        board[row][col] = 1
                    turn += 1
                # print board state to terminal
                # commented out because this is slow for larger boards
                # displayBoard()

                # check to see if the game has been won using checkWin function
                gameWon, player = checkWin(board, winCondition)
                if(gameWon):
                    if(player == 0):
                        score_o += 1
                        # draw rectangle for end screen, tint colour of the winning player
                        drawEndRectangle((240,180,180))
                    else:
                        score_x += 1
                        drawEndRectangle((180,180,240))
                    # display game over message
                    displayMessage("Game over. " + ("X" if player else "O") + " won!", -30)
                    print(("X" if player else "O") + " won!")
                
                # board is full, game is drawn
                elif(turn == maxMoves):
                    drawEndRectangle(GREY)
                    font = pygame.font.SysFont("Source Code Pro", 60)
                    displayMessage("Game over. It's a draw!", -30)
                    print("DRAW!")
                
                # game ends
                if(gameWon or turn == maxMoves):
                    # print end screen text
                    displayMessage("Click again to reset.", 30)
                    
                    # wait for player to click to reset
                    print(f"Scores\n * O: {score_o}\n * X: {score_x}")
                    print("Waiting for reset...")
                    gameEnd = True

        pygame.display.update()
