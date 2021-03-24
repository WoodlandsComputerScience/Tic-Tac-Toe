
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


board = [[0]*3 for i in range(3)]

def setup(lineColor, lineWidth):

	pygame.draw.line(screen, lineColor, (screenWidth/3, 0) , (screenWidth/3, screenHeight) , lineWidth)
	pygame.draw.line(screen, lineColor, (screenWidth/3*2, 0) , (screenWidth/3*2, screenHeight) , lineWidth)
	pygame.draw.line(screen, lineColor, (0, screenHeight/3) , (screenWidth, screenHeight/3) , lineWidth)
	pygame.draw.line(screen, lineColor, (0, screenHeight/3*2) , (screenWidth, screenHeight/3*2) , lineWidth)



setup(BLACK, 8);

while True:
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			sys.exit()

		if ev.type == pygame.MOUSEBUTTONDOWN:
			x = ev.pos[0]
			y = ev.pos[1]
			row = y // (screenHeight//3)
			col = x // (screenWidth//3)
			print(str(row) + " " + str(col))

	pygame.display.update()