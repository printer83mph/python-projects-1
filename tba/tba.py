# Text Based Adventure
# module by printer83mph

class Cow(object):
	
	def __init__(self,start_hp=10):
		self.hp = start_hp
		self.max_hp = start_hp
		self.name = "Cow"
		self.alive = True
	
	def rename(self,new_name):
		self.name = new_name

	def kill(self):
		print(self.name + " fainted!")
		self.alive = False
		
	def hurt(self,amt):
		self.hp -= amt
		if(self.hp <= 0):
			self.kill()
	
	def can_attack(self):
		return False
	
	def heal(self,amt):
		old_hp = self.hp
		self.hp = min(self.hp + amt, self.max_hp)
		print(self.name + " healed for " + str(self.hp - old_hp) + " hp!")
	
	def health_up(self,amt=1):
		self.max_health += amt
	
	def talk():
		print("Moo")

class Bull(Cow):
	
	def __init__(self,start_hp=10,ap=2):
		self.hp = start_hp
		self.max_hp = start_hp
		self.name = "Bull"
		self.alive = True
		self.atk_power = ap
	
	def attack(self,cow):
		print(self.name + " attacked " + cow.name + " for " + str(self.atk_power) + " damage!")
		cow.hurt(self.atk_power)
	
	def can_attack(self):
		return True
	
	def talk():
		print("Snort")

class Weapon:
	
	def __init__(self,name,damage=3,uses=5):
		self.name = name
		self.damage = damage
		self.uses = uses
	
	def tamper(self,amt):
		self.uses -= amt

class Monkey(Cow):
	
	def __init__(self,start_hp=10,weps=[]):
		self.hp = start_hp
		self.max_hp = start_hp
		self.name = "Monkey"
		self.alive = True
		self.weapons = weps
	
	def attack(self,cow):
		cur_wep = 0
		while(cur_wep <= len(self.weapons)-1):
			if(self.weapons[cur_wep].uses > 0):
				print(self.name + " used " + self.weapons[cur_wep].name + " against " + cow.name + " for " + str(self.weapons[cur_wep].damage) + " damage!")
				self.weapons[cur_wep].uses -= 1
				cow.hurt(self.weapons[cur_wep].damage)
				return
			cur_wep += 1
		print(self.name + " can't attack!")
	
	def can_attack(self):
		cur_wep = 0
		while(cur_wep <= len(self.weapons)-1 and self.alive):
			if(self.weapons[cur_wep].uses > 0):
				return True
			cur_wep += 1
		return False
	
	def talk():
		print("I kill you!")
	
	def give(self,wep):
		print(self.name + " got " + wep.name + "!")
		self.weapons.append(wep)

class Farmer(Cow):
	
	def __init__(self,start_hp=10,owned=[]):
		self.hp = start_hp
		self.max_hp = start_hp
		self.name = "Farmer"
		self.alive = True
		self.owned = owned
	
	def attack(self,cow):
		cur_cow = 0
		while(cur_cow <= len(self.owned)-1):
			if(self.owned[cur_cow].can_attack()):
				print(self.name + " deployed " + self.owned[cur_cow].name + "!")
				self.owned[cur_cow].attack(cow)
				return
			cur_cow += 1
		print(self.name + " can't attack!")
