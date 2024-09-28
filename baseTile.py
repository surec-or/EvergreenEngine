import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)
import pygame
import random
import pickle
import time

tileTextureCache = {}
globalDrawCount = 0

images = ["toletole.jpg", "toletole1.jpg", "toletole2.jpg", "toletole3.jpg", "klusha.jpg", "wood.jpg"]

orientations = [0, 90, 180, 270]

screen = pygame.display.set_mode([64,64])

class tilemap:

    def __init__(self, sizex, sizey, type, tilesize, texture=None, tileset=None):

        self.x, self.y = 0, 0

        self.sizex = sizex
        self.sizey = sizey

        self.tileset = tileset

        self.tilesize = tilesize

        self.list = []

        self.chunkmode = False

        if type == "tileset":

            for funcX in range(sizex):

                self.list.append([])

                for funcY in range(sizey):

                    self.list[funcX].append(tile(tilesize*funcX, tilesize*funcY, 0, "baseMaterial", 0, False, tilesize=self.tilesize, slope=(0,0), tilesetTexture=(0,0,tilesize)))

        elif type == "texture":

            for funcX in range(sizex):

                self.list.append([])

                for funcY in range(sizey):

                    self.list[funcX].append(tile(tilesize*funcX, tilesize*funcY, 0, "baseMaterial", 0, False, tilesize=self.tilesize, slope=(0,0),texture=texture))

    def tileAtPoint(self, coordinate= (tuple)):

        return self.list[coordinate[0]//self.tilesize][coordinate[1]//self.tilesize]

    def draw(self, x, y):

        global globalDrawCount

        globalDrawCount += 1

        start = time.perf_counter_ns()

        blitList = []

        for i, row in enumerate(self.list):
                
                for j, element in enumerate(row):

                    blitList.append((tileTextureCache[element.texture], [element.x+x, element.y+y]))

        screen.blits(blitList)

        end = time.perf_counter_ns()

        # print(f"Completed tilemap.draw operation #{globalDrawCount} of this session in {(end-start)/1000000}ms")
    
    def newChunks(self, x, y, chunksizex, chunksizey):

        chunkList = []

        for funcX in range(chunksizex):

            for funcY in range(chunksizey):

                chunkList[funcX].append(chunk(x, y, chunksizex, chunksizey, self.tilesize))



class chunk(tilemap):

    def __init__(self, x, y, sizex, sizey, tilesize):

        self.x = x
        self.y = y
        self.sizex = sizex
        self.sizey = sizey
        self.tilesize = tilesize

class tile(tilemap):

        def __init__(self, x, y, z, material, room: int, indoors: bool, tilesize, slope=(0,0), texture=None, outdoorsTexture=None, tilesetTexture=None, tilesetOutdoorsTexture=None):

            self.tilesize = tilesize
            self.x = x      
            self.y = y
            self.z = z
            self.material = material
            self.room = room
            self.indoors = indoors
            self.slope = slope

            if texture is not None:

                self.texture = texture

                if texture in tileTextureCache:

                    return
                
                else:

                    tileTextureCache[texture] = pygame.transform.scale(pygame.image.load(texture).convert(), (self.tilesize, self.tilesize))

                    print(f"Texture file '{texture}' was unloaded, loaded pygame.image object to textureCache")

                self.outdoorsTexture = outdoorsTexture

            elif tilesetTexture is not None:

                self.tilesetTexture = tilesetTexture

                self.tilesetOutdoorsTexture = tilesetOutdoorsTexture

            else:

                quit("Py2DPG baseTile Error: You must define either a texture or tileset texture coordinate tuple! Define a texture with a string containing a filename, and a tileset texture using a tuple (x on image, y on image, scale)")

'''
pygame.init()

pygame.display.set_mode(screensize)

clock = pygame.time.Clock()

run = True

textureCache = {}

tickSpeed = 25 # tickrate (in milliseconds)

TICKEVENT = pygame.USEREVENT+1

pygame.time.set_timer(TICKEVENT, tickSpeed)


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        keys = pygame.key.get_pressed()

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_r:

                myMap = tilemap(25, 25, "texture", 64, "toletole.jpg")

                originx, originy = 0,0

                myMap.draw()

        if event.type == TICKEVENT: # activates once per tick

            # if physicsActive:

                
            # movement

            if keys[pygame.K_LEFT]:
                        
                originx += 3

                myMap.draw()

            elif keys[pygame.K_RIGHT]:
                        
                originx -= 3

                myMap.draw()

            if keys[pygame.K_UP]:
                        
                originy += 3

                myMap.draw()

            elif keys[pygame.K_DOWN]:
                        
                originy -= 3

                myMap.draw()
'''