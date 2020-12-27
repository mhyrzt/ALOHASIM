from consts import *
from node import Node 
from frame import Frame
from log import Log
class Server(Node):
    def __init__(self, screen):
        super().__init__("SERVER", screen, ITS_SERVER)
        self.slaves   = []
        self.requests = [] # Frames
        self.logs     = []
        self.simtime  = getTime()
        
    def addSlave(self, slave):
        self.slaves += [slave]
    
    def addRequest(self, frame):
        self.requests += [frame]
    
    def checkCollision(self, frame):
        start_time = frame.getFrameTime()
        end_time   = start_time + FRAME_TIME
        collisions = []
        
        for f in self.requests:
            if f == frame:
                continue
            if end_time > f.getFrameTime():
                collisions += [f]
        
        if collisions == []:
            new_frame = Frame(self, frame.message, frame.sender)
            return new_frame, False, [frame]
        
        colission_frame = Frame(self, Frame.collision(*collisions), collisions)
        return colission_frame, True, collisions
    
    def processRequests(self):
        processed = []
        
        for frame in self.requests:
            if frame in processed:
                continue
            
            response, error, frames = self.checkCollision(frame)
            for f in frames:
                processed += [f]
                sender     = f.getSender()
                sender.getFrame(response)
        
        for frame in processed:
            try:
                self.requests.remove(frame)
            except:
                pass
    
    def addLog(self, log):
        log.setTime(self.simtime)
        self.logs += [log]
    
    def getLog(self):
        return self.logs

    def showLogs(self):
        pass