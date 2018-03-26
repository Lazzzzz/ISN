import pygame
from item import *
from generator import * 

class Inventory():
	def __init__(self, player, fenetre):
		
		self.fenetre = fenetre
		self.player = player

		self.slot_number = -1
		
		self.inventory_main = []
	
		self.slot_head = []
		self.slot_body = []
		self.slot_legs = []
		self.slot_foot = []	
	
		self.slot_weapon = []
		self.slot_pistol = []
		self.slot_special = []
		self.slot_heal = []

		self.inventory_select = pygame.image.load("res\\gui\\inventory_select.png").convert_alpha()
		self.inventory_select = pygame.transform.scale(self.inventory_select, (64,64))
		
		self.inventory_image = pygame.image.load("res\\gui\\inventory.png").convert_alpha()
		self.inventory_image = pygame.transform.scale(self.inventory_image, (1000, 274))

		self.inventory_health = pygame.image.load("res\\gui\\inventory_health.png").convert() 
		self.inventory_health = pygame.transform.scale(self.inventory_health, (126, 28))

		self.inventory_armor = pygame.image.load("res\\gui\\inventory_armor.png").convert()
		self.inventory_armor = pygame.transform.scale(self.inventory_armor, (126, 28))

		self.inventory_money = pygame.image.load("res\\gui\\inventory_money.png").convert()	
		self.inventory_money = pygame.transform.scale(self.inventory_money, (126, 28))

		self.inventory_money_buy = pygame.image.load("res\\gui\\inventory_money_buy.png").convert()	
		self.inventory_money_buy = pygame.transform.scale(self.inventory_money_buy, (126, 28))

		self.inventory_money_purchased = pygame.image.load("res\\gui\\inventory_money_purchased.png").convert()	
		self.inventory_money_purchased = pygame.transform.scale(self.inventory_money_purchased, (126, 28))

		self.pos = [140, 223]

		self.mouse_posX, self.mouse_posY = pygame.mouse.get_pos()

		self.inventory_open = False

		self.buy = False

		self.font = pygame.font.Font("res\\font\\ZOMBIE.TTF", 30)

		self.player_hp = None
		self.money = 0

		self.chest_price = 100
	
	def addItem(self, item):
		
		if len(self.inventory_main) < 24:
			self.inventory_main.append(item)
		else:
			print("inventaire plein")

	def removeItem(self, item):
		self.inventory_main.remove(item)

	def open(self, chest_list, waveGenerator, player):
			
			#===================> OPEN INVENTORY LOOP <=========================#

		self.inventory_open = True
		self.player_hp = str(player.hp)
		
		while self.inventory_open:

			#====================> CHECK QUIT INVENTORY <====================#

			for event in pygame.event.get():
			
				if event.type == pygame.KEYUP and event.key == pygame.K_e:
					self.buy = False
					self.inventory_open = False
					pygame.mouse.set_visible(False)

			#===================> INITIALISATION <=============================#

			pygame.mouse.set_visible(True)
			
			self.slot_number = -1
			self.mouse_posX, self.mouse_posY = pygame.mouse.get_pos()
			
			self.fenetre.blit(self.inventory_image, (self.pos))
			self.fenetre.blit(self.inventory_health, (204, 303), (0, 0, int((126/100) * int(self.player.hp_100)), 28))
			self.fenetre.blit(self.inventory_armor, (204, 367))
			self.fenetre.blit(self.inventory_money, (204, 431), (0, 0, int((126/100) * int(self.money)), 28))

			for item in self.inventory_main:
								
				if self.slot_number < 24:
					self.slot_number = self.slot_number + 1
				else:
					self.slot_number == -1
				
				if self.slot_number < 6:
					if item != None:
						self.fenetre.blit(item.icon, ((516  + (66 * self.slot_number), 236)))
				
				elif self.slot_number < 12:
					if item != None:
						self.fenetre.blit(item.icon, ((516  + (66 * (self.slot_number - 6)), 302)))					
				
				elif self.slot_number < 18:
					if item != None:
						self.fenetre.blit(item.icon, ((516 + (66 * (self.slot_number - 12)), 368)))					
				
				elif self.slot_number < 24:
					if item != None:
						self.fenetre.blit(item.icon, ((516 + (66 * (self.slot_number - 18)), 434)))

			#=====================> BLIT AND SELECT MAIN INVENTORY <========================#

			if self.mouse_posX >= 254 and self.mouse_posY >= 223 and self.mouse_posX <= 1026 and self.mouse_posY <= 497:
				
				for item in self.inventory_main:
					if self.inventory_main.index(item) < 6:
						if self.mouse_posX >= 506 + (65) * (self.inventory_main.index(item)) and self.mouse_posY >= 223 and self.mouse_posX <= 506 + (65)*(self.inventory_main.index(item)) + 66 and self.mouse_posY <= 289:
							self.fenetre.blit(self.inventory_select, (511 + (66) * (self.inventory_main.index(item)), 228))

							for text in item.stats:
								self.fenetre.blit(text, (1075,255 + item.stats.index(text)*20))

							for text in item.description:
								self.fenetre.blit(text, (955,235 + item.description.index(text)*20))
								
							if pygame.mouse.get_pressed()[0]:
									if item.type == "weapon":
										if len(self.slot_weapon) != 0:
											for block in self.slot_weapon:
												self.inventory_main.append(block)
												self.slot_weapon.remove(block)
									
										self.slot_weapon.append(item)
										self.inventory_main.remove(item)
									
									if item.type == "pistol":
										if len(self.slot_pistol) != 0:
											for block in self.slot_pistol:
												self.inventory_main.append(block)
												self.slot_pistol.remove(block)

										self.slot_pistol.append(item)
										self.inventory_main.remove(item)
			
									if item.type == "special":
										if len(self.slot_special) != 0:
											for block in self.slot_special:
												self.inventory_main.append(block)
												self.slot_special.remove(block)
	
										self.slot_special.append(item)
										self.inventory_main.remove(item)
								
									if item.type == "heal":
										if len(self.slot_heal) != 0:
											for block in self.slot_heal:
												self.inventory_main.append(block)
												self.slot_heal.remove(block)
	
										self.slot_heal.append(item)
										self.inventory_main.remove(item)						
									
									if item.type == "head":
										if len(self.slot_head) != 0:
											for block in self.slot_head:
												self.inventory_main.append(block)
												self.slot_head.remove(block)
	
										self.slot_head.append(item)
										self.inventory_main.remove(item)
			
									if item.type == "body":
										if len(self.slot_body) != 0:
											for block in self.slot_body:
												self.inventory_main.append(block)
												self.slot_body.remove(block)
	
										self.slot_body.append(item)
										self.inventory_main.remove(item)
					
									if item.type == "legs":
										if len(self.slot_legs) != 0:
											for block in self.slot_legs:
												self.inventory_main.append(block)
												self.slot_legs.remove(block)
	
										self.slot_legs.append(item)
										self.inventory_main.remove(item)
								
									if item.type == "foot":
										if len(self.slot_foot) != 0:
											for block in self.slot_foot:
												self.inventory_main.append(block)
												self.slot_foot.remove(block)
	
										self.slot_foot.append(item)
										self.inventory_main.remove(item)

							for event in pygame.event.get():
								if event.type == pygame.KEYUP and event.key == pygame.K_x:
									self.inventory_main.remove(item)

					elif self.inventory_main.index(item) < 12:
							if self.mouse_posX >= 506 + (65) * ((self.inventory_main.index(item) - 6)) and self.mouse_posY >= 296 and self.mouse_posX <= 506 + (65) * ((self.inventory_main.index(item) - 6)) + 66 and self.mouse_posY <= 361:
								self.fenetre.blit(self.inventory_select, (511 + (66) * ((self.inventory_main.index(item) - 6)), 296))
								
								for text in item.stats:
									self.fenetre.blit(text, (1075,255 + item.stats.index(text)*20))
	
								for text in item.description:
									self.fenetre.blit(text, (955,235 + item.description.index(text)*20))
									
								if pygame.mouse.get_pressed()[0]:
									if item.type == "weapon":
										if len(self.slot_weapon) != 0:
											for block in self.slot_weapon:
												self.inventory_main.append(block)
												self.slot_weapon.remove(block)
									
										self.slot_weapon.append(item)
										self.inventory_main.remove(item)
									
									if item.type == "pistol":
										if len(self.slot_pistol) != 0:
											for block in self.slot_pistol:
												self.inventory_main.append(block)
												self.slot_pistol.remove(block)

										self.slot_pistol.append(item)
										self.inventory_main.remove(item)
			
									if item.type == "special":
										if len(self.slot_special) != 0:
											for block in self.slot_special:
												self.inventory_main.append(block)
												self.slot_special.remove(block)
	
										self.slot_special.append(item)
										self.inventory_main.remove(item)
								
									if item.type == "heal":
										if len(self.slot_heal) != 0:
											for block in self.slot_heal:
												self.inventory_main.append(block)
												self.slot_heal.remove(block)
	
										self.slot_heal.append(item)
										self.inventory_main.remove(item)						
									
									if item.type == "head":
										if len(self.slot_head) != 0:
											for block in self.slot_head:
												self.inventory_main.append(block)
												self.slot_head.remove(block)
	
										self.slot_head.append(item)
										self.inventory_main.remove(item)
			
									if item.type == "body":
										if len(self.slot_body) != 0:
											for block in self.slot_body:
												self.inventory_main.append(block)
												self.slot_body.remove(block)
	
										self.slot_body.append(item)
										self.inventory_main.remove(item)
					
									if item.type == "legs":
										if len(self.slot_legs) != 0:
											for block in self.slot_legs:
												self.inventory_main.append(block)
												self.slot_legs.remove(block)
	
										self.slot_legs.append(item)
										self.inventory_main.remove(item)
								
									if item.type == "foot":
										if len(self.slot_foot) != 0:
											for block in self.slot_foot:
												self.inventory_main.append(block)
												self.slot_foot.remove(block)
	
										self.slot_foot.append(item)
										self.inventory_main.remove(item)
							
								for event in pygame.event.get():							
									if event.type == pygame.KEYUP and event.key == pygame.K_x:
										self.inventory_main.remove(item)

					elif self.inventory_main.index(item) < 18:
							if self.mouse_posX >= 506 + (65) * (self.inventory_main.index(item) - 12) and self.mouse_posY >= 361 and self.mouse_posX <= 506 + (65)*(self.inventory_main.index(item) - 12) + 66 and self.mouse_posY <= 434:
								self.fenetre.blit(self.inventory_select, (511 + (66) * (self.inventory_main.index(item) - 12), 361))
							
								for text in item.stats:
									self.fenetre.blit(text, (1075,255 + item.stats.index(text)*20))
	
								for text in item.description:
									self.fenetre.blit(text, (955,235 + item.description.index(text)*20))

								if pygame.mouse.get_pressed()[0]:
									if item.type == "weapon":
										if len(self.slot_weapon) != 0:
											for block in self.slot_weapon:
												self.inventory_main.append(block)
												self.slot_weapon.remove(block)
									
										self.slot_weapon.append(item)
										self.inventory_main.remove(item)
									
									if item.type == "pistol":
										if len(self.slot_pistol) != 0:
											for block in self.slot_pistol:
												self.inventory_main.append(block)
												self.slot_pistol.remove(block)

										self.slot_pistol.append(item)
										self.inventory_main.remove(item)
			
									if item.type == "special":
										if len(self.slot_special) != 0:
											for block in self.slot_special:
												self.inventory_main.append(block)
												self.slot_special.remove(block)
	
										self.slot_special.append(item)
										self.inventory_main.remove(item)
								
									if item.type == "heal":
										if len(self.slot_heal) != 0:
											for block in self.slot_heal:
												self.inventory_main.append(block)
												self.slot_heal.remove(block)
	
										self.slot_heal.append(item)
										self.inventory_main.remove(item)						
									
									if item.type == "head":
										if len(self.slot_head) != 0:
											for block in self.slot_head:
												self.inventory_main.append(block)
												self.slot_head.remove(block)
	
										self.slot_head.append(item)
										self.inventory_main.remove(item)
			
									if item.type == "body":
										if len(self.slot_body) != 0:
											for block in self.slot_body:
												self.inventory_main.append(block)
												self.slot_body.remove(block)
	
										self.slot_body.append(item)
										self.inventory_main.remove(item)
					
									if item.type == "legs":
										if len(self.slot_legs) != 0:
											for block in self.slot_legs:
												self.inventory_main.append(block)
												self.slot_legs.remove(block)
	
										self.slot_legs.append(item)
										self.inventory_main.remove(item)
								
									if item.type == "foot":
										if len(self.slot_foot) != 0:
											for block in self.slot_foot:
												self.inventory_main.append(block)
												self.slot_foot.remove(block)
	
										self.slot_foot.append(item)
										self.inventory_main.remove(item)
								
								for event in pygame.event.get():								
									if event.type == pygame.KEYUP and event.key == pygame.K_x:
										self.inventory_main.remove(item)					
					
					elif self.inventory_main.index(item) < 24:
							if self.mouse_posX >= 506 + (65) * (self.inventory_main.index(item) - 18) and self.mouse_posY >= 428 and self.mouse_posX <= 506 + (65)*(self.inventory_main.index(item) - 18) + 66 and self.mouse_posY <= 506:
								self.fenetre.blit(self.inventory_select, (511 + (66) * (self.inventory_main.index(item) - 18), 428))

								for text in item.stats:
									self.fenetre.blit(text, (1075,255 + item.stats.index(text)*20))
	
								for text in item.description:
									self.fenetre.blit(text, (955,235 + item.description.index(text)*20))
	
								if pygame.mouse.get_pressed()[0]:
									if item.type == "weapon":
										if len(self.slot_weapon) != 0:
											for block in self.slot_weapon:
												self.inventory_main.append(block)
												self.slot_weapon.remove(block)
									
										self.slot_weapon.append(item)
										self.inventory_main.remove(item)
									
									if item.type == "pistol":
										if len(self.slot_pistol) != 0:
											for block in self.slot_pistol:
												self.inventory_main.append(block)
												self.slot_pistol.remove(block)

										self.slot_pistol.append(item)
										self.inventory_main.remove(item)
			
									if item.type == "special":
										if len(self.slot_special) != 0:
											for block in self.slot_special:
												self.inventory_main.append(block)
												self.slot_special.remove(block)
	
										self.slot_special.append(item)
										self.inventory_main.remove(item)
								
									if item.type == "heal":
										if len(self.slot_heal) != 0:
											for block in self.slot_heal:
												self.inventory_main.append(block)
												self.slot_heal.remove(block)
	
										self.slot_heal.append(item)
										self.inventory_main.remove(item)						
									
									if item.type == "head":
										if len(self.slot_head) != 0:
											for block in self.slot_head:
												self.inventory_main.append(block)
												self.slot_head.remove(block)
	
										self.slot_head.append(item)
										self.inventory_main.remove(item)
			
									if item.type == "body":
										if len(self.slot_body) != 0:
											for block in self.slot_body:
												self.inventory_main.append(block)
												self.slot_body.remove(block)
	
										self.slot_body.append(item)
										self.inventory_main.remove(item)
					
									if item.type == "legs":
										if len(self.slot_legs) != 0:
											for block in self.slot_legs:
												self.inventory_main.append(block)
												self.slot_legs.remove(block)
	
										self.slot_legs.append(item)
										self.inventory_main.remove(item)
								
									if item.type == "foot":
										if len(self.slot_foot) != 0:
											for block in self.slot_foot:
												self.inventory_main.append(block)
												self.slot_foot.remove(block)
	
										self.slot_foot.append(item)
										self.inventory_main.remove(item)
								
								for event in pygame.event.get():
									if event.type == pygame.KEYUP and event.key == pygame.K_x:
										self.inventory_main.remove(item)

				
			for chest in chest_list:
				if chest.inventory_open == True:
					if len(chest.inventory) > 0:
						for item in chest.inventory:
						
							self.fenetre.blit(chest.gui, (0,0))
							self.fenetre.blit(item.icon, (10, 660))

						if self.mouse_posX >= 5 and self.mouse_posY >= 650:
							if self.mouse_posX <= 65 and self.mouse_posY <= 715:								
								self.fenetre.blit(self.inventory_select, (4, 652))

								for text in chest.inventory[0].stats:
									self.fenetre.blit(text, (1075,255 + item.stats.index(text)*20))

								for text in chest.inventory[0].description:
									self.fenetre.blit(text, (955,235 + item.description.index(text)*20))

								if len(self.inventory_main) < 24:
									if pygame.mouse.get_pressed()[0]:
										self.addItem(chest.inventory[0])
										
										for item in chest.inventory:
											chest.inventory.remove(item)

										chest.remove()
										self.fenetre.blit(chest.gui, (0,0))	
										
		
			if self.mouse_posX > 204 and self.mouse_posY > 431:
				if self.mouse_posX < 330 and self.mouse_posY < 459:
					if self.money >= 100:
						if self.buy == False:
							self.fenetre.blit(self.inventory_money_buy, (204, 431))
							
							if pygame.mouse.get_pressed()[0]:
								waveGenerator.newChest = True
								self.money = self.money - 100
								self.buy = True
								self.chest_price = self.chest_price + 20
								print(self.chest_price)
						
						else:
							self.fenetre.blit(self.inventory_money_purchased, (204, 431))

					else:
						self.fenetre.blit(self.font.render(str(self.money), False, (0, 0, 0)), (245 ,433))

			#print(self.mouse_posX, self.mouse_posY)
			if self.mouse_posX > 204 and self.mouse_posY > 303:
				if self.mouse_posX < 330 and self.mouse_posY < 332:

					self.fenetre.blit(self.font.render(self.player_hp, False, (0, 0, 0)), (245 ,305))

			#=====================> BLIT PLAYER SLOT <=====================# 
			
			if len(self.slot_weapon) != 0:
				for item in self.slot_weapon:	

					self.fenetre.blit(item.icon, (414, 238))

					if self.mouse_posX >= 410 and self.mouse_posY >= 229 and self.mouse_posX <= 474 and self.mouse_posY <= 293:
						self.fenetre.blit(self.inventory_select, (410, 229))

						for text in item.stats:
							self.fenetre.blit(text, (1075,255 + item.stats.index(text)*20))

						for text in item.description:
							self.fenetre.blit(text, (955,235 + item.description.index(text)*20))

			if len(self.slot_pistol) != 0:
				for item in self.slot_pistol:	

					self.fenetre.blit(item.icon, (414, 304))

					if self.mouse_posX >= 410 and self.mouse_posY >= 295 and self.mouse_posX <= 474 and self.mouse_posY <= 359:
						self.fenetre.blit(self.inventory_select, (410, 295))

						for text in item.stats:
							self.fenetre.blit(text, (1075,255 + item.stats.index(text)*20))

						for text in item.description:
							self.fenetre.blit(text, (955,235 + item.description.index(text)*20))

			if len(self.slot_special) != 0:
				for item in self.slot_special:	

					self.fenetre.blit(item.icon, (414, 370))

					if self.mouse_posX >= 410 and self.mouse_posY >= 361 and self.mouse_posX <= 474 and self.mouse_posY <= 425:
						self.fenetre.blit(self.inventory_select, (410, 361))

						for text in item.stats:
							self.fenetre.blit(text, (1075,255 + item.stats.index(text)*20))

						for text in item.description:
							self.fenetre.blit(text, (955,235 + item.description.index(text)*20))

			if len(self.slot_heal) != 0:
				for item in self.slot_heal:	

					self.fenetre.blit(item.icon, (414, 436))

					if self.mouse_posX >= 410 and self.mouse_posY >= 427 and self.mouse_posX <= 474 and self.mouse_posY <= 491:
						self.fenetre.blit(self.inventory_select, (410, 427))

						for text in item.stats:
							self.fenetre.blit(text, (1075,255 + item.stats.index(text)*20))

						for text in item.description:
							self.fenetre.blit(text, (955,235 + item.description.index(text)*20))

			if len(self.slot_head) != 0:
				for item in self.slot_head:	

					self.fenetre.blit(item.icon, (348, 238))

					if self.mouse_posX >= 344 and self.mouse_posY >= 229 and self.mouse_posX <= 408 and self.mouse_posY <= 293:
						self.fenetre.blit(self.inventory_select, (344, 229))

						for text in item.stats:
							self.fenetre.blit(text, (1075,255 + item.stats.index(text)*20))

						for text in item.description:
							self.fenetre.blit(text, (955,235 + item.description.index(text)*20))

			if len(self.slot_body) != 0:
				for item in self.slot_body:	

					self.fenetre.blit(item.icon, (348, 304))

					if self.mouse_posX >= 344 and self.mouse_posY >= 295 and self.mouse_posX <= 408 and self.mouse_posY <= 359:
						self.fenetre.blit(self.inventory_select, (344, 295))

						for text in item.stats:
							self.fenetre.blit(text, (1075,255 + item.stats.index(text)*20))

						for text in item.description:
							self.fenetre.blit(text, (955,235 + item.description.index(text)*20))

			if len(self.slot_legs) != 0:
				for item in self.slot_legs:	

					self.fenetre.blit(item.icon, (348, 370))

					if self.mouse_posX >= 344 and self.mouse_posY >= 361 and self.mouse_posX <= 408 and self.mouse_posY <= 425:
						self.fenetre.blit(self.inventory_select, (344, 361))

						for text in item.stats:
							self.fenetre.blit(text, (1075,255 + item.stats.index(text)*20))

						for text in item.description:
							self.fenetre.blit(text, (955,235 + item.description.index(text)*20))

			if len(self.slot_foot) != 0:
				for item in self.slot_foot:	

					self.fenetre.blit(item.icon, (348, 436))

					if self.mouse_posX >= 344 and self.mouse_posY >= 427 and self.mouse_posX <= 408 and self.mouse_posY <= 491:
						self.fenetre.blit(self.inventory_select, (344, 427))

						for text in item.stats:
							self.fenetre.blit(text, (1075,255 + item.stats.index(text)*20))

						for text in item.description:
							self.fenetre.blit(text, (955,235 + item.description.index(text)*20))
			
			pygame.display.flip()