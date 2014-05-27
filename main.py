import pygame, sys, darking, harvest_screen, physics, random, darkSerial
from harvest_screen import *

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
thr = darking.movThread

def main():
	frameCount = 0
	clock = pygame.time.Clock()
	addPts([500,100],25,40)
	cntrlpt = darking.controlPoint(495,150,particles)
	newpt = darking.controlPoint(395,150,particles)	
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
	#cPoint = darking.blobPoint(200,230)
	#cPoint.setControl(particles)
	#particles.append(cPoint)
	mvspd = 4
	pygame.key.set_repeat()
	pygame.key.set_repeat(1,5)
	x = darking.movThread(cntrlpt)
	x.start()
	while 1:
		frameCount += 1 
		#print frameCount
		#if frameCount%10 == 0: addPts([random.randint(0,600),20],1,1)
		clock.tick(60)
		for event in pygame.event.get():
            		if event.type == pygame.QUIT: 
				sys.exit()
            				
			if pygame.key.get_pressed()[pygame.K_f]:
					currentQ = currentP
					currentP += 1
					
					if currentP >= len(controlPoints): currentP = 0
            		if pygame.key.get_pressed()[pygame.K_RIGHT]:
					controlPoints[currentP].position.x+= mvspd
					#physics.applyForce(controlPoints[currentP],physics.vector2d(5,0))
            		if pygame.key.get_pressed()[pygame.K_LEFT]:
                                        controlPoints[currentP].position.x-=mvspd
					#physics.applyForce(controlPoints[currentP],physics.vector2d(-5,0))
            		if pygame.key.get_pressed()[pygame.K_UP]:
					controlPoints[currentP].position.y-=mvspd
					#physics.applyForce(controlPoints[currentP],physics.vector2d(0,-5))
            		if pygame.key.get_pressed()[pygame.K_DOWN]:
					controlPoints[currentP].position.y+=mvspd
					#physics.applyForce(controlPoints[currentP],physics.vector2d(0,5))
			if pygame.key.get_pressed()[pygame.K_w]:
					controlPoints[currentQ].position.y-= mvspd
			if pygame.key.get_pressed()[pygame.K_a]:
					controlPoints[currentQ].position.x-= mvspd	
			if pygame.key.get_pressed()[pygame.K_s]:
					controlPoints[currentQ].position.y+= mvspd
			if pygame.key.get_pressed()[pygame.K_d]:
					controlPoints[currentQ].position.x+= mvspd	

		#screen.fill(white)
		screen.blit(background, backgroundRect)
		#for i in range(len(particles)-1):
		#	forceTest(frameCount,[3],particles[i],physics.vector2d(-5,0))
		#	forceTest(frameCount,[10],particles[i],physics.vector2d(0,-7))
		#	forceTest(frameCount,[15],particles[i],physics.vector2d(10,-8))
		
		for i in range(len(particles)):	
		#	if particles[i].position.y >= 490 or particles[i].position.y <= 10:
		#		particles[i].velocity.y *=-.5
		#	if particles[i].position.x >= 715 or particles[i].position.x <= 10:
		#		particles[i].velocity.x *=-.5	
				#particles[i].velocity.reverse(y)
				#forceTest(0,[0],particles[i],physics.vector2d(0,-9)) 
			particles[i].bump(nonControl)
			particles[i].update()
			particles[i].blit()
		pygame.display.flip()	
			

main()
