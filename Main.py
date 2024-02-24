import pygame 
import BallFile 
import math

pygame.init()
clock = pygame.time.Clock()

ScreenWidth = 1200
ScreenHeight = 768

#Images
BackgroundImage = pygame.image.load("C:\\Users\\Arda\\Documents\\GolfGameWithPython\\Images\\BackgroundImage.jpg")
BoxImage = pygame.image.load("C:\\Users\\Arda\\Documents\\GolfGameWithPython\\Images\\Box.png")
RectBoxImage = pygame.image.load("C:\\Users\\Arda\\Documents\\GolfGameWithPython\\Images\\RectBox.png")
Flag = pygame.image.load("C:\\Users\\Arda\\Documents\\GolfGameWithPython\\Images\\Flag.png")
Ball = pygame.image.load("C:\\Users\\Arda\\Documents\\GolfGameWithPython\\Images\\Ball.png")



Screen = pygame.display.set_mode((ScreenWidth,ScreenHeight))
pygame.display.set_caption('Preview')

#defining fonts
Font = pygame.font.SysFont("arialblack",32)


Run = True 
PauseTheGame = False
ball = BallFile.Ball(15,600)

Dragging = False
StartPos = None


while Run: 
    Screen.blit(BackgroundImage,[0,0])
    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                PauseTheGame = True 
                ball.deneme()

        if event.type == pygame.QUIT:
            Run = False


    pygame.display.update()
pygame.quit()