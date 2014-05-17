import pygame, sys, darking, harvest_screen, physics
from harvest_screen import *



## better fix all this to work with  the new objects
def main():
	frameCount = 0
	clock = pygame.time.Clock()
	particles = []
	controlPoints = []
	nonControl = []
	for x in range(10):
		for y in range(20):
			pt = darking.blobPoint(525-5*x,100+5*y)
			nonControl.append(pt)
			particles.append(pt)
	cntrlpt = darking.controlPoint(495,150,particles)
	newpt = darking.controlPoint(395,150,particles)	
	particles.append(cntrlpt)
	particles.append(newpt)	
	controlPoints.append(cntrlpt)
	controlPoints.append(newpt)
	cntrlpt.controls.append(newpt)
	newpt.controls.append(cntrlpt)
	
	currentP = 0
	currentQ = 1
	#cPoint = darking.blobPoint(200,230)
	#cPoint.setControl(particles)
	#particles.append(cPoint)
	mvspd = 2
	pygame.key.set_repeat()
	pygame.key.set_repeat(1,5)
	while 1:
		#frameCount += 1 
		#print frameCount
		clock.tick(60)
		for event in pygame.event.get():
            		if event.type == pygame.QUIT: sys.exit()
            				
			if pygame.key.get_pressed()[pygame.K_f]:
					currentQ = currentP
					currentP += 1
					
					if currentP >= len(controlPoints): currentP = 0
            		if pygame.key.get_pressed()[pygame.K_RIGHT]:
					controlPoints[currentP].position.x+= mvspd
					#physics.applyForce(i,physics.vector2d(20,0))	
            		if pygame.key.get_pressed()[pygame.K_LEFT]:
                                        controlPoints[currentP].position.x-=mvspd
					#physics.applyForce(i,physics.vector2d(-20,0))
            		if pygame.key.get_pressed()[pygame.K_UP]:
					controlPoints[currentP].position.y-=mvspd
					#physics.applyForce(i,physics.vector2d(0,-20))
            		if pygame.key.get_pressed()[pygame.K_DOWN]:
					controlPoints[currentP].position.y+=mvspd
					#physics.applyForce(i,physics.vector2d(0,20))
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
