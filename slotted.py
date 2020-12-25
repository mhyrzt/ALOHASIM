from node import Node
from consts import *
class Slotted(Node):
    def __init__(self, name, screen, server):
        super().__init__(name, screen, ITS_NODE)
        self.server   = server
        self.request  = None
        self.response = None

    def getFrame(self, frame):
        self.reponse = frame
    
    def emptyBuffer(self):
        if self.request is None or self.reponse is None:
            return
        
        SUCSESSFUL = self.request.message == self.reponse.message
        
        if SUCSESSFUL:
            self.resetDefault()
        else:
            self.waitfor = getRandomTime()
        
        return SUCSESSFUL
    
    def resetDefault(self):
        self.request  = None
        self.response = None
        self.waitfor  = None
    
    def sendFrame(self):
        if not self.request is None:
            server.getFrame(self.request)
        
    def addFrame(self, frame):
        if self.request is None:
            self.request = frame
            log("new Frame ready to sent", self)
        else:
            log("cant add new frame", self) 