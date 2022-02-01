import pygame

WIDTH, HEIGHT = 800, 800

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Analog Clock")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

EPS = 60

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                run = False

        screen.fill(BLACK)
        pygame.display.update()
        clock.tick(EPS)
    pygame.quit()


main()