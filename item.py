import pygame
import math

BLACK = (0, 0, 0)
WHITE = (255, 255 ,255)
RED = (255, 0 ,0) 
GREEN = (0, 255 ,0)
BLUE = (0, 0 ,255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

#=========Type==========#

#weapon
#pistol
#special
#heal
#head
#body
#legs
#foot

#=======================#
class Pistol():
	def __init__(self, degats, fenetre):

		self.fenetre = fenetre

		self.cadence = 40
		self.compteur_cadence = self.cadence

		self.font = pygame.font.SysFont("Comic Sans MS", 15)

		self.name = "Pistol"
		self.degats = str(degats)
		self.type = "pistol"
		self.nametype = "Pistol"

		self.stats = [self.font.render(self.degats, False, RED), self.font.render(self.nametype, False, RED)]
		self.description = [

		self.font.render(self.name, False, WHITE), 
		self.font.render("Degats = ", False, WHITE),
		self.font.render("Type = ", False, WHITE),
		self.font.render("Despription :", False, WHITE),
		self.font.render("débit faible/faibles dégats", False, WHITE),
		self.font.render("", False, WHITE), 
		self.font.render("Appuyez sur > X < pour ", False, WHITE), 
		self.font.render("Supprimer l'item", False, WHITE)

		]
		
		self.icon = pygame.image.load("res\\items\\weapon\\pistol.png").convert_alpha()
		self.icon = pygame.transform.scale(self.icon, (50, 50))


	def use(self, projectile_list, player):
		projectile_list.add(ProjectileAK(player.rect.x+16, player.rect.y+16, int(self.degats), 10, player.angle, 7, self.fenetre))

class AK():
	def __init__(self, degats, fenetre):

		self.fenetre = fenetre

		self.cadence = 10
		self.compteur_cadence = self.cadence

		self.font = pygame.font.SysFont("Comic Sans MS", 15)
		
		self.name = "AK"
		self.degats = str(degats)
		self.type = "weapon"
		self.nametype = "Fusil"

		self.stats = [self.font.render(self.degats, False, RED), self.font.render(self.nametype, False, RED)]
		self.description = [

		self.font.render(self.name, False, WHITE), 
		self.font.render("Degats = ", False, WHITE),
		self.font.render("Type = ", False, WHITE),
		self.font.render("Despription :", False, WHITE),
		self.font.render("Arme puissante", False, WHITE),
		self.font.render("", False, WHITE), 
		self.font.render("Appuyez sur > X < pour ", False, WHITE), 
		self.font.render("Supprimer l'item", False, WHITE)

		]
		
		self.render = pygame.image.load("res\\items\\weapon\\fusil_topview.png").convert_alpha()
		self.rotate = pygame.transform.rotate(self.render, 0)

		self.icon = pygame.image.load("res\\items\\weapon\\ak.png").convert_alpha()
		self.icon = pygame.transform.scale(self.icon, (50, 50))

	def use(self, projectile_list, player):

		projectile_list.add(ProjectileAK(player.rect.x+16, player.rect.y+16, int(self.degats), 10, player.angle, 7, self.fenetre))

class Bazooka():
	def __init__(self, degats, fenetre):

		self.fenetre = fenetre

		self.cadence = 60
		self.compteur_cadence = self.cadence

		self.font = pygame.font.SysFont("Comic Sans MS", 15)

		self.name = "Bazooka"
		self.degats = str(degats)
		self.type = "special"
		self.nametype = "Bazooka"

		self.stats = [self.font.render(self.degats, False, RED), self.font.render(self.nametype, False, RED)]
		self.description = [

		self.font.render(self.name, False, WHITE), 
		self.font.render("Degats = ", False, WHITE),
		self.font.render("Type = ", False, WHITE),
		self.font.render("Despription :", False, WHITE),
		self.font.render("Faible débit/bons dégats", False, WHITE),
		self.font.render("", False, WHITE), 
		self.font.render("Appuyez sur > X < pour ", False, WHITE), 
		self.font.render("Supprimer l'item", False, WHITE)

		]
		
		self.icon = pygame.image.load("res\\items\\weapon\\bazooka.png").convert_alpha()
		self.icon = pygame.transform.scale(self.icon, (50, 50))
	
	def active(self, projectile_list, player):

		projectile_list.add(ProjectileBazooka(player.rect.x, player.rect.y, int(self.degats), 40, player.angle, 7, self.fenetre))

class Uzi():
	def __init__(self, degats, fenetre):

		self.fenetre = fenetre

		self.cadence = 5
		self.compteur_cadence = self.cadence

		self.font = pygame.font.SysFont("Comic Sans MS", 15)

		self.name = "Uzi"
		self.degats = str(degats)
		self.type = "pistol"
		self.nametype = "Auto"

		self.stats = [self.font.render(self.degats, False, RED), self.font.render(self.nametype, False, RED)]
		self.description = [

		self.font.render(self.name, False, WHITE), 
		self.font.render("Degats = ", False, WHITE),
		self.font.render("Type = ", False, WHITE),
		self.font.render("Despription :", False, WHITE),
		self.font.render("Bon débit/faibles dégats", False, WHITE),
		self.font.render("", False, WHITE), 
		self.font.render("Appuyez sur > X < pour ", False, WHITE), 
		self.font.render("Supprimer l'item", False, WHITE)

		]
		
		self.icon = pygame.image.load("res\\items\\weapon\\uzi.png").convert_alpha()
		self.icon = pygame.transform.scale(self.icon, (50, 50))


	def use(self, projectile_list, player):
		projectile_list.add(ProjectileAK(player.rect.x+16, player.rect.y+16, int(self.degats), 10, player.angle, 7, self.fenetre))

class heal_kit():
	def __init__(self, fenetre):

		self.fenetre = fenetre

		self.font = pygame.font.SysFont("Comic Sans MS", 15)

		self.name = "Medoc"
		self.heal = "maxHP"
		self.type = "heal"
		self.nametype = "heal"

		self.stats = [self.font.render(self.heal, False, RED), self.font.render(self.nametype, False, RED)]
		self.description = [

		self.font.render(self.name, False, WHITE), 
		self.font.render("Heal = ", False, WHITE),
		self.font.render("Type = ", False, WHITE),
		self.font.render("Despription :", False, WHITE),
		self.font.render("Ça soigne un MAX !", False, WHITE),
		self.font.render("", False, WHITE), 
		self.font.render("Appuyez sur > X < pour ", False, WHITE), 
		self.font.render("Supprimer l'item", False, WHITE)

			]

		self.icon = pygame.image.load("res\\items\\heal\\heal_kit.png").convert_alpha()
		self.icon = pygame.transform.scale(self.icon, (50, 50))
	
	def use(self, player, inventory):
		if player.hp != player.maxHP:

			player.hp = player.maxHP
			inventory.slot_heal.remove(self)

class medoc():
	def __init__(self, fenetre):

		self.fenetre = fenetre

		self.font = pygame.font.SysFont("Comic Sans MS", 15)

		self.name = "Medoc"
		self.heal = str(40)
		self.type = "heal"
		self.nametype = "heal"

		self.stats = [self.font.render(self.heal, False, RED), self.font.render(self.nametype, False, RED)]
		self.description = [

		self.font.render(self.name, False, WHITE), 
		self.font.render("Heal = ", False, WHITE),
		self.font.render("Type = ", False, WHITE),
		self.font.render("Despription :", False, WHITE),
		self.font.render("Un peu meilleur qu'un", False, WHITE),
		self.font.render("doliprane", False, WHITE),
		self.font.render("", False, WHITE), 
		self.font.render("Appuyez sur > X < pour ", False, WHITE), 
		self.font.render("Supprimer l'item", False, WHITE)

			]

		self.icon = pygame.image.load("res\\items\\heal\\medoc.png").convert_alpha()
		self.icon = pygame.transform.scale(self.icon, (50, 50))
	
	def use(self, player, inventory):
		if player.hp != player.maxHP:
			player.hp = player.hp + int(self.heal)
	
			if player.hp > player.maxHP:
				player.hp = player.maxHP
	
			inventory.slot_heal.remove(self)

class pills():
	def __init__(self, fenetre):

		self.fenetre = fenetre

		self.font = pygame.font.SysFont("Comic Sans MS", 15)

		self.name = "Medoc"
		self.heal = str(20)
		self.type = "heal"
		self.nametype = "heal"

		self.stats = [self.font.render(self.heal, False, RED), self.font.render(self.nametype, False, RED)]
		self.description = [

		self.font.render(self.name, False, WHITE), 
		self.font.render("Heal = ", False, WHITE),
		self.font.render("Type = ", False, WHITE),
		self.font.render("Despription :", False, WHITE),
		self.font.render("Des pillules avec un", False, WHITE),
		self.font.render("goût amer dégueulasses", False, WHITE),
		self.font.render("", False, WHITE), 
		self.font.render("Appuyez sur > X < pour ", False, WHITE), 
		self.font.render("Supprimer l'item", False, WHITE)

			]

		self.icon = pygame.image.load("res\\items\\heal\\pills.png").convert_alpha()
		self.icon = pygame.transform.scale(self.icon, (50, 50))
	
	def use(self, player, inventory):

		if player.hp != player.maxHP:
			player.hp = player.hp + int(self.heal)
	
			if player.hp > player.maxHP:
				player.hp = player.maxHP
	
			inventory.slot_heal.remove(self)

class syringe():
	def __init__(self, fenetre):

		self.fenetre = fenetre

		self.font = pygame.font.SysFont("Comic Sans MS", 15)

		self.name = "Medoc"
		self.heal = str(100)
		self.type = "heal"
		self.nametype = "heal"

		self.stats = [self.font.render(self.heal, False, RED), self.font.render(self.nametype, False, RED)]
		self.description = [

		self.font.render(self.name, False, WHITE), 
		self.font.render("Heal = ", False, WHITE),
		self.font.render("Type = ", False, WHITE),
		self.font.render("Despription :", False, WHITE),
		self.font.render("Bon remèdes mais il", False, WHITE),
		self.font.render("ne faut pas avoir peur", False, WHITE),		
		self.font.render("des piqûres", False, WHITE),
		self.font.render("", False, WHITE), 
		self.font.render("Appuyez sur > X < pour ", False, WHITE), 
		self.font.render("Supprimer l'item", False, WHITE)

			]

		self.icon = pygame.image.load("res\\items\\heal\\syringe.png").convert_alpha()
		self.icon = pygame.transform.scale(self.icon, (50, 50))
	
	def use(self, player, inventory):

		if player.hp != player.maxHP:
			player.hp = player.hp + int(self.heal)
	
			if player.hp > player.maxHP:
				player.hp = player.maxHP
	
			inventory.slot_heal.remove(self)

class ProjectileAK(pygame.sprite.Sprite):
	def __init__(self, posX, posY, degats, scale, angle, speed, fenetre):
		super().__init__()

		self.fenetre = fenetre

		self.angle = math.radians(90 - angle)
		self.speed = speed/10

		self.degats = degats

		self.animation = []
		self.image = pygame.image.load("res\\items\\bullet\\bullet.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scale, scale))
		self.image = pygame.transform.rotate(self.image, 270-(math.degrees(self.angle)))
		self.animation.append(self.image)

		self.len = len(self.animation)

		self.frame = 0
		self.counter = 0

		self.rect = self.image.get_rect()

		self.rect.x = posX
		self.rect.y = posY

		self.vecteur = 20
		self.velocity_y = None
		self.velocity_x = None

		self.entity_touch = []

	def update(self, entity_list, wall_list):
		
		self.velocity_x = math.cos(self.angle)*20
		self.velocity_y = math.sin(self.angle)*20

		self.rect.x = self.rect.x + (self.velocity_x * self.speed)
		self.rect.y = self.rect.y + (self.velocity_y * self.speed)

		self.fenetre.blit((self.animation[self.frame]), (self.rect))

		if len(self.entity_touch) != 0:
			for entity in self.entity_touch:
				entity.hp = entity.hp - self.degats
				pygame.sprite.Sprite.kill(self)

		collide_wall = pygame.sprite.spritecollide(self, wall_list, False)
		collide_entity = pygame.sprite.spritecollide(self, entity_list, False)

		if len(collide_wall) != 0:
			pygame.sprite.Sprite.kill(self)
	
		if len(collide_entity) != 0:
			self.rect.x = self.rect.x - 32
			self.rect.y = self.rect.y - 32
			
			for entity in collide_entity:
				self.entity_touch.append(entity)

class ProjectileBazooka(pygame.sprite.Sprite):
	def __init__(self, posX, posY, degats, scale, angle, speed, fenetre):
		super().__init__()

		self.fenetre = fenetre

		self.angle = math.radians(90 - angle)
		self.speed = speed/10

		self.degats = degats

		self.animation = []
		self.explosion_animation = []

		self.image = pygame.image.load("res\\items\\bullet\\rocket.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scale, scale))
		self.image = pygame.transform.rotate(self.image, 270-(math.degrees(self.angle)))
		
		self.animation.append(self.image)

		self.explosion = False

		self.image = pygame.image.load("res\\items\\animation\\explosion\\explosion_001.png").convert_alpha()
		self.explosion_animation.append(self.image)
		self.image = pygame.image.load("res\\items\\animation\\explosion\\explosion_002.png").convert_alpha()
		self.explosion_animation.append(self.image)
		self.image = pygame.image.load("res\\items\\animation\\explosion\\explosion_003.png").convert_alpha()
		self.explosion_animation.append(self.image)
		self.image = pygame.image.load("res\\items\\animation\\explosion\\explosion_004.png").convert_alpha()
		self.explosion_animation.append(self.image)
		self.image = pygame.image.load("res\\items\\animation\\explosion\\explosion_005.png").convert_alpha()
		self.explosion_animation.append(self.image)
		self.image = pygame.image.load("res\\items\\animation\\explosion\\explosion_006.png").convert_alpha()
		self.explosion_animation.append(self.image)
		self.image = pygame.image.load("res\\items\\animation\\explosion\\explosion_007.png").convert_alpha()
		self.explosion_animation.append(self.image)
		self.image = pygame.image.load("res\\items\\animation\\explosion\\explosion_008.png").convert_alpha()
		self.explosion_animation.append(self.image)
		self.image = pygame.image.load("res\\items\\animation\\explosion\\explosion_009.png").convert_alpha()
		self.explosion_animation.append(self.image)

		self.len = len(self.animation)

		self.frame = 0
		self.counter = 0

		self.explosion_len = len(self.explosion_animation)

		self.explosion_frame = 0
		self.explosion_counter = 0		

		self.rect = pygame.Rect(0, 16, 32, 32)

		self.rect.x = posX
		self.rect.y = posY
		self.vecteur = 20

		self.velocity_y = None
		self.velocity_x = None

		self.entity_touch = []
		self.degats_made = False

	def update(self, entity_list, wall_list):
		
		if self.explosion == False:
			
			self.velocity_x = math.cos(self.angle)*20
			self.velocity_y = math.sin(self.angle)*20
	
			self.rect.x = self.rect.x + (self.velocity_x * self.speed)
		
			self.rect.y = self.rect.y + (self.velocity_y * self.speed)

			self.fenetre.blit((self.animation[self.frame]), (self.rect.x, self.rect.y))

		if self.explosion == True:
			if self.explosion_counter >= self.speed*5: 
		
				if self.explosion_frame == self.explosion_len:
					pygame.sprite.Sprite.kill(self)

				else: 
					self.explosion_frame = self.explosion_frame + 1

				self.explosion_counter = 1	
		
			else:
				self.explosion_counter = self.explosion_counter + 1	

			self.fenetre.blit(self.explosion_animation[self.explosion_frame - 1], (self.rect.x - 32, self.rect.y - 32))
			
			if self.degats_made == False:
				if self.entity_touch != None:					
					for entity in self.entity_touch:
						entity.hp = entity.hp - self.degats 
				self.degats_made = True
		
		if self.explosion == False:
			
			collide_wall = pygame.sprite.spritecollide(self, wall_list, False)
			collide_entity = pygame.sprite.spritecollide(self, entity_list, False)

			if len(collide_wall) != 0:
				self.explosion = True
				self.rect = pygame.Rect(self.rect.x, self.rect.y, 64, 64)

				self.entity_touch = pygame.sprite.spritecollide(self, entity_list, False)
				
		
			if len(collide_entity) != 0:
				self.explosion = True
				self.rect = pygame.Rect(self.rect.x, self.rect.y, 64, 64)

				self.entity_touch = pygame.sprite.spritecollide(self, entity_list, False)