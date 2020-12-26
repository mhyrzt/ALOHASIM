from consts import *
from node import Node 
from frame import Frame

class Server(Node):
    def __init__(self, screen):
        super().__init__("SERVER", screen, ITS_SERVER)
        self.slaves   = []
        self.requests = [] # Frames
    
    def addSlave(self, slave):
        self.slaves += [slave]
    
    def sortRequests(self):
        pass
    
    def addRequest(self, frame):
        self.requests += [frame]
        self.sortRequests()
    
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
            new_frame = Frame(self, frame.message)
            return new_frame, False, [frame]
        
        colission_frame = Frame(self, Frame.collision(*collisions))
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