import pygame, sys, random
from BotMoves import botMove

pygame.init()

# size of board (min: 3)
boardSize = 15

# max number of moves (for checking for draws)
maxMoves = boardSize**2

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

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
    font = pygame.font.SysFont("Source Code Pro", 28)
    label_o = font.render(f"{score_o}", 1, RED)
    screen.blit(label_o, (10, 10))
    label_x = font.render(f"{score_x}", 1, BLUE)
    screen.blit(label_x, (10, 30))
    
# draws a grid onto the screen based on board size
def setup(lineColor, lineWidth):
    for v in range(boardSize-1):
        pygame.draw.line(screen, lineColor, ((SCREEN_WIDTH//boardSize)*(v+1), 0), ((SCREEN_WIDTH//boardSize)*(v+1), SCREEN_HEIGHT), lineWidth)
    for h in range(boardSize-1):
        pygame.draw.line(screen, lineColor, (0, (SCREEN_HEIGHT//boardSize)*(h+1)), (SCREEN_WIDTH, (SCREEN_HEIGHT//boardSize)*(h+1)), lineWidth)
    renderScore()

def resetBoard():
    global board, turn
    board = newBoard()
    turn = 0
    screen.fill(WHITE)
    setup(BLACK, 5);

def displayBoard():
    for x in range(boardSize):
        print("|", end="")
        for y in range(boardSize):
            cur = board[x][y]
            print("_" if cur == 0 else ("X" if cur == 1 else "O"), end = "|")
        print()

# draws X
def drawX(row, col):
    linePos1 = ((SCREEN_WIDTH/boardSize*col+50*3/boardSize,SCREEN_WIDTH/boardSize*row+50*3/boardSize),
                (SCREEN_WIDTH/boardSize*col+150*3/boardSize,SCREEN_WIDTH/boardSize*row+150*3/boardSize))
    linePos2 = ((SCREEN_WIDTH/boardSize*col+150*3/boardSize,SCREEN_WIDTH/boardSize*row+50*3/boardSize),
                (SCREEN_WIDTH/boardSize*col+50*3/boardSize,SCREEN_WIDTH/boardSize*row+150*3/boardSize))
    pygame.draw.line(screen, BLUE, linePos1[0], linePos1[1], int(30*3/boardSize))
    pygame.draw.line(screen, BLUE, linePos2[0], linePos2[1], int(30*3/boardSize))

# draws O
def drawO(row, col):
    pygame.draw.circle(screen, RED, (SCREEN_WIDTH/boardSize*col + 100*3/boardSize,
                                     SCREEN_WIDTH/boardSize*row + 100*3/boardSize), 70*3/boardSize)
    pygame.draw.circle(screen, WHITE, (SCREEN_WIDTH/boardSize*col + 100*3/boardSize,
                                       SCREEN_WIDTH/boardSize*row + 100*3/boardSize), 45*3/boardSize)

# draws rectangle at the center of the screen using given colour
def drawEndRectangle(colour):
    s = pygame.Surface((500, 150))  # the size of your rect
    s.set_alpha(200)                # alpha level
    s.fill((colour))                # this fills the entire surface
    screen.blit(s, (50, 225))       # (0,0) are the top-left coordinates
    pygame.draw.rect(screen, BLACK, pygame.Rect(50, 225, 500, 150), 6)

# displays message at the center of the screen
def displayMessage(message, y):
    font = pygame.font.SysFont("Source Code Pro", 40)
    displayText = font.render(message, 1, BLACK)
    displayPosition = displayText.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + y))
    screen.blit(displayText, displayPosition)

def checkWin(board): 
    # a tuple - (if win exists, returns 1 if player1 wins 0 if player2/CPU wins)
    # check rows and cols
    for i in range(boardSize):
        m = 0
        n = 0
        if(board[i][0] != 0):
            winning = True
            while(winning and m < boardSize):
                if(board[i][0] != board[i][m]):
                    winning= False
                m += 1
            if(winning):
                return (1, board[i][0] == 1)
        if(board[0][i] != 0):
            winning = True
            while(winning and n < boardSize):
                if(board[0][i] != board[n][i]):
                    winning = False
                n += 1
            if(winning):
                return (1,board[0][i]==1)

    # check diagonals
    if(board[0][0] != 0):
        i = 0
        winning = True
        while(winning and i < boardSize):
            if(board[0][0] != board[i][i]):
                winning = False
            i += 1
        if(winning):
            return (1, board[0][0] == 1)
    if(board[boardSize-1][0] != 0):
        i = 0
        winning = True
        while(winning and i < boardSize):
            if(board[0][boardSize-1] != board[i][boardSize-1-i]):
                winning = False
            i += 1
        if(winning):
            return (1, board[0][boardSize-1] == 1)

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
            row = y // (SCREEN_HEIGHT // boardSize)
            col = x // (SCREEN_WIDTH // boardSize)
            
            # check that the spot in the board is empty
            if(board[row][col] == 0):
                print(str(row) + " " + str(col))

                # X
                drawX(row, col)
                board[row][col] = 1
                turn += 1
                
                # O
                botRow, botCol = botMove(board, maxMoves-turn)
                if(botRow != -1):
                    drawO(botRow, botCol)
                    board[botRow][botCol] = 2
                    turn += 1
                
                # print board state to terminal
                # displayBoard()

                # check to see if the game has been won using checkWin function
                gameWon, player = checkWin(board)
                if(gameWon):
                    if(player == 0):
                        score_o += 1
                        # draw rectangle for end screen, tint colour of the winning player
                        drawEndRectangle((240,180,180))
                    else:
                        score_x += 1
                        drawEndRectangle((180,180,240))
                    # display game over message
                    displayMessage("Game over. " + ("X" if player else "O") + " won!", -20)
                    print(("X" if player else "O") + " won!")
                
                # board is full, game is drawn
                elif(turn == maxMoves):
                    drawEndRectangle(GREY)
                    font = pygame.font.SysFont("Source Code Pro", 40)
                    displayMessage("Game over. It's a draw!", -20)
                    print("DRAW!")
                
                # game ends
                if(gameWon or turn == maxMoves):
                    # print end screen text
                    displayMessage("Click again to reset.", 20)
                    
                    # wait for player to click to reset
                    print(f"Scores\n * O: {score_o}\n * X: {score_x}")
                    print("Waiting for reset...")
                    gameEnd = True

        pygame.display.update()
