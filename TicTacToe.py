import pygame, sys, random

pygame.init()

screenWidth = 600
screenHeight = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (180, 180, 180)
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(WHITE)

# keeps track of the tic-tac-toe board
board = [[0]*3 for i in range(3)]

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
    
# draws a 3x3 grid onto the screen
def setup(lineColor, lineWidth):
    pygame.draw.line(screen, lineColor, (screenWidth/3, 0), (screenWidth/3, screenHeight), lineWidth)
    pygame.draw.line(screen, lineColor, (screenWidth/3*2, 0), (screenWidth/3*2, screenHeight), lineWidth)
    pygame.draw.line(screen, lineColor, (0, screenHeight/3), (screenWidth, screenHeight/3), lineWidth)
    pygame.draw.line(screen, lineColor, (0, screenHeight/3*2), (screenWidth, screenHeight/3*2), lineWidth)
    renderScore()

def resetBoard():
    global board, turn
    board = [[0]*3 for i in range(3)]
    turn = 0
    screen.fill(WHITE)
    setup(BLACK, 5);

def displayBoard():
    #for z in range(3*2+1):
    #    print("_", end="")
    #print()
    for y in range(3):
        print("|", end="")
        for x in range(3):
            cur = board[x][y]
            print("_" if cur == 0 else ("X" if cur == 1 else "O"), end = "|")
        print()

# draws X
def drawX(row, col):
    linePos1 = ((screenWidth/3*col+50,screenWidth/3*row+50), (screenWidth/3*col+150,screenWidth/3*row+150))
    linePos2 = ((screenWidth/3*col+150,screenWidth/3*row+50), (screenWidth/3*col+50,screenWidth/3*row+150))
    pygame.draw.line(screen, BLUE, linePos1[0], linePos1[1], 30)
    pygame.draw.line(screen, BLUE, linePos2[0], linePos2[1], 30)

# draws O
def drawO(row, col):
    pygame.draw.circle(screen, RED, (screenWidth/3*col + 100, screenWidth/3*row + 100), 70)
    pygame.draw.circle(screen, WHITE, (screenWidth/3*col + 100, screenWidth/3*row + 100), 45)

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
    displayPosition = displayText.get_rect(center = (screenWidth/2, screenHeight/2 + y))
    screen.blit(displayText, displayPosition)

def checkWin(board):
    # check for diagonal wins
    if(board[1][1] != 0 and ((board[0][0] == board[1][1] and board[1][1] == board[2][2])
                        or (board[2][0] == board[1][1] and board[1][1] == board[0][2]))):
        return True
    # check for horizontal wins
    for x in range(3):
        if(board[x][1] != 0 and (board[x][0] == board[x][1] and board[x][1] == board[x][2])):
            return True
    # check for vertical wins
    for y in range(3):
        if(board[1][y] != 0 and (board[0][y] == board[1][y] and board[1][y] == board[2][y])):
            return True
    return False

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
            row = y // (screenHeight // 3)
            col = x // (screenWidth // 3)
            
            # check that the spot in the board is empty
            if(board[col][row] == 0):
                print(str(row) + " " + str(col))
                # draw either an x or an o on the screen depending on whose turn it is
                if(turn % 2): # X
                    drawX(row, col)
                    board[col][row] = 1
                else:         # O
                    drawO(row, col)
                    board[col][row] = 2

                # increment turn, redraw board
                turn += 1
                displayBoard()

                # check to see if the game has been won using checkWin function
                gameWon = checkWin(board)
                if(gameWon):
                    if(turn % 2):
                        score_o += 1
                        # draw rectangle for end screen, tint colour of the winning player
                        drawEndRectangle((240,180,180))
                    else:
                        score_x += 1
                        drawEndRectangle((180,180,240))
                    # display game over message
                    displayMessage("Game over. " + ("O" if turn % 2 else "X") + " won!", -20)
                    print(("O" if turn % 2 else "X") + " won!")
                
                # board is full, game is drawn
                elif(turn == 9):
                    drawEndRectangle(GREY)
                    font = pygame.font.SysFont("Source Code Pro", 40)
                    displayMessage("Game over. It's a draw!", -20)
                    print("DRAW!")
                
                # game ends
                if(gameWon or turn == 9):
                    # print end screen text
                    displayMessage("Click again to reset.", 20)
                    
                    # wait for player to click to reset
                    print(f"Scores\n * O: {score_o}\n * X: {score_x}")
                    print("Waiting for reset...")
                    gameEnd = True
        pygame.display.update()
