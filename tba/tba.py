# Text Based Adventure
# module by printer83mph

class Cow(object):
	
	def __init__(self):
		self.hp = 10
		self.name = "Cow"
		self.alive = True
	
	def rename(self,new_name):
		self.name = new_name

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

class Enemy(Cow):
	
	def __init__(self,start_hp,ap):
		self.hp = start_hp
		self.name = "Enemy"
		self.alive = True
		self.atk_power = ap
	
	def attack(self):
		return self.atk_power
