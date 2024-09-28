import pygame

pygame.init()

screen = pygame.display.set_mode((64, 64))

class textBox:

    def __init__(self, x, y):
        
        self.x = x
        self.y = y

        self.objectList = [None] # List of textObjects

    def draw(self):

        pixel = 0

        for i, object in enumerate(self.objectList):

            if object:

                if object[2]:

                    screen.blit(pygame.font.Font(object[0][0], object[0][1]).render(object[1][0], object[1][1], object[1][2], object[1][3]), (self.x, self.y-pixel)) # For some fucking reason the function won't accept packed tuples and I'm too lazy to find a pythonic solution. Figures.

                    pixel += object[0][1]

                else:
                    
                    screen.blit(object[0], (self.x, self.y-pixel))

                    pixel += object[1]

    def newTextObject(self, text, font, fontsize, textColor, row, dynamic: bool, bgColor=None, **kwargs):

        index = 0

        if dynamic == True:

            while index < row:

                if index < len(self.objectList):

                    self.objectList.append(None)

                index += 1

            self.objectList[index] = ([(font, fontsize), (text.format(**kwargs), True, textColor, bgColor), True])

        if dynamic == False:

            while index < row:

                if index < len(self.objectList):

                    self.objectList.append(None)

                index += 1

            self.objectList[index] = ([pygame.font.Font(font, fontsize).render(text, True, textColor, bgColor), fontsize, False])