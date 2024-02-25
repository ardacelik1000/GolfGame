import pygame 
import BallFile 
import math
import sys

pygame.init()
FPS = 60
clock = pygame.time.Clock()

#Screen Measurement
ScreenWidth = 1200
ScreenHeight = 768

#Images
BackgroundImage = pygame.image.load("C:\\Users\\Arda\\Documents\\GolfGameWithPython\\Images\\BackgroundImage.jpg")
BoxImage = pygame.image.load("C:\\Users\\Arda\\Documents\\GolfGameWithPython\\Images\\Box.png")
RectBoxImage = pygame.image.load("C:\\Users\\Arda\\Documents\\GolfGameWithPython\\Images\\RectBox.png")
Flag = pygame.image.load("C:\\Users\\Arda\\Documents\\GolfGameWithPython\\Images\\Flag.png")
Ball = pygame.image.load("C:\\Users\\Arda\\Documents\\GolfGameWithPython\\Images\\Ball.png")


#Game Variables 
WallThickness = 10
Gravity = 0.5
BounceStop = 0.3


#Tab Settings
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
            ball.xSpeed = min(math.sqrt(dx ** 2 + dy ** 2) * 0.1, 10)
            ball.ySpeed = min(math.sqrt(dx ** 2 + dy ** 2) * 0.1, 10)

    if not Dragging: 
        pass
    if Dragging: 
        EndingPos = pygame.mouse.get_pos()
        dx = EndingPos[0] - StartPos[0]
        dy = EndingPos[1] - StartPos[1]
        distance = math.sqrt(dx ** 2 + dy ** 2)
        angle = math.atan2(dy, dx)

        for i in range(0, int(distance), 5):
            x = StartPos[0] + i * math.cos(angle)
            y = StartPos[1] + i * math.sin(angle)

            pygame.draw.circle(Screen, (255,0,0), (int(x), int(y)), 2)
    

    ball.update()
    Screen.blit(Ball,[ball.x,ball.y])

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()