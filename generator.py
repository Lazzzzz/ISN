import pygame
import random
import math
from zombieBasic import *
from ghost import *
from item import *

class CollideBlock(pygame.sprite.Sprite):
	def __init__(self, posX, posY):
		super().__init__()

		self.rect = pygame.Rect(64, 64, 64, 64)

		self.rect.x = posX
		self.rect.y = posY


class SpawnBlock(pygame.sprite.Sprite):
	def __init__(self, posX, posY):
		super().__init__()

		self.rect = pygame.Rect(64, 64, 64, 64)

		self.rect.x = posX
		self.rect.y = posY

class MapLoader():
	def __init__(self, fenetre):
		
		print("Initialisation de MapLoader...")

		self.fenetre = fenetre

		self.wall_list = pygame.sprite.Group()

		self.level_list = []
		
		self.level = None
		self.wall = None
		self.map = None

		self.posX = 64
		self.posY = 64

		self.chunk_size_x = 320
		self.chunk_size_y = 180

		self.number_chunk_x = 0
		self.number_chunk_x = 0
		
		self.speed_update = 4

		self.move_left = False
		self.move_right = False
		self.move_up = False
		self.move_down = False

		self.counter_x = self.chunk_size_x
		self.counter_y = self.chunk_size_y

		self.minimap_image = pygame.image.load("res\\gui\\minimap.png").convert_alpha()

		self.minimap = None
		self.minimap_scale_x = None
		self.minimap_scale_y = None

		self.font = pygame.font.Font("res\\font\\TIMER.TTF", 20)
		self.font_counter = pygame.font.Font("res\\font\\TIMER.TTF", 30)
		self.time = None

		print("...finis")

	def addMap(self, map):

		self.level_list.append(map)

	def randomMap(self):

		if self.level_list == None:
			print("aucune map dans le repertoire")

		else:
			self.level = random.choice(self.level_list)
			self.map = self.level.map
		
		for y in range(0, len(self.level.wall)):
			for x in range(0, len(self.level.wall[y])):
				
				if self.level.wall[y][x] == 1:
					self.wall_list.add(CollideBlock(x*64 + self.posX, y*64 + self.posY))
				
				if self.level.wall[y][x] == 1:
					self.wall_list.add(CollideBlock(x*64 + self.posX, y*64 + self.posY))
		
		self.minimap = pygame.transform.scale(self.map, (150, 150))
		
		self.minimap_scale_x = 150 /self.level.size_x
		self.minimap_scale_y = 150 / self.level.size_y

	def loadMap(self, map):
		
		if self.level_list == None:
			print("aucune map dans le repertoire")

		else:
			self.level = self.level_list[map]
			self.map = self.level.map
		
		for y in range(0, len(self.level.wall)):
			for x in range(0, len(self.level.wall[y])):
				
				if self.level.wall[y][x] == 1:
					self.wall_list.add(CollideBlock(x*64 + self.posX, y*64 + self.posY))
				
				if self.level.wall[y][x] == 1:
					self.wall_list.add(CollideBlock(x*64 + self.posX, y*64 + self.posY))
		
		self.minimap = pygame.transform.scale(self.map, (150, 150))
		
		self.minimap_scale_x = 150 /self.level.size_x
		self.minimap_scale_y = 150 / self.level.size_y

	def chunkUpdate(self, player, entity_list, bullet_list, chest_list, spawn_point, spawn_chest):

		if player.rect.x > 640 + self.chunk_size_x:
			self.move_left = True

		if player.rect.x < 640 - self.chunk_size_x:
			self.move_right = True

		if player.rect.y > 360 + self.chunk_size_y:
			self.move_down = True

		if player.rect.y < 360 - self.chunk_size_y:
			self.move_up = True

		if self.move_left == True:
			if self.counter_x != 0:
				self.counter_x = self.counter_x - self.speed_update

			else:
				self.counter_x = self.chunk_size_x
				self.move_left = False

			self.posX = self.posX - self.speed_update

			for wall in self.wall_list:	
				wall.rect.x = wall.rect.x - self.speed_update

			for entity in entity_list:
				entity.rect.x = entity.rect.x - self.speed_update 

			for bullet in bullet_list:
				bullet.rect.x = bullet.rect.x - self.speed_update
			
			for chest in chest_list:
				chest.rect.x = chest.rect.x - self.speed_update

			for spawn in spawn_point:
				spawn.rect.x = spawn.rect.x - self.speed_update
			
			for spawn in spawn_chest:
				spawn.rect.x = spawn.rect.x - self.speed_update			
			
			player.rect.x = player.rect.x - self.speed_update
		
		if self.move_right == True:
			if self.counter_x != 0:
				self.counter_x = self.counter_x - self.speed_update

			else:
				self.counter_x = self.chunk_size_x
				self.move_right = False

			self.posX = self.posX + self.speed_update

			for wall in self.wall_list:	
				wall.rect.x = wall.rect.x + self.speed_update

			for entity in entity_list:
				entity.rect.x = entity.rect.x + self.speed_update 

			for bullet in bullet_list:
				bullet.rect.x = bullet.rect.x + self.speed_update
			
			for chest in chest_list:
				chest.rect.x = chest.rect.x + self.speed_update

			for spawn in spawn_point:
				spawn.rect.x = spawn.rect.x + self.speed_update
			
			for spawn in spawn_chest:
				spawn.rect.x = spawn.rect.x + self.speed_update
			
			player.rect.x = player.rect.x + self.speed_update
		
		if self.move_down == True:
			if self.counter_y != 0:
				self.counter_y = self.counter_y - self.speed_update

			else:
				self.counter_y = self.chunk_size_y
				self.move_down = False

			self.posY = self.posY - self.speed_update

			for wall in self.wall_list:	
				wall.rect.y = wall.rect.y - self.speed_update

			for entity in entity_list:
				entity.rect.y = entity.rect.y - self.speed_update 
			
			for bullet in bullet_list:
				bullet.rect.y = bullet.rect.y - self.speed_update
			
			for chest in chest_list:
				chest.rect.y = chest.rect.y - self.speed_update

			for spawn in spawn_point:
				spawn.rect.y = spawn.rect.y - self.speed_update
			
			for spawn in spawn_chest:
				spawn.rect.y = spawn.rect.y - self.speed_update
			
			player.rect.y = player.rect.y - self.speed_update
		
		if self.move_up == True:
			if self.counter_y != 0:
				self.counter_y = self.counter_y - self.speed_update

			else:
				self.counter_y = self.chunk_size_y
				self.move_up = False

			self.posY = self.posY + self.speed_update

			for wall in self.wall_list:	
				wall.rect.y = wall.rect.y + self.speed_update

			for entity in entity_list:
				entity.rect.y = entity.rect.y + self.speed_update

			for bullet in bullet_list:
				bullet.rect.y = bullet.rect.y + self.speed_update

			for chest in chest_list:
				chest.rect.y = chest.rect.y + self.speed_update

			for spawn in spawn_point:
				spawn.rect.y = spawn.rect.y + self.speed_update

			for spawn in spawn_chest:
				spawn.rect.y = spawn.rect.y + self.speed_update

			player.rect.y = player.rect.y + self.speed_update

	def miniMap(self, player, entity_list, chest_list, waveGenerator):

		pygame.draw.rect(self.fenetre, (182,182,182), (1110, 20, 150,150))

		for y in range(0, len(self.level.wall)):
			for x in range(0, len(self.level.wall[y])):
				if self.level.wall[y][x] == 1:

					pygame.draw.rect(self.fenetre, (54,54,54), (1110 + ((x*64)*self.minimap_scale_x), 20 + ((y*64)*self.minimap_scale_y), 64*self.minimap_scale_x, 64*self.minimap_scale_y))
		self.fenetre.blit(self.minimap_image, (1105, 15))
		pygame.draw.rect(self.fenetre, (0,0,255) , ( (1110 -self.posX * self.minimap_scale_x) + (player.rect.x * self.minimap_scale_x), (20 -self.posY * self.minimap_scale_y) + (player.rect.y * self.minimap_scale_x), 4,4))

		for entity in entity_list:
			pygame.draw.rect(self.fenetre, (255,0,0) , ( (1110 -self.posX * self.minimap_scale_x) + (entity.rect.x * self.minimap_scale_x), (20 -self.posY * self.minimap_scale_y) + (entity.rect.y * self.minimap_scale_x), 2,2))

		for chest in chest_list:
			pygame.draw.rect(self.fenetre, (0,255,0) , ( (1110 -self.posX * self.minimap_scale_x) + (chest.rect.x * self.minimap_scale_x), (20 -self.posY * self.minimap_scale_y) + (chest.rect.y * self.minimap_scale_x), 4,4))
		
		self.time = str(int(waveGenerator.counter/60))
		self.fenetre.blit((self.font.render("Next Wave in :", False, (163, 35, 35))), (1115,180))
		
		if int(waveGenerator.counter/60) == 0:
			self.fenetre.blit((self.font.render("ongoing...", False, (163, 35, 35))), (1135,200))			
		
		else:

			self.fenetre.blit((self.font_counter.render(self.time, False, (163, 35, 35))), (1155,200))

