import pygame, sys, darking, harvest_screen, physics, random, darkSerial
from harvest_screen import *

flushCount = 1000000
particles = []
controlPoints = []
nonControl = []
frameCount = 0
def addPts(origin,x,y):
	for x in range(x):
		for y in range(y):
			pt = darking.blobPoint(origin[0]-5*x,origin[1]+5*y)
			nonControl.append(pt)
			particles.append(pt)

def main():
	frameCount = 0
	clock = pygame.time.Clock()
	addPts([500,100],25,40)
	cntrlpt = darking.controlPoint(495,150,particles)
	newpt = darking.controlPoint(475,150,particles)	
	particles.append(cntrlpt)
	particles.append(newpt)	
	cntrlpt.parts = particles
	newpt.parts = particles
	controlPoints.append(cntrlpt)
	controlPoints.append(newpt)
	cntrlpt.controls.append(newpt)
	newpt.controls.append(cntrlpt)
	
	currentP = 0
	currentQ = 1
	mvspd = 4
#	x = darking.movThread(cntrlpt)
#	x.start()
	while 1:
		frameCount += 1 
		#print frameCount
		#if frameCount%10 == 0: addPts([random.randint(0,600),20],1,1)
		clock.tick(200)
		for event in pygame.event.get():
            		if event.type == pygame.QUIT: 
				sys.exit()
            				
		screen.blit(background, backgroundRect)
		movlist = darkSerial.getInputList(darkSerial.DarkSerial)
		cList = movlist[:]
		for i in range(len(cList)):
			if i > 3:
				cList[i] = 0

		nList = movlist[:]
		for i in range(len(nList)):
                        if i < 2:
                                nList[i] = 0
		newpt.leash(cntrlpt)
		cntrlpt.update()
		newpt.update()
		cntrlpt.accelerate(cList)
		newpt.accelerate(nList)
		
		for i in range(len(nonControl)):	
			nonControl[i].bump(nonControl)
			nonControl[i].update()
			nonControl[i].accelerate()
			nonControl[i].blit()

		if frameCount % flushCount == 0: darkSerial.DarkSerial.flushInput() 
		pygame.display.flip()	
			

main()
