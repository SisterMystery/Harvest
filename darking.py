import pygame,random, physics, harvest_screen, math
from harvest_screen import *

class blobPoint(object):
	def __init__(self,x,y):
		# add itself to the Things-with-mass list? 
		#get black pixel image and its 1x1 rectangle
		self.image = pygame.image.load("images/blackPixel.bmp")
		self.rect = self.image.get_rect().inflate(3,3)
		self.position = physics.vector2d(x,y)
		self.velocity = physics.vector2d(0,0) #x,y velocities (pixels per tick)
		#self.acceleration = physics.vector2d(0,0)  # x,y accelerations
	 	self.temperature = 20 # maybe irrelevant? maybe super important? 
		self.controlpt = False	


	def bump(self,ptList):
		i = self.rect.collidelist(ptList)
		ptList[i].velocity,self.velocity = self.velocity.multiply(.6),ptList[i].velocity.multiply(.6)	

	def accelerate(self):
	# In this world there are very few forces: here we check and apply them all to this blobPoint
		# accelerate for particle attraction
		physics.applyForce(self,physics.Gravity)
		# accelerate for solid?/liquid/air resistance
		#if not self.controlpt: 
		#	dragVect = self.velocity.multiply(-.2)
		self.velocity = self.velocity.multiply(.95)
		if self.velocity.x + self.velocity.y > 150:
			self.velocity = physics.vector2d(10,10)
		 #accelerate for other forces?   			
	def update(self):
		if self.position.x > width:
			self.position.x = width -1
			self.velocity = self.velocity.reverse()	
		if self.position.x < 0:
			self.position.x = 1
			self.velocity = self.velocity.reverse()	
		if self.position.y > height:
			self.position.y = height-1
			self.velocity = self.velocity.reverse()	
		if self.position.y < 0:
			self.position.y = 1
			self.velocity = self.velocity.reverse()	
		self.velocity = self.velocity.multiply(.65)
		self.position = self.position.add(self.velocity)
		self.accelerate()
	
	def blit(self):
		self.rect.center = self.position.coords
		screen.blit(self.image,self.rect) 		
		
class controlPoint(blobPoint):
	def __init__(self,x,y):
		blobPoint.__init__(self,x,y)
		#DO THIS GODDAM THING!!!!
	def accelerate(self):
			for point in self.parts:
				dist = math.sqrt(math.pow(self.position.x-point.position.x,2)+math.pow(self.position.y-point.position.y,2))
				vect = physics.vector2d(self.position.x-point.position.x,self.position.y-point.position.y).unitize()
				vect = vect.multiply(350)
				
				vect = vect.divide(math.pow(dist,1.5))
				physics.applyForce(point,vect)	
				if self.rect.colliderect(point.rect):
					self.velocity = physics.vector2d(0,0)
					point.velocity = physics.vector2d(0,0)
				if dist <= 50 and point.controlpt:
					#point.velocity = point.velocity.reverse()
					point.velocity = physics.vector2d(0,0)
					vect = vect.reverse()
					#physics.applyForce(point,vect)
				if dist <= 50 and not point.controlpt:
					point.velocity = point.velocity.multiply(.5)
		
				if dist >= 200 and not point.controlpt:
					a = random.randint(-70,70)
					b = random.randint(-70,70)
					if abs(a) > 30:
						a = random.randint(-70,70)
					if abs(b) > 30:
						b = random.randint(-70,70)
					point.position = self.position.add(physics.vector2d(a,b))
		# accelerate for gravity
		
