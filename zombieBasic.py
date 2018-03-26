import pygame
import math

class Texture():
	def __init__(self, scaleX, scaleY):

		self.animation_spawn = []
		self.animation_move = []
		self.animation_attack = []
		self.animation_death = []

		self.ghost_animation_move = []

		self.image = pygame.image.load("res\\entity\\zombieBasic\\spawn\\zombie_spawn_0001.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation_spawn.append(self.image)

		self.image = pygame.image.load("res\\entity\\zombieBasic\\spawn\\zombie_spawn_0002.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation_spawn.append(self.image)

		self.image = pygame.image.load("res\\entity\\zombieBasic\\move\\zombie_move_0001.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation_move.append(self.image)

		self.image = pygame.image.load("res\\entity\\zombieBasic\\move\\zombie_move_0002.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation_move.append(self.image)

		self.image = pygame.image.load("res\\entity\\zombieBasic\\move\\zombie_move_0003.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation_move.append(self.image)

		self.image = pygame.image.load("res\\entity\\zombieBasic\\move\\zombie_move_0004.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation_move.append(self.image)

		self.image = pygame.image.load("res\\entity\\zombieBasic\\attack\\zombie_attack_0001.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation_attack.append(self.image)

		self.image = pygame.image.load("res\\entity\\zombieBasic\\attack\\zombie_attack_0002.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation_attack.append(self.image)

		self.image = pygame.image.load("res\\entity\\zombieBasic\\death\\death_001.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation_death.append(self.image)
		
		self.image = pygame.image.load("res\\entity\\zombieBasic\\death\\death_002.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation_death.append(self.image)
		
		self.image = pygame.image.load("res\\entity\\zombieBasic\\death\\death_003.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation_death.append(self.image)
		
		self.image = pygame.image.load("res\\entity\\zombieBasic\\death\\death_004.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation_death.append(self.image)
	
		self.image = pygame.image.load("res\\entity\\zombieBasic\\death\\death_005.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation_death.append(self.image)
		
		self.image = pygame.image.load("res\\entity\\zombieBasic\\death\\death_006.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation_death.append(self.image)

		self.image = pygame.image.load("res\\entity\\zombieBasic\\death\\death_007.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation_death.append(self.image)

		self.image = pygame.image.load("res\\entity\\ghost\\ghost001.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.ghost_animation_move.append(self.image)

		self.image = pygame.image.load("res\\entity\\ghost\\ghost002.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.ghost_animation_move.append(self.image)

		self.image = pygame.image.load("res\\entity\\ghost\\ghost003.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.ghost_animation_move.append(self.image)

		self.image = pygame.image.load("res\\entity\\ghost\\ghost004.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.ghost_animation_move.append(self.image)

		self.image = pygame.image.load("res\\entity\\ghost\\ghost005.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.ghost_animation_move.append(self.image)

		self.image = pygame.image.load("res\\entity\\ghost\\ghost006.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.ghost_animation_move.append(self.image)

class ZombieBasic(pygame.sprite.Sprite):
	def __init__(self, texture, speed, posX, posY, hp, degats, fenetre):
		super().__init__()

		self.fenetre = fenetre
		
		self.name = "zombie"
		
		self.health_image = pygame.image.load("res\\entity\\zombieBasic\\health.png").convert_alpha()

		self.maxHP = hp
		self.hp = self.maxHP
		self.hp_100 = None
	
		self.rect = pygame.Rect(32, 32, 32, 32)
		self.rect.x = posX
		self.rect.y = posY

		self.len_spawn = len(texture.animation_spawn)
		self.len_move = len(texture.animation_move)
		self.len_attack = len(texture.animation_attack)
		self.len_death = len(texture.animation_death)

		self.spawn = True
		self.move = False       
		self.attack = False
		self.death = False
		
		self.frame_spawn = 1
		self.counter_spawn = 1

		self.frame_move = 1
		self.counter_move = 1
			
		self.frame_attack = 1
		self.counter_attack = 1

		self.frame_death = 1
		self.counter_death = 1

		self.speed = speed

		self.delta_x = None
		self.delta_y = None

		self.dist = None
		self.angle = 0
	
		self.rotate_image = None
		self.degats = degats

		self.collide = []


	def update(self, texture, player, wall_list, entity_list):
		
		if self.rect.x > -32 and self.rect.y > -32:
			if self.rect.x < 1302 and self.rect.y < 752:
				if pygame.sprite.collide_rect(self, player) == True:
					self.attack = True
					self.move = False

				if self.spawn == True:

					if self.counter_spawn >= self.speed*2:
					
						self.counter_spawn = 1
						self.spawn = False
						self.move = True
						self.frame_spawn = self.frame_spawn + 1
					
					else:
						self.counter_spawn = self.counter_spawn + 1

					self.fenetre.blit(texture.animation_spawn[self.frame_spawn - 1], (self.rect))
				
				elif self.move == True:

					if self.counter_move == self.speed:
						self.counter_move = 1

						if self.frame_move == self.len_move:
							self.frame_move = 1
						
						else:
							self.frame_move = self.frame_move + 1 

					else:

						self.counter_move = self.counter_move + 1

					self.rotate_image = pygame.transform.rotate(texture.animation_move[self.frame_move - 1], self.angle)
					
					self.fenetre.blit(self.rotate_image, (self.rect.x - 16, self.rect.y - 16))

				elif self.attack == True:
				
				
					if self.counter_attack >= self.speed*3:
						self.counter_attack = 1

						if self.frame_attack == self.len_attack:
							self.frame_attack = 1
							self.attack = False
							self.move = True
							player.hp = player.hp - self.degats
					
						else:
							self.frame_attack = self.frame_attack + 1 

					else:

						self.counter_attack = self.counter_attack + 1

					self.rotate_image = pygame.transform.rotate(texture.animation_attack[self.frame_attack - 1], self.angle)

					self.fenetre.blit(self.rotate_image, (self.rect))

				if self.death == True:
					
					if self.frame_death >= self.len_death:
						
						pygame.sprite.Sprite.kill(self)
						player.inventory.money = player.inventory.money + 5

					if self.counter_death >= self.speed*0.5:
						
						self.counter_death = 1
						self.frame_death = self.frame_death + 1
			
					else:
						self.counter_death = self.counter_death + 1
			
					self.fenetre.blit(texture.animation_death[self.frame_death - 1], (self.rect))
			
			else:
				self.spawn = False
				self.move = True

		else:
			self.spawn = False
			self.move = True
		
		if self.move == True:
		
			self.delta_x = player.rect.x - self.rect.x
			self.delta_y = player.rect.y - self.rect.y

			self.dist = math.hypot(self.delta_x, self.delta_y)
			
			if self.dist != 0:
				if self.delta_x >= 0 and self.delta_y >= 0:
					self.angle = math.degrees(math.acos(abs(self.delta_y / self.dist)))
					
				elif self.delta_x < 0 and self.delta_y > 0:
					self.angle = 360 - math.degrees(math.asin(abs(self.delta_x / self.dist)))
		
				elif self.delta_x <= 0 and self.delta_y <= 0:
					self.angle = 180 + math.degrees(math.acos(abs(self.delta_y / self.dist)))
		
				elif self.delta_x >= 0 and self.delta_y < 0:        
					self.angle = 180 - math.degrees(math.asin(abs(self.delta_x / self.dist)))

			if self.dist != 0:
				
				self.delta_x = (self.delta_x / self.dist)
				self.delta_y = (self.delta_y / self.dist)

			self.rect.x = self.rect.x + self.delta_x * self.speed/2

			collide_wall = pygame.sprite.spritecollide(self, wall_list, False)
			collide_entity = pygame.sprite.spritecollide(self, entity_list, False)
			
			for block in collide_wall:

				if self.delta_x * self.speed/2 > 0:
					self.rect.right = block.rect.left
				
				if self.delta_x * self.speed/2 < 0:
					self.rect.left = block.rect.right

			for entity in collide_entity:
				if self != entity:
					if entity.name != "ghost":
						if entity.death == False:					
							if self.delta_x * self.speed/2 > 0:
								self.rect.right = entity.rect.left
					
							if self.delta_x * self.speed/2 < 0:
								self.rect.left = entity.rect.right


			self.rect.y = self.rect.y + self.delta_y * self.speed/2
			
			collide_wall = pygame.sprite.spritecollide(self, wall_list, False)
			collide_entity = pygame.sprite.spritecollide(self, entity_list, False)
			
			for block in collide_wall:
			
				if self.delta_y * self.speed/2 > 0:
					self.rect.bottom = block.rect.top
				
				if self.delta_y * self.speed/2 < 0:
					self.rect.top = block.rect.bottom 

			for entity in collide_entity:
				if self != entity:
					if entity.name != "ghost":
						if entity.death == False:
							if self.delta_y * self.speed/2 > 0:
								self.rect.bottom = entity.rect.top
						
							if self.delta_y * self.speed/2 < 0:
								self.rect.top = entity.rect.bottom 
		
			self.hp_100 = (100 / self.maxHP) * self.hp

			if self.hp <= 0:
				self.death = True
				self.move = False
				self.attack = False
				self.rect = pygame.Rect(self.rect.x, self.rect.y, 0, 0)

			if self.hp >= 0:
				self.fenetre.blit(self.health_image, (self.rect.x, self.rect.y - 15), (0, 0, int((64/100) * self.hp_100), 8))
