from consts import *
from random import shuffle
class Frame:
    def __init__(self, sender, message):
        self.time_at = getTime()
        self.sender  = sender
        self.message = message
    
    def __str__(self):
        string = "[{TIME}]:{SENDER}\u2192{MESSAGE}".format(
            TIME    = self.time_at, 
            SENDER  = self.sender.getName(),
            MESSAGE = self.message
            )
    
    def getFrameTime(self):
        return self.time_at
    
    def getSender(self):
        return self.sender

    @staticmethod
    def collision(*args):
        string = ""
        for a in args:
            string += a.message
        string = list(string)
        string = shuffle(string)
        string = ''.join(string)
        return string