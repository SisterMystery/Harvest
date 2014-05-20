import pygame,random, physics, harvest_screen, math
from harvest_screen import *

class blobPoint(object):
	def __init__(self,x,y):
		self.kind = "blobPoint"
		# add itself to the Things-with-mass list? 
		#get black pixel image and its 1x1 rectangle
		self.image = pygame.image.load("images/blackPixel.bmp")
		self.rect = self.image.get_rect().inflate(5,5)
		self.position = physics.vector2d(x,y)
		self.velocity = physics.vector2d(0,0) #x,y velocities (pixels per tick)
		#self.acceleration = physics.vector2d(0,0)  # x,y accelerations
	 	self.temperature = 20 # maybe irrelevant? maybe super important? 


	def bump(self,ptlist):
		for point in ptlist:
				 
			if abs(self.position.x - point.position.x) < 1 and abs(self.position.y - point.position.y) < 1:
				vect = physics.vector2d(self.position.x-point.position.x,self.position.y-point.position.y).unitize()
				physics.applyForce(self,vect.multiply(1))
				break
	"""			
	def bump(self,ptList):
		
		bumps = self.rect.collidelistall(ptList)
		
		#if bumps:
		#	self.velocity = self.velocity.multiply(.7).reverse()

		
		x = self.velocity.x
		y = self.velocity.y
		for i in bumps:
			x += ptList[i].velocity.x
			y += ptList[i].velocity.y
			x /= len(ptList)
			y /= len(ptList)
			
			self.velocity = physics.vector2d(x,y)
	"""	
	def accelerate(self):
	# In this world there are very few forces: here we check and apply them all to this blobPoint
		# accelerate for particle attraction
		physics.applyForce(self,physics.Gravity)
		# accelerate for solid?/liquid/air resistance
		#if not self.controlpt: 
		#	dragVect = self.velocity.multiply(-.2)
		self.velocity = self.velocity.multiply(.95) #drag? 
		if self.velocity.x + self.velocity.y > 350: #maximum speed?
			one = self.velocity.unitize()
			self.velocity = one.multiply(350)
		 #accelerate for other forces?   			
	def update(self):
		if self.position.x > width:
			self.position.x -= 1 + abs(self.position.x - width)
			self.velocity.x *= -.5	
		if self.position.x < 2:
			self.position.x += abs(self.position.x)
			self.velocity.x *= .5
		if self.position.y > height -50:
			self.position.y -= 51 - abs(self.position.y - height )
			self.velocity.y *= -.5
		if self.position.y < 1:
			self.position.y = 10
			self.velocity.x *= .5
	
		self.position = self.position.add(self.velocity)
		self.accelerate()
	
	def blit(self):
		self.rect.center = self.position.coords
		screen.blit(self.image,self.rect) 		
		
class controlPoint(blobPoint):
	def __init__(self,x,y,minions):
		blobPoint.__init__(self,x,y)
		self.parts = minions
		self.controls = []
		self.image = pygame.image.load("images/redPixel.bmp")
		self.kind = "controlPoint" 
		#DO THIS GODDAM THING!!!!
	def accelerate(self):
			self.velocity = self.velocity.multiply(.95) #drag? 
                  	if abs(self.velocity.x + self.velocity.y) > 5: #maximum speed?
                         	one = self.velocity.unitize()
                          	self.velocity = one.multiply(5)
			physics.applyForce(self,physics.Gravity)

			for point in self.parts:#.controls:
				
				dist = math.sqrt(math.pow(self.position.x-point.position.x,2)+math.pow(self.position.y-point.position.y,2))
				vect = physics.vector2d(self.position.x-point.position.x,self.position.y-point.position.y).unitize()
				newdist = math.sqrt(math.pow(self.controls[0].position.x-point.position.x,2)+math.pow(self.controls[0].position.y-point.position.y,2))
				
				if dist > 23 and newdist > 23  and point.kind == "blobPoint" : #and newdist >  50:
					#point.velocity = point.velocity.multiply(.5)
					if dist + newdist > 120:
						vect = vect.divide(math.pow(dist,1.001))
						physics.applyForce(point,vect.multiply(70))
					else:
						physics.applyForce(point,vect.multiply(3))
					#point.velocity = vect.multiply(5)
					
					#point.position = self.position
					#point.position.y += random.choice((-1,1))/10
					#point.position.x += random.choice((-1,1))/10
					#point.velocity = vect.unitize().multiply(10)
					#vect = vect.reverse()
					#physics.applyForce(point,vect)
				if dist < 2 and point.kind == "blobPoint" :#or newdist < 40:
					#point.velocity = vect.unitize().multiply(-10)
					physics.applyForce(point,vect.reverse().multiply(3))
					#point.velocity = vect.multiply(-4)
						
				if point.kind == "controlPoint" and dist > 60 :
					self.position = self.position.add(vect)
								
					

	def bump(self,ptList):
		#i = self.rect.collidelist(ptList)
		#ptList[i].velocity = ptList[i].velocity.multiply(.8).reverse()	
		return 0

		
