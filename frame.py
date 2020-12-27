from consts import *
from random import shuffle
class Frame:
    def __init__(self, sender, message, reciver = None, t = getTime()):
        self.time_at = t
        self.sender  = sender
        self.reciver = reciver
        self.message = message
    
    def __str__(self):
        string = "{TIME} -- {SENDER} = {MESSAGE}".format(
            TIME    = self.time_at, 
            SENDER  = self.sender.getName(),
            MESSAGE = self.message
            )
        return OKBLUE + string + ENDC
    
    def getFrameTime(self):
        return self.time_at
    
    def getSender(self):
        return self.sender

    def setTime(self, t):
        self.time_at = t
    
    def swapTR(self):
        self.sender, self.reciver = self.reciver, self.sender

    @staticmethod
    def collision(*args):
        string = ""
        for a in args:
            string += a.message
        string = list(string)
        shuffle(string)
        string = ''.join(string)
        return string