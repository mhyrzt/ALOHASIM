from node import Node
from consts import *

class Pure(Node):
    def __init__(self, name, screen, server):
        super().__init__(name, screen, ITS_NODE)
        self.server  = server
        self.request = None
        self.reponse = None
        self.buffer  = []
        self.attempt = 1
   
    def getFrame(self, frame):
        self.reponse = frame
        self.emptyBuffer()
    
    def emptyBuffer(self):
        if self.canProcess():
            return
        
        SUCSESSFUL = self.request.message == self.reponse.message
        
        if SUCSESSFUL:
            log("Frame delivered, %d attempts" % self.attempt, self, OKGREEN)
            self.resetDefault()
        else:
            
            newTime = self.request.getFrameTime() + getRandomTime() + FRAME_TIME
            self.request.setTime(newTime)
            if self.attempt % PRINT_ATTEMPT == 0:
                log("Frame not delivered", self, FAIL)
            self.attempt += 1

    def resetDefault(self):
        self.request  = None
        self.response = None
        self.attempt  = 1

    def sendFrame(self):
        if not self.request is None:
            self.server.addRequest(self.request)
        else:
            try:
                self.request = self.buffer.pop(0)
                log("new Frame ready to sent from buffer", self, OKCYAN)
                self.sendFrame()
            except:
                pass
                

    def addFrame(self, frame):
        if self.request is None:
            self.request = frame
            log("new Frame ready to sent", self, OKCYAN)
        else:
            self.buffer.append(frame)
            log("cant add new frame, buffered in memory", self, WARNING)

    def canProcess(self):
        return self.request is None or self.reponse is None