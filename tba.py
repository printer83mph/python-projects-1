class Cow(object):
	
	def __init__(self):
		self.hp = 10
		self.name = "Cow"
		self.alive = True
		
	def kill(self):
		self.alive = False
		
	def hurt(self,amt):
		self.hp -= amt
		if(self.hp <= 0):
			self.kill()
	
	def heal(self,amt):
		self.hp += amt
	
	def talk():
		print("Moo")
