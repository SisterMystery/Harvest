import pygame, darking, harvest_screen, physics
from harvest_screen import *



## better fix all this to work with  the new objects
def main():
	frameCount = 0
	clock = pygame.time.Clock()
	particles = []

	for x in range(25):
		for y in range(30):
			particles.append(darking.blobPoint(525-2*x,100+2*y))
	for i in range(len(particles)):
		if i == 10  or i == 200:#i == 1 or i == 100 or i == 375:
			particles[i].setControl(particles)
	controls = []
	for i in particles:
		if i.controlpt: controls.append(i)
	currentP = 0
	currentQ = 1
	#cPoint = darking.blobPoint(200,230)
	#cPoint.setControl(particles)
	#particles.append(cPoint)
	mvspd = 2
	pygame.key.set_repeat()
	pygame.key.set_repeat(1,5)
	while 1:
		frameCount += 1 
		#print frameCount
		clock.tick(120)
		for event in pygame.event.get():
            		if event.type == pygame.QUIT: sys.exit()
            				
			if pygame.key.get_pressed()[pygame.K_f]:
					currentQ = currentP
					currentP += 1
					
					if currentP >= len(controls): currentP = 0
            		if pygame.key.get_pressed()[pygame.K_RIGHT]:
					controls[currentP].position.x+= mvspd
					#physics.applyForce(i,physics.vector2d(20,0))	
            		if pygame.key.get_pressed()[pygame.K_LEFT]:
                                        controls[currentP].position.x-=mvspd
					#physics.applyForce(i,physics.vector2d(-20,0))
            		if pygame.key.get_pressed()[pygame.K_UP]:
					controls[currentP].position.y-=mvspd
					#physics.applyForce(i,physics.vector2d(0,-20))
            		if pygame.key.get_pressed()[pygame.K_DOWN]:
					controls[currentP].position.y+=mvspd
					#physics.applyForce(i,physics.vector2d(0,20))
			if pygame.key.get_pressed()[pygame.K_w]:
					controls[currentQ].position.y-= mvspd
			if pygame.key.get_pressed()[pygame.K_a]:
					controls[currentQ].position.x-= mvspd	
			if pygame.key.get_pressed()[pygame.K_s]:
					controls[currentQ].position.y+= mvspd
			if pygame.key.get_pressed()[pygame.K_d]:
					controls[currentQ].position.x+= mvspd	

		screen.fill(white)
		#for i in range(len(particles)-1):
		#	forceTest(frameCount,[3],particles[i],physics.vector2d(-5,0))
		#	forceTest(frameCount,[10],particles[i],physics.vector2d(0,-7))
		#	forceTest(frameCount,[15],particles[i],physics.vector2d(10,-8))
		for i in range(len(particles)):	
			if particles[i].position.y >= 490 or particles[i].position.y <= 10:
				particles[i].velocity.y *=-.9
			if particles[i].position.x >= 715 or particles[i].position.x <= 10:
				particles[i].velocity.x *=-.9	
				#particles[i].velocity.reverse(y)
				#forceTest(0,[0],particles[i],physics.vector2d(0,-9)) 
			particles[i].bump(particles)
			particles[i].update()
			particles[i].blit()
		pygame.display.flip()		

main()