class Chest(pygame.sprite.Sprite):
	def __init__(self, posX, posY, item, fenetre):
		super().__init__()

		self.fenetre = fenetre

		self.image = pygame.image.load("res\\chest\\chest.png").convert_alpha()
		self.gui = pygame.image.load("res\\gui\\chest_ingame_gui.png").convert_alpha()

		self.rect = self.image.get_rect()

		self.spawn = False

		self.font = pygame.font.Font("res\\font\\ZOMBIE.TTF", 60)
		self.counter = 180

		self.inventory = []
		self.inventory.append(item)

		self.inventory_open = False

		self.rect.x = posX
		self.rect.y = posY

		self.despawn_counter = 10800 # 3 minutes

	def remove(self):

		pygame.sprite.Sprite.kill(self)

	def update(self, player):

		self.fenetre.blit(self.image, (self.rect.x, self.rect.y))

		if self.despawn_counter == 0:
			self.remove()
		
		else:
			self.despawn_counter = self.despawn_counter - 1

		if self.counter > 0:
			self.counter = self.counter - 1
			self.fenetre.blit((self.font.render("A chest has just appeared", False, (35, 163, 35))), (275,130))
			
		if pygame.sprite.collide_rect(self, player) == True:

			for item in self.inventory:
				self.fenetre.blit(self.gui, (0,0))
				self.fenetre.blit(item.icon, (10, 660))
				self.inventory_open = True

		else:
			self.inventory_open = False

