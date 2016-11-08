# Text Based Adventure
# module by printer83mph

import random

class Cow(object):
	
	def __init__(self):
		self.hp = 10
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
	
	def heal(self,amt):
		print(self.name + " healed for " + str(amt) + " hp!")
		self.hp += amt
	
	def talk():
		print("Moo")

class Bull(Cow):
	
	def __init__(self,start_hp,ap):
		self.hp = start_hp
		self.name = "Bull"
		self.alive = True
		self.atk_power = ap
	
	def attack(self,cow):
		print(self.name + " attacked " + cow.name + " for " + str(self.atk_power) + " damage!")
		cow.hurt(self.atk_power)
	
	def talk():
		print("Snort")

class Attack:
	
	def __init__(self,name,damage,uses):
		self.name = name
		self.damage = damage
		self.uses = uses

class SmartBull(Cow):
	
	def __init__(self,start_hp,atks):
		self.hp = start_hp
		self.name = "Smart Bull"
		self.alive = True
		self.attacks = atks
	
	def attack(self,cow):
		cur_atk = 0
		while(cur_atk <= len(self.attacks)-1):
			if(self.attacks[cur_atk].uses > 0):
				print(self.name + " used " + self.attacks[cur_atk].name + " against " + cow.name + " for " + str(self.attacks[cur_atk].damage) + " damage!")
				self.attacks[cur_atk].uses -= 1
				cow.hurt(self.attacks[cur_atk].damage)
				return
			cur_atk += 1
		print(self.name + " has no attacks left!")
	
	def talk():
		print("Snort (Greetings!)")
