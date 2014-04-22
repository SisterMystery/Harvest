import pygame, math, time

# This is all the stuff for setting up the screen that the game is played on.
# adjusting the size variable will alter the screen dimensions 

size = width, height = 744,500
white = (255,255,255)
pygame.init()
pygame.font.init()
speed = [1,1]

screen = pygame.display.set_mode(size)
