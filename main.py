from frame   import *
from node    import *
from slotted import *
from server  import *
from pure    import *
import os

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)   
    pygame.display.set_caption("ALOHA SIMULATION")
    
    srvr = Server(screen)
    srvr.setPos(SCREEN_X // 2, SCREEN_Y // 2)

    nodes  = []     
    for i in NODE_NUMBERS:
        name = "ISLAND " + str(i + 1)
        node = None
        if SIMULATION == PURE:
            node = Pure(name, screen, srvr)
        else:
            node = Slotted(name, screen, srvr)
        
        node.setPos(*getNewPos(i))
        nodes.append(node)
        srvr.addSlave(node)
    
    for f in getFrames():
        frame = Frame(nodes[f[0]], f[1], f[2]) 
        nodes[f[0]].addFrame(frame)    
    
    while True:
        eventsHandler()
        screen.fill(COLOR_BLACK)
        
        drawNodes(nodes, srvr)
        processNodes(nodes)
        srvr.processRequests()

        pygame.display.update()
        pygame.time.delay(DELAY_TIME)