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

        if event.type == pygame.QUIT:
            Run = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            Dragging = True
            StartPos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            Dragging = False
            EndingPos = pygame.mouse.get_pos()
            dx = EndingPos[0] - StartPos[0]
            dy = EndingPos[1] - StartPos[1]
            Angle = math.degrees(math.atan2(dy, dx))
            ball.angle = Angle
            ball.speed = min(math.sqrt(dx ** 2 + dy ** 2) * 0.1, 10)
    if Dragging: 
        EndingPos 
    pygame.display.update()
pygame.quit()