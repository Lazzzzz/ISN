import pygame

class fire():
	def __init__(self, speed, scaleX, scaleY, fenetre):
		
		self.fenetre = fenetre

		self.animation = []

		self.image = pygame.image.load("res\\fire\\onfire_0001.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY/8))
		self.animation.append(self.image)
		
		self.image = pygame.image.load("res\\fire\\onfire_0002.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation.append(self.image)
	
		self.image = pygame.image.load("res\\fire\\onfire_0003.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation.append(self.image)
		
		self.image = pygame.image.load("res\\fire\\onfire_0004.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation.append(self.image)
		
		self.image = pygame.image.load("res\\fire\\onfire_0005.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation.append(self.image)
		
		self.image = pygame.image.load("res\\fire\\onfire_0006.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation.append(self.image)
		
		self.image = pygame.image.load("res\\fire\\onfire_0007.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation.append(self.image)
		
		self.image = pygame.image.load("res\\fire\\onfire_0008.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation.append(self.image)
		
		self.image = pygame.image.load("res\\fire\\onfire_0009.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
		self.animation.append(self.image)
	
		self.posX = None
		self.posY = None

		self.len = len(self.animation)

		self.frame = 1

		self.counter = 1
		self.speed = speed

	def move(self, posX, posY):
		
		self.posX = posX
		self.posY = posY

	def update(self):

		if self.counter == self.speed: 
		
			if self.frame == self.len:
				self.frame = 1
			else: 
				self.frame = self.frame + 1

			self.counter = 1	
		
		else:
			self.counter = self.counter + 1	
			
		self.fenetre.blit(self.animation[self.frame - 1], (self.posX, self.posY))