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
		self.alive = False
		
	def hurt(self,amt):
		self.hp -= amt
		if(self.hp <= 0):
			self.kill()
	
	def heal(self,amt):
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
		cow.hurt(self.atk_power)

class Attack:
	
	def __init__(self,name,damage,uses):
		self.name = name
		self.damage = damage
		self.uses = uses

class SmartBull(Cow):
	
	def __init__(self,start_hp,atks,atknames,atktimes):
		self.hp = start_hp
		self.name = "Smart Bull"
		self.alive = True
		self.attacks = atks
	
	def attack(self,cow):
		cow.hurt(5)
