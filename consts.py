from time import time, localtime
from random import randint
import pygame
from math import sin, cos, pi

#### VARIABLES ####
ITS_NODE   = False
ITS_SERVER = True

MIN_TIME =  200 #ms 
MAX_TIME = 5000 #ms

NODE_NUMBERS = 18 # MAX 36 for best visualization
NODE_NUMBERS = range(NODE_NUMBERS)
NODE_RADIUS  = 35
NODE_WIDTH   = 1

COLOR_NODE   = (255, 0, 0)
COLOR_SERVER = (0, 255, 0)
COLOR_LINK   = [255] * 3
COLOR_BLACK  = [0] * 3

FRAME_TIME = 10 #ms

SCREEN_X    = 960
SCREEN_Y    = 960
SCREEN_SIZE = [SCREEN_X, SCREEN_Y]

FONT_SIZE = 16
FONT_NAME = 'ubuntu'

DELAY_TIME = 100 #ms

PURE    = "PURE"
SLOTTED = "SLOTTED"

SIMULATION    = PURE
PRINT_ATTEMPT = len(NODE_NUMBERS) ** 2

HEADER  = '\033[95m'
OKBLUE  = '\033[94m'
OKCYAN  = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL    = '\033[91m'
ENDC    = '\033[0m'
BOLD    = '\033[1m'

#### FUNCTIONS ####
def getTime(): # Get Time in MS
    return time() * 1000

def getRandomTime():
    global MIN_TIME, MAX_TIME
    return randint(MIN_TIME, MAX_TIME)

def convMs(t):
    return t * 1000

def convTime(t, ms = True):
    t = t / 1000 if ms else t
    t = localtime(t)
    t = "{}:{}:{}".format(t.tm_hour, t.tm_min, t.tm_sec)
    return t

def log(message, node, color = None):
    LOG = "[{TIME}]:{NAME} \u2192 {MESSAGE}".format(
        TIME    = convTime(getTime()),
        NAME    = node.name,
        MESSAGE = message
    )
    if color is None:
        print(LOG)
    else:
        print(color + LOG + ENDC)

def drawNodes(nodes, server):
    for node in nodes:
        server.drawLink(node)
        node.printG()
    server.printG()

def getNewPos(n, r = 400):
    global NODE_NUMBERS
    c = len(NODE_NUMBERS)
    t = 2 * pi * n / c
    x = r * cos(t) + SCREEN_X // 2
    y = r * sin(t) + SCREEN_Y // 2
    return [int(x), int(y)]

def getFrames():
    line = input()
    out  = []
    while not line == "END":
        temp     = line.split()
        temp[0]  = int(temp[0])
        temp[2]  = int(temp[2])
        out     += [temp]
        line     = input()
    return out

def processNodes(nodes):
    for node in nodes:
        node.sendFrame()

def eventsHandler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def processFinished(nodes):
    for node in nodes:
        if node.buffer == [] and node.request is None:
            continue
        else:
            return False
    return True