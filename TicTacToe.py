import pygame, sys, random

pygame.init()

screenWidth = 600
screenHeight = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(WHITE)

# keeps track of the tic-tac-toe board
board = [[0]*3 for i in range(3)]

# keep track of how many turns have elapsed
turn = 0

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

setup(BLACK, 5);

def resetBoard():
    global board,turn
    board = [[0]*3 for i in range(3)]
    turn = 0
    screen.fill(WHITE)
    setup(BLACK, 5);

def displayBoard():
    for y in range(3):
        for x in range(3):
            cur = board[x][y]
            print("_" if cur == 0 else ("X" if cur == 1 else "O"), end = ",")
        print()

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

while(True):
    for ev in pygame.event.get():
        if(ev.type == pygame.QUIT):
            sys.exit()

        #if the user clicks on the screen
        if(ev.type == pygame.MOUSEBUTTONDOWN):
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
                    pygame.draw.line(screen, BLUE, (screenWidth/3*col+50,screenWidth/3*row+50), (screenWidth/3*col+150,screenWidth/3*row+150), 30)
                    pygame.draw.line(screen, BLUE, (screenWidth/3*col+150,screenWidth/3*row+50), (screenWidth/3*col+50,screenWidth/3*row+150), 30)
                    board[col][row] = 1
                else:         # O
                    pygame.draw.circle(screen, RED, (screenWidth/3*col + 100, screenWidth/3*row + 100), 70)
                    pygame.draw.circle(screen, WHITE, (screenWidth/3*col + 100, screenWidth/3*row + 100), 45)
                    board[col][row] = 2

                # increment turn, redraw board
                turn += 1
                displayBoard()
                pygame.display.update()

                # check to see if the game has been won using checkWin function
                game_won = checkWin(board)
                if(game_won):
                    if(turn % 2):
                        score_o += 1
                    else:
                        score_x += 1
                    print(("O" if turn % 2 else "X") + " won!")
                elif(turn == 9):
                    print("DRAW!")
                if(game_won == 1 or turn == 9):
                    # TODO: wait for reset button to be pressed
                    print(f"Scores\n * O: {score_o}\n * X: {score_x}")
                    print("Reseting board in three seconds...")
                    pygame.time.wait(3000)
                    resetBoard()

        pygame.display.update()

