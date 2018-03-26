import pygame
from inventory import *
from player import *

class LoadBar():
	def __init__(self, posX, posY, elements, fenetre):
		
		self.fenetre = fenetre

		self.posX = posX
		self.posY = posY

		self.load_bar_empty = pygame.image.load("res\\menu\\load_bar_empty.png").convert_alpha()
		self.load_bar_full = pygame.image.load("res\\menu\\load_bar_full.png").convert_alpha()

		self.counter = 0

		self.elements = elements

		self.done = False

		self.font = pygame.font.Font("res\\font\\ZOMBIE.TTF", 30)

		self.fenetre.blit(self.load_bar_empty, (self.posX, self.posY))
		
		self.text = None
		self.text_rect = None

	def next(self, text):
			
			self.fenetre.fill((0,0,0))
			
			self.text = self.font.render(str(text), True, (255, 255, 255))
			self.text_rect = self.text.get_rect(center=(self.posX + 360/2, self.posY + 100))

			self.fenetre.blit(self.load_bar_empty, (self.posX, self.posY))
			self.fenetre.blit(self.text, self.text_rect)
			
			self.counter = self.counter + 1
			self.fenetre.blit(self.load_bar_full, (self.posX, self.posY), (0,0, int((360 / self.elements) * self.counter) ,36))
			pygame.display.flip()

class Menu():
	def __init__(self, fenetre):
		self.fenetre = fenetre
		
		self.background = pygame.image.load("res\\menu\\background_main_menu.png").convert()
		self.selector_play = pygame.image.load("res\\menu\\background_main_play.png").convert()
		self.selector_quit = pygame.image.load("res\\menu\\background_main_quit.png").convert()

		self.mouse_posX, self.mouse_posY = pygame.mouse.get_pos()

		self.done = False
		self.quit = False

		self.player = None
		self.inventory = None
		self.injection = None

		self.loadBar = LoadBar(460, 342, 3, fenetre)

	def setPlayer(self, fenetre):

		self.player = Player(4, 560, 260, 64, 64, 150, fenetre)

		self.inventory = Inventory(self.player, fenetre)
		self.player.inventory = self.inventory

	def setMap(self, wall_list, maploader):
		
		self.waveGenerator = WaveGenerator(wall_list, maploader, self.fenetre)
		self.spawn_point = self.waveGenerator.spawn_point
		self.spawn_chest = self.waveGenerator.spawn_chest

	def update(self, maploader):
		
		self.mouse_posX, self.mouse_posY = pygame.mouse.get_pos()
		self.fenetre.blit(self.background, (0,0))

		if self.mouse_posX > 45 and self.mouse_posY > 385:
			if self.mouse_posX < 255 and self.mouse_posY < 486:

				self.fenetre.blit(self.selector_play, (0, 0))

				if pygame.mouse.get_pressed()[0]:
					
					self.fenetre.fill((0,0,0))
					self.loadBar.next("randomMap")

					maploader.randomMap()
					
					self.wall_list = maploader.wall_list
					
					self.setPlayer(self.fenetre)
					self.setMap(self.wall_list, maploader)

					self.loadBar.next("injection")

					self.done = True
					self.injection = False
		
					self.loadBar.next("finish")

		print(self.mouse_posX, self.mouse_posY)

		if self.mouse_posX > 45 and self.mouse_posY > 524:
			if self.mouse_posX < 278 and self.mouse_posY < 632:

				self.fenetre.blit(self.selector_quit, (0, 0))

				if pygame.mouse.get_pressed()[0]:
					self.done = True
					self.quit = True
					
		pygame.display.flip()

class PauseMenu():
	def __init__(self, fenetre):

		self.fenetre = fenetre

		self.image = pygame.image.load("res\\menu\\pauseMenu.png")

		self.mouse_posX, self.mouse_posY = pygame.mouse.get_pos()

		self.done = False
		self.finish = False

	def update(self):

		self.done = False
		self.finish = False		
		
		while not self.done:

			for event in pygame.event.get():
				if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
					self.done = True
					self.finish = False


			self.mouse_posX, self.mouse_posY = pygame.mouse.get_pos()

			self.fenetre.blit(self.image, (480,330))

			if self.mouse_posX > 480 and self.mouse_posY > 330:
				if self.mouse_posX < 781 and self.mouse_posY < 394:
					if pygame.mouse.get_pressed()[0]:
						self.done = True
						self.finish = True


			pygame.display.flip()
