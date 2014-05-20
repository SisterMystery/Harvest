import pygame

pygame.joystick.init()
sticks = pygame.joystick.get_count()
blobstick = pygame.joystick.Joystick(0)

blobstick.init()
 
