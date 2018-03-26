import pygame
import math
from zombieBasic import Texture

class Ghost(pygame.sprite.Sprite):
	def __init__(self, texture, speed, posX, posY, hp, degats, fenetre):
		super().__init__()

		self.fenetre = fenetre

		self.name = "ghost"

		self.health_image = pygame.image.load("res\\entity\\zombieBasic\\health.png").convert_alpha()

		self.maxHP = hp
		self.hp = self.maxHP
		self.hp_100 = None
	
		self.rect = pygame.Rect(32, 32, 32, 32)
		self.rect.x = posX
		self.rect.y = posY

		self.len_move = len(texture.ghost_animation_move)
		
		self.move = False      

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

		self.death = False
	
		self.rotate_image = None
		self.degats = degats

		self.collide = []

		self.inWall = False

	def update(self, texture, player, wall_list, entity_list):
		
		if self.inWall == False:

			if self.rect.x > -32 and self.rect.y > -32:
				if self.rect.x < 1302 and self.rect.y < 752:
					if pygame.sprite.collide_rect(self, player) == True:
						self.move = False
						
						if self.counter_attack == 0:
							player.hp = player.hp - self.degats
						
						else:

							self.counter_attack = self.counter_attack + 1

							if self.counter_attack == 300:
								self.counter_attack = 0


					else:
						self.move = True
						self.counter_attack = 0


					if self.move == True:

						if self.counter_move == self.speed*1.5:
							self.counter_move = 1

							if self.frame_move == self.len_move:
								self.frame_move = 1
								
							else:
								self.frame_move = self.frame_move + 1 

						else:

							self.counter_move = self.counter_move + 1

							self.rotate_image = pygame.transform.rotate(texture.ghost_animation_move[self.frame_move - 1], self.angle)
							
							self.fenetre.blit(self.rotate_image, (self.rect.x - 16, self.rect.y - 16))

					
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
			self.rect.y = self.rect.y + self.delta_y * self.speed/2

			collide_wall = pygame.sprite.spritecollide(self, wall_list, False)
			collide_entity = pygame.sprite.spritecollide(self, entity_list, False)
			
			self.inWall = False

			for block in collide_wall:

				self.inWall = True

			self.hp_100 = (100 / self.maxHP) * self.hp

			if self.hp <= 0:
				pygame.sprite.Sprite.kill(self)
				player.inventory.money = player.inventory.money + 10

			if self.inWall == False:
				if self.hp >= 0:
					self.fenetre.blit(self.health_image, (self.rect.x, self.rect.y - 15), (0, 0, int((64/100) * self.hp_100), 8))