class WaveGenerator():
	def __init__(self, wall_list, maploader, fenetre):
		
		self.fenetre = fenetre
		self.wave = float(0)

		self.counter = 7200
		self.mob_cap = 50

		self.attack_factor = 1
		self.health_factor = 1
		self.mob_factor = 2
		self.weapon_factor = 1
		
		self.spawn_point = []
		self.spawn_chest = []

		self.set_spawn = False
		
		self.number_spawn_point = 20
		self.counter_spawn = 0
		
		self.number_chest_point = 100
		self.counter_chest = 0

		self.spawn = None
		self.mob_count = 0

		self.msg_counter = 180

		self.newWave = False
		self.newMsg = False

		self.newChest = False
		self.chest_counter = 60
		
		self.font = pygame.font.Font("res\\font\\ZOMBIE.TTF", 60)

		self.categorie_choise = None
		self.item_choise = None

		self.luck_counter = 3600 
		self.zombie_spawn_counter = 0

		self.categorie = [

		"weapon",	
		"pistol",
		"special",
		"health"

		]


		self.drop_list_weapon = [
		
		"AK"
		
		]

		self.drop_list_pistol = [
		
		"Uzi"
		
		]
		
		self.drop_list_special = [
		
		"Bazooka"
		
		]


		self.drop_list_health = [
		
		"heal_kit",
		"medoc",
		"pills",
		"syringe"
		
		]


		print("generation des spawn point ...")

		while not self.set_spawn:

			if self.counter_spawn < self.number_spawn_point:

				x = random.randint(64, maploader.level.size_x - 64)
				y = random.randint(64, maploader.level.size_y - 64)

				collide_wall = pygame.sprite.spritecollide(SpawnBlock(x, y) , wall_list, False) 

				if len(collide_wall) == 0:

					self.spawn_point.append(SpawnBlock(x,y))
					self.counter_spawn = self.counter_spawn + 1
			
			if self.counter_chest < self.number_chest_point:

				x2 = random.randint(32, maploader.level.size_x - 32)
				y2 = random.randint(32, maploader.level.size_y - 32)
				
				collide_wall = pygame.sprite.spritecollide(SpawnBlock(x2, y2) , wall_list, False) 

				if len(collide_wall) == 0:

					self.spawn_chest.append(SpawnBlock(x2, y2))
					self.counter_chest = self.counter_chest + 1 	
			
			if self.counter_chest == self.number_chest_point:
				if self.counter_chest == self.number_chest_point:					

					self.set_spawn = True
					print("... finis")

	def update(self, texture, wall_list, entity_list, chest_list, spawn_point, maploader, player):
		
		if self.newWave == True:
			if self.zombie_spawn_counter == 0:
				
				self.spawn = random.choice(spawn_point)
				entity_list.add(ZombieBasic(texture, random.randint(4, 8), self.spawn.rect.x, self.spawn.rect.y, 20+self.health_factor, 10+self.attack_factor, self.fenetre))
				
				self.spawn = random.choice(spawn_point)
				entity_list.add(Ghost(texture, random.randint(4, 8), self.spawn.rect.x, self.spawn.rect.y, 5+self.health_factor, 5+self.attack_factor, self.fenetre))

				self.counter_spawn = self.counter_spawn + 1
				self.zombie_spawn_counter = 60

			else:
				self.zombie_spawn_counter = self.zombie_spawn_counter - 1

			if self.counter_spawn >= self.mob_factor:
				self.newWave = False
				self.counter_spawn = 0
				self.counter = 36000
			
		else:

			self.counter = self.counter - 1
			
			if self.counter == 0:

				self.wave = self.wave + 1
				self.newWave = True
				self.newMsg = True
				
				self.attack_factor = random.randint(int(self.attack_factor + self.attack_factor*(1/8)) - 2, int(self.attack_factor + self.attack_factor*(1/8) + 2))
				self.health_factor = random.randint(int(self.health_factor + self.health_factor*(1/5)) - 2, int(self.health_factor + self.health_factor*(1/5) + 2))
				self.mob_factor = random.randint(int(self.mob_factor + self.mob_factor*(1/8)), int(self.mob_factor + self.mob_factor*(1/8) + 2))
				self.weapon_factor = random.randint(int(self.weapon_factor + self.weapon_factor*(1/10)), int(self.weapon_factor + self.weapon_factor*(1/10) + 2))

				print(self.attack_factor, self.health_factor, self.mob_factor, self.weapon_factor)

			if self.counter > 300:
				if len(entity_list) == 0:
						self.counter = 300 # 10 secondes

		if self.newMsg == True:
			
			self.msg_counter = self.msg_counter - 1
			
			self.fenetre.blit((self.font.render("NEW WAVE", False, (163, 35, 35))), (500,200))
			self.fenetre.blit((self.font.render(str(int(self.wave)), False, (163, 35, 35))), (650,270))
			
			if self.msg_counter == 0:
				self.msg_counter = 180
				self.newMsg = False	

		if self.newChest == True:

			self.spawn = random.choice(self.spawn_chest)
			
			self.categorie_choise = random.choice(self.categorie)

			if self.categorie_choise == "weapon":
				self.item_choise = random.choice(self.drop_list_weapon)
			
				if self.item_choise == "AK":
					chest_list.add(Chest(self.spawn.rect.x, self.spawn.rect.y, AK(10+self.weapon_factor, self.fenetre),  self.fenetre))
					self.newChest = False					
			
			if self.categorie_choise == "pistol":
				self.item_choise = random.choice(self.drop_list_pistol)
				
				if self.item_choise == "Uzi":
					chest_list.add(Chest(self.spawn.rect.x, self.spawn.rect.y, Uzi(5+self.weapon_factor, self.fenetre),  self.fenetre))
					self.newChest = False

			if self.categorie_choise == "special":
				self.item_choise = random.choice(self.drop_list_special)

				if self.item_choise == "Bazooka":
					chest_list.add(Chest(self.spawn.rect.x, self.spawn.rect.y, Bazooka(25+self.weapon_factor, self.fenetre),  self.fenetre))
					self.newChest = False
		
			if self.categorie_choise == "health":
				self.item_choise = random.choice(self.drop_list_health)			

				if self.item_choise == "heal_kit":
					chest_list.add(Chest(self.spawn.rect.x, self.spawn.rect.y, heal_kit(self.fenetre),  self.fenetre))
					self.newChest = False
			
				elif self.item_choise == "medoc":
					chest_list.add(Chest(self.spawn.rect.x, self.spawn.rect.y, medoc(self.fenetre),  self.fenetre))
					self.newChest = False				
			
				elif self.item_choise == "pills":
					chest_list.add(Chest(self.spawn.rect.x, self.spawn.rect.y, pills(self.fenetre),  self.fenetre))
					self.newChest = False
			
				elif self.item_choise == "syringe":
					chest_list.add(Chest(self.spawn.rect.x, self.spawn.rect.y, syringe(self.fenetre),  self.fenetre))
					self.newChest = False
		else:
			self.chest_counter = self.chest_counter - 1
			self.luck_counter = self.luck_counter - 1

			if self.luck_counter == 0:
				if random.randint(0, 20) == 1:
					self.newChest = True

			if self.chest_counter == 0:
				self.newChest = True
				self.chest_counter = 10800

