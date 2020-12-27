from consts import *

class Log:
    def __init__(self, msg, node, frame, color = None):
        self.node    = node
        self.message = msg
        self.color   = color
        self.frame   = frame
        self.timeat  = getTime()
        self.simtime = None
    
    def setTime(self, t):
        self.simtime = t

    def show(self):
        log(self.message, self.node, self.color)