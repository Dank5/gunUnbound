import pygame

def main():
    pygame.init()

    white = (255,255,255)
    black = (0,0,0)

    
    pygame.display.set_caption("hello")
    screen = pygame.display.set_mode((800,600))

    clock = pygame.time.Clock()

    def mobile(screen, colour, x, y, width, height):
        pygame.draw.rect(screen, colour, [x,y,width,height])
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            screen.fill(white)
            mobile(screen, black, 400, 300, 30, 30)
            pygame.display.update()
            clock.tick(60)
            
            
    pygame.quit()
    quit()


if __name__=="__main__":
    main()
