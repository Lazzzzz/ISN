import pygame, math

class Player(pygame.sprite.Sprite):
	def __init__(self, speed, posX, posY, scaleX, scaleY, hp, fenetre):
		super().__init__()

		self.fenetre = fenetre

		self.animation_legs = []
		self.animation_body = []
		self.torso = []

		self.health_image = pygame.image.load("res\\entity\\player\\health\\health.png").convert_alpha()

		self.gui_image = pygame.image.load("res\\gui\\ingame_gui.png").convert_alpha()
		self.gui_select = pygame.image.load("res\\gui\\ingame_gui_select.png").convert_alpha()

		self.maxHP = hp
		self.hp = self.maxHP
		self.hp_100 = None

		self.image = pygame.image.load("res\\entity\\player\\body\\nurse_torso_2h_weapon.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.torso.append(self.image)

		self.image = pygame.image.load("res\\entity\\player\\body\\nurse_torso_2h_pistol.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.torso.append(self.image)

		self.image = pygame.image.load("res\\entity\\player\\body\\nurse_torso_2h_special.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.torso.append(self.image)

		self.image = pygame.image.load("res\\entity\\player\\body\\nurse_torso_2h_heal.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.torso.append(self.image)

		self.image = pygame.image.load("res\\entity\\player\\body\\nurse_torso_2h.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.torso.append(self.image)

		self.image = pygame.image.load("res\\entity\\player\\legs\\nurse_legs_0001.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation_legs.append(self.image)
		
		self.image = pygame.image.load("res\\entity\\player\\legs\\nurse_legs_0002.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation_legs.append(self.image)
	
		self.image = pygame.image.load("res\\entity\\player\\legs\\nurse_legs_0003.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation_legs.append(self.image)
		
		self.image = pygame.image.load("res\\entity\\player\\legs\\nurse_legs_0004.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation_legs.append(self.image)

		self.rect = pygame.Rect(32, 32, 32, 32)
	
		self.rect.x = posX
		self.rect.y = posY

		self.len_legs = len(self.animation_legs)

		self.nude = None

		self.frame_legs = 1

		self.counter_legs = 0
		
		self.speed = speed
		self.mposX, self.mposY = pygame.mouse.get_pos()

		self.dist = None
		self.delta_x = None
		self.delta_y = None
		self.rotate_image_legs = None
		self.rotate_image_body = None

		self.projectile_list = pygame.sprite.Group()
		self.special_list = pygame.sprite.Group()

		self.velocity_x = 0
		self.velocity_y = 0

		self.inventory = None
		self.select_slot = 0
		self.select_posX = 93
		self.select_posY = 650

		self.itemSlot_weapon = False
		self.itemSlot_pistol = False
		self.itemSlot_special = False
		self.itemSlot_heal = False

	def goLeft(self, velocity):
		self.velocity_x = -velocity
	
	def goRight(self, velocity):
		self.velocity_x = velocity
	
	def goUp(self, velocity ):
		self.velocity_y = -velocity
	
	def goDown(self, velocity):	
		self.velocity_y = velocity
	
	def stop(self):
		self.velocity_x = 0
		self.velocity_y = 0

	def selectSlot(self, slot):
		self.select_slot = slot

		if self.select_slot == 0:
			self.select_posX = 93
			self.select_posY = 650
	
		if self.select_slot == 1:
			self.select_posX = 159
			self.select_posY = 650
		
		if self.select_slot == 2:
			self.select_posX = 225
			self.select_posY = 650
	
		if self.select_slot == 3:
			self.select_posX = 291
			self.select_posY = 650
	
	def use(self, inventory):
		self.inventory = inventory

		if self.select_slot == 0:
			if len(self.inventory.slot_weapon) != None:

				for item in self.inventory.slot_weapon:
					if item.compteur_cadence == 0:
						item.use(self.projectile_list, self)
						item.compteur_cadence = item.cadence

		if self.select_slot == 1:
			if len(self.inventory.slot_pistol) != None:
				for item in self.inventory.slot_pistol:
					if item.compteur_cadence == 0:
	
						item.use(self.projectile_list, self)
						item.compteur_cadence = item.cadence
		
		if self.select_slot == 2:			
			if len(self.inventory.slot_special) != None:
				
				for item in self.inventory.slot_special:
					if item.compteur_cadence == 0:
						item.active(self.projectile_list, self)
						item.compteur_cadence = item.cadence

		if self.select_slot == 3:	
			if len(self.inventory.slot_heal) != None:
				for item in self.inventory.slot_heal:
	
						item.use(self, self.inventory)
					
	def update(self, wall_list, entity_list, maploader):

		if self.inventory != None:
			if len(self.inventory.slot_weapon) != None:
				for item in self.inventory.slot_weapon:
					if item.compteur_cadence != 0:

						item.compteur_cadence = item.compteur_cadence - 1

			if len(self.inventory.slot_pistol) != None:
				for item in self.inventory.slot_pistol:
					if item.compteur_cadence != 0:

						item.compteur_cadence = item.compteur_cadence - 1

			if len(self.inventory.slot_special) != None:
				for item in self.inventory.slot_special:
					if item.compteur_cadence != 0:

						item.compteur_cadence = item.compteur_cadence - 1

		self.rect.x = self.rect.x + self.velocity_x
		collide_wall = pygame.sprite.spritecollide(self, wall_list, False)
		
		for block in collide_wall:

			if self.velocity_x > 0:
				self.rect.right = block.rect.left
			
			if self.velocity_x < 0:
				self.rect.left = block.rect.right
		
		self.rect.y = self.rect.y + self.velocity_y
		
		collide_wall = pygame.sprite.spritecollide(self, wall_list, False)
		
		for block in collide_wall:

			if self.velocity_y > 0:
				self.rect.bottom = block.rect.top
			
			if self.velocity_y < 0:
				self.rect.top = block.rect.bottom
		
		self.mposX, self.mposY = pygame.mouse.get_pos()

		if self.counter_legs == self.speed: 
		
			if self.frame_legs == self.len_legs:
				self.frame_legs = 1
			else: 
				self.frame_legs = self.frame_legs + 1

			self.counter_legs = 1
		
		else:
			self.counter_legs = self.counter_legs + 1

		self.delta_x = self.mposX - self.rect.x
		self.delta_y = self.mposY - self.rect.y

		self.dist = math.hypot(self.delta_x, self.delta_y)

		if self.delta_x > 0 and self.delta_y > 0:
			self.angle = math.degrees(math.acos(abs(self.delta_y / self.dist)))
		
		elif self.delta_x < 0 and self.delta_y > 0:
			self.angle = 360 - math.degrees(math.asin(abs(self.delta_x / self.dist)))

		elif self.delta_x < 0 and self.delta_y < 0:
			self.angle = 180 + math.degrees(math.acos(abs(self.delta_y / self.dist)))

		elif self.delta_x > 0 and self.delta_y < 0:		
			self.angle = 180 - math.degrees(math.asin(abs(self.delta_x / self.dist)))

		self.itemSlot_weapon = False			
		self.itemSlot_pistol = False
		self.itemSlot_special = False
		self.itemSlot_heal = False

		for item in self.inventory.slot_weapon:
			self.itemSlot_weapon = True
		
		for item in self.inventory.slot_pistol:
			self.itemSlot_pistol = True

		for item in self.inventory.slot_special:
			self.itemSlot_special = True

		for item in self.inventory.slot_heal:
			self.itemSlot_heal = True

		self.rotate_image_legs = pygame.transform.rotate(self.animation_legs[self.frame_legs - 1], self.angle)

		if self.itemSlot_weapon == True or self.itemSlot_pistol == True or self.itemSlot_special == True or self.itemSlot_heal == True:
			self.rotate_image_body = pygame.transform.rotate(self.torso[self.select_slot], self.angle)
		
		elif self.itemSlot_weapon == False and self.itemSlot_pistol == False and self.itemSlot_special == False and self.itemSlot_heal == False:
			self.rotate_image_body = pygame.transform.rotate(self.torso[4], self.angle)

		self.hp_100 = (100 / self.maxHP) * self.hp
		
		"""
		self.slot_head = []
		self.slot_body = []
		self.slot_legs = []
		self.slot_foot = []	
	
		self.slot_weapon = []	--- FAIT
		self.slot_pistol = []	--- FAIT
		self.slot_special = []		--- FAIT
		self.slot_heal = []		--- FAIT
		"""
		 
		self.fenetre.blit(self.gui_image, (0, 0))

		if len(self.inventory.slot_weapon) == 1:
			for item in self.inventory.slot_weapon:
				self.fenetre.blit(item.icon, (98,656))				

		if len(self.inventory.slot_pistol) == 1:
			for item in self.inventory.slot_pistol:
				self.fenetre.blit(item.icon, (166,656))	

		if len(self.inventory.slot_special) == 1:
			for item in self.inventory.slot_special:
				self.fenetre.blit(item.icon, (232,656))	

		if len(self.inventory.slot_heal) == 1:
			for item in self.inventory.slot_heal:
				self.fenetre.blit(item.icon, (298,656))	

		self.fenetre.blit(self.gui_select, (self.select_posX, self.select_posY))
		self.fenetre.blit(self.health_image, (self.rect.x, self.rect.y - 15), (0, 0, int((64/100) * self.hp_100), 8))
		self.fenetre.blit(self.rotate_image_legs, (self.rect.x - 16, self.rect.y - 16))
		self.fenetre.blit(self.rotate_image_body, (self.rect.x - 16, self.rect.y - 16))

