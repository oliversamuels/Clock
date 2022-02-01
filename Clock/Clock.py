import pygame
from math import pi, cos, sin
import datetime

WIDTH, HEIGHT = 800, 800

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Analog Clock")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
center = (WIDTH / 2, HEIGHT / 2)
clock_radius = 400

FPS = 60

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                run = False

        screen.fill(BLACK)
        pygame.draw.circle(screen, WHITE, center, clock_radius - 10, 10)
        pygame.draw.circle(screen, WHITE, center, 12)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()


main()