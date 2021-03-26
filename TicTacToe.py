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

#keeps track of the tic-tac-toe board
board = [[0]*3 for i in range(3)]

#keep track of how many turns have elapsed
turn = 0

#draws a 3x3 grid onto the screen
def setup(lineColor, lineWidth):
    pygame.draw.line(screen, lineColor, (screenWidth/3, 0), (screenWidth/3, screenHeight), lineWidth)
    pygame.draw.line(screen, lineColor, (screenWidth/3*2, 0), (screenWidth/3*2, screenHeight), lineWidth)
    pygame.draw.line(screen, lineColor, (0, screenHeight/3), (screenWidth, screenHeight/3), lineWidth)
    pygame.draw.line(screen, lineColor, (0, screenHeight/3*2), (screenWidth, screenHeight/3*2), lineWidth)

setup(BLACK, 5);

while(True):
    for ev in pygame.event.get():
        if(ev.type == pygame.QUIT):
            sys.exit()

        #if the user clicks on the screen
        if(ev.type == pygame.MOUSEBUTTONDOWN):
            x = ev.pos[0]
            y = ev.pos[1]
            #calculate where in the 3x3 grid the user clicked
            row = y // (screenHeight//3)
            col = x // (screenWidth//3)
            #check that that spot in the board is empty
            if(board[col][row] == 0):
                print(str(row) + " " + str(col))
                #draw either an x or an o on the screen depending on whose turn it is
                #red and blue right now because i'm lazy
                if(turn % 2):
                    pygame.draw.circle(screen, RED, (screenWidth/3*col + 100, screenWidth/3*row + 100), 20)
                    board[col][row] = 1
                else:
                    pygame.draw.circle(screen, BLUE, (screenWidth/3*col + 100, screenWidth/3*row + 100), 20)
                    board[col][row] = 2
                turn += 1
        
        pygame.display.update()
