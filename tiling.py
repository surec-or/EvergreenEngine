import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)
import pygame
import random
import pickle
import time

images = ["toletole.jpg", "toletole1.jpg", "toletole2.jpg", "toletole3.jpg", "klusha.jpg"]

orientations = [0, 90, 180, 270]

screen = pygame.display.set_mode([64,64])

screensize = [1280, 720] # list(input("Enter your desired window size using the format, including brackets [Horizontal, Verticle]:"


class tilemap:

    def __init__(self, x, y, type, tilesize, tileset=None):

        self.tileset = tileset

        self.tilesize = tilesize

        self.list = []

        if type == "tileset":

            for funcX in range(x):

                self.list.append([])

                for funcY in range(y):

                    self.list[funcX].append(tile(tilesize*funcX, tilesize*funcY, 0, "baseMaterial", 0, False, tilesize=self.tilesize, slope=(0,0), tilesetTexture=(0,0,tilesize)))

        elif type == "texture":

            for funcX in range(x):

                self.list.append([])

                for funcY in range(y):

                    self.list[funcX].append(tile(tilesize*funcX, tilesize*funcY, 0, "baseMaterial", 0, False, tilesize=self.tilesize, slope=(0,0),texture=random.choice(images)))

    def draw(self):

        start = time.time()

        blitList = []

        for i, row in enumerate(self.list):
                
                for j, element in enumerate(row):
                            
                    blitList.append((pygame.transform.rotate(textureCache[element.texture], random.choice(orientations)), [element.x, element.y]))


        screen.blits(blitList)

        pygame.display.update()

        end = time.time()

        print(end-start)

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

                if texture in textureCache:

                    return
                
                else:

                    textureCache[texture] = pygame.transform.scale(pygame.image.load(texture).convert(), (self.tilesize, self.tilesize))

                self.outdoorsTexture = outdoorsTexture

            elif tilesetTexture is not None:

                self.tilesetTexture = tilesetTexture

                self.tilesetOutdoorsTexture = tilesetOutdoorsTexture

            else:

                quit("RPEngine Tile Engine Error: you must define either a texture or tileset texture coordinate tuple! Define a texture with a string containing a filename, and a tileset texture using a tuple (x on image, y on image, scale)")

'''
def createTileset(x, y, tilesize, name, margin=None): TILEMAP

    for funcX in range(x):

        tileset.append([])

        for funcY in range(y):

            tileset[funcX].append((tilesize*funcX, tilesize*funcY, 0, 0,  "toletole.jpg", "baseMaterial", False, False))

def drawTile(x, y, z=None, texture=None, material=None, collide=None, room=None, slopelow=None, slopehigh=None, indoors=None):

def tileProperty(x, y, property, value):
'''

file = 'toletole.jpg'
image = pygame.image.load(file)
rect = image.get_rect()
print(image)

pygame.init()

pygame.display.set_mode(screensize)

clock = pygame.time.Clock()

run = True

textureCache = {}

while run:
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False          

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_r:

                myMap = tilemap(100, 100, "texture", 64)

                myMap.draw()
            
            if event.key == pygame.K_e:

                print(myMap.list[0][0].texture)

        if event.type == pygame.MOUSEBUTTONDOWN:

            checkRect = pygame.Rect(pygame.mouse.get_pos()[0]-25, pygame.mouse.get_pos()[1]-25, 50, 50)
            
            print(checkRect.topleft)

            pygame.draw.rect(screen, (255,255,255), checkRect)

            pygame.display.update()
