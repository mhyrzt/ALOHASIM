from frame   import *
from node    import *
from slotted import *
from server  import *
from pure    import *

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)   
    pygame.display.set_caption("ALOHA SIMULATION")
    
    server = Server(screen)
    server.setPos(SCREEN_X // 2, SCREEN_Y // 2)

    nodes  = []     
    for i in NODE_NUMBERS:
        name = "ISLAND " + str(i + 1)
        node = None
        if SIMULATION == PURE:
            node = Pure(name, screen, server)
        else:
            node = Slotted(name, screen, server)
        
        node.setPos(*getNewPos(i))
        nodes += [node]
    
    while True:
        screen.fill(COLOR_BLACK)

        drawNodes(nodes, server)

        pygame.display.update()
        pygame.time.delay(DELAY_TIME)