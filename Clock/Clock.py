import pygame

WIDTH, HEIGHT = 800, 800

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Analog Clock")
clock = pygame.time.Clock()