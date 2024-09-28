import pygame
import baseTile
import time
import math
import vectorPx

screensize = [1280, 720] # list(input("Enter your desired window size using the format, including brackets [Horizontal, Verticle]:"

pygame.init()

screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Py2DPG Game")

clock = pygame.time.Clock()

run = True

tickSpeed = 25 # tickrate (in milliseconds)

TICKEVENT = pygame.USEREVENT+1

pygame.time.set_timer(TICKEVENT, tickSpeed)

hwyGoth = pygame.font.Font("HWYGOTH.TTF", 16)

originx, originy = 0, 0

camx, camy = 0,0

timerStart, timerEnd = 0, 0

movementSpeed = 1

currentMap = None

myMap = baseTile.tilemap(25, 25, "texture", 64, "toletole.jpg")
myMap2 = baseTile.tilemap(25, 25, "texture", 128, "toletole1.jpg")
myMap3 = baseTile.tilemap(10, 10, "texture", 64, "toletole.jpg")
myMap4 = baseTile.tilemap(5, 5, "texture", 128, "toletole1.jpg")

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        keys = pygame.key.get_pressed()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_EQUALS:

                movementSpeed += 1
            
            if event.key == pygame.K_MINUS:

                movementSpeed -= 1
            
            if event.key == pygame.K_1:

                currentMap = myMap
            
            if event.key == pygame.K_2:

                currentMap = myMap2
            
            if event.key == pygame.K_3:

                currentMap = myMap3
            
            if event.key == pygame.K_4:

                currentMap = myMap4


        if event.type == TICKEVENT: # activates once per tick

            screen.fill((0,0,0))

            timerStart = time.perf_counter()

            if currentMap:

                currentMap.draw(originx, originy)

            # if physicsActive:
   
            # movement

            if keys[pygame.K_LEFT]:
                        
                originx += movementSpeed

                currentMap.draw(originx, originy)

            elif keys[pygame.K_RIGHT]:
                        
                originx -= movementSpeed

                currentMap.draw(originx, originy)

            if keys[pygame.K_UP]:
                        
                originy += movementSpeed

                currentMap.draw(originx, originy)

            elif keys[pygame.K_DOWN]:
                        
                originy -= movementSpeed

                currentMap.draw(originx, originy)

            timerEnd = time.perf_counter()

            # annoying piece of shit code because i couldnt make a fucking text engine after 6 hours

            debugTitle = hwyGoth.render(f"Debug", True, (255,255,255), (0,0,0))

            tickRateDebug = hwyGoth.render(f"TPS: {max(0, 25-round((timerEnd-timerStart)*1000))}/{tickSpeed}", True, (255,255,255), (0,0,0))

            movementSpeedDebug = hwyGoth.render(f"movementSpeed: {movementSpeed}", True, (255,255,255), (0,0,0))

            # it works its just annoying as hell to set up in window rendered debugs, fuck python fstrings

            screen.blit(debugTitle, (0, 0))

            screen.blit(tickRateDebug, (0, 16))
            
            screen.blit(movementSpeedDebug, (0, 32))


        pygame.display.update()

             