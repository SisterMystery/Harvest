import pygame, math, time

# This is all the stuff for setting up the screen that the game is played on.
# adjusting the size variable will alter the screen dimensions 

#size = width, height = 744,500

white = (255,255,255)
pygame.init()
pygame.font.init()
speed = [1,1]
background  = pygame.image.load("images/trees.bmp")

backgroundRect = background.get_rect()
size = (width, height) =background.get_size() 
screen = pygame.display.set_mode(size)

