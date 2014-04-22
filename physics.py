import math

class vector2d(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.coords = [x,y]

	def add(self,vector):
		x = self.x + vector.x
		y = self.y + vector.y
		return vector2d(x,y)

	def reverse(self):
		return vector2d(-self.x,-self.y)
	
	def unitize(self):
		one = abs(float(self.x)) + abs(float(self.y))
		if one == 0: return(vector2d(0,0))
		return vector2d(self.x/one,self.y/one)
	
	def multiply(self,num):
		return vector2d(self.x*num,self.y*num)	
	
	def divide(self,num):
		num = float(num)
		if num == 0: return(vector2d(0,0))
		return vector2d(self.x/num,self.y/num)

def applyForce(mass,vector):
	mass.velocity = mass.velocity.add(vector)

def forceTest(count,frames,mass,vector):
	if count in frames:
		physics.applyForce(mass,vector)

Gravity = vector2d(0,.980665) # pixel/second^2 = centimeter/second^2		
