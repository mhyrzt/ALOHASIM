from consts import *
import pygame
class Node:
    def __init__(self, name, screen, is_server):
        self.name   = name
        self.pos    = None
        self.color  = COLOR_SERVER if is_server else COLOR_NODE
        self.screen = screen
        
    def printG(self):
        pygame.draw.circle(
            self.screen , 
            self.color  , 
            self.pos    , 
            NODE_RADIUS
            )
        
        pygame.draw.circle(
            self.screen , 
            COLOR_BLACK , 
            self.pos    , 
            NODE_RADIUS - NODE_WIDTH
            )
        
        font = pygame.font.SysFont(None, FONT_SIZE)
        text = font.render(self.name, True, self.color)
        rect = text.get_rect()
        rect.center = self.pos
        self.screen.blit(text, rect)

    def drawLink(self, node):
        pygame.draw.line(
            self.screen,
            COLOR_LINK,
            self.pos,
            node.getPos(),
        )

    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def setPos(self, x, y):
        self.pos = [x, y]
    
    def getPos(self):
        return self.pos 
    
    def getName(self):
        return self.name
    
    def sendFrame(self, frame, reciver):
        reciver.getFrame(frame)

    def getFrame(self, frame):
        pass