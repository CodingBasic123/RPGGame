import pygame
import sys
pygame.init()

scW = 800
scH = 600

clock = pygame.time.Clock()
icon = pygame.image.load("icon.png")

window = pygame.display.set_mode((scW, scH))
pygame.display.set_caption("My Game")
pygame.display.set_icon(icon)

playerImgX = pygame.image.load("stickman.png")
playerImg = pygame.transform.scale(playerImgX, (200, 200))
grassImgX = pygame.image.load("grass.png")
grassImg = pygame.transform.scale(grassImgX, (800, 600))

xP = 10
yP = 10
widthP = 50
heightP = 50
velP = 5

xG = 0
yG = 0
widthG = 0
heightG = 0

run = True

def loadPlayer(x, y):
    window.blit(playerImg, (x, y))
def loadGrass(x, y):
    window.blit(grassImg, (x, y))
    

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
            pygame.quit()
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and xP > 5:
        xP -= velP
    if key[pygame.K_RIGHT] and xP < 650 - widthP - velP:
        xP += velP
    if key[pygame.K_UP] and yP > velP:
        yP -= velP
    if key[pygame.K_DOWN] and yP < 550 - heightP - velP:
        yP += velP
    
    window.fill((255,255,255))
    loadGrass(xG, yG)
    loadPlayer(xP, yP)
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
