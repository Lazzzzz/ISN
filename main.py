#Changelog
#main - generator - zombie - inventory - player - item

try:
	import pygame
	from zombieBasic import *
	from ghost import *
	from animation import *
	from inventory import *
	from player import *
	from generator import *
	from level import *
	from menu import *

except ImportError:
	print("Impossible de charger un module")

print("Initialisation...")

pygame.init()
pygame.font.init()

taille = [1280, 720]

fenetre = pygame.display.set_mode((taille), pygame.FULLSCREEN)
pygame.key.set_repeat(30,0)
pygame.display.set_caption('zombie')
pygame.mouse.set_visible(True)

loadBar = LoadBar(460, 342, 4, fenetre)

loadBar.next("clock")

clock = pygame.time.Clock()
done = True
counter = 0

loadBar.next("level")

font = pygame.font.SysFont("Comic Sans MS", 30)

texture = Texture(64,64)

maploader = MapLoader(fenetre)
maploader.addMap(levelTest())
#maploader.addMap(level1())

loadBar.next("menu")

entity_list = pygame.sprite.Group()
chest_list = pygame.sprite.Group()

quit = False

menu = Menu(fenetre)
pauseMenu = PauseMenu(fenetre)

loadBar.next("finish")

print("chargement finis en : " +  str(pygame.time.get_ticks()/1000) + " secondes")

while not quit:
	
	if menu.injection == False:

		waveGenerator = menu.waveGenerator

		player = menu.player
		inventory = menu.inventory

		wall_list = menu.wall_list

		spawn_point = menu.spawn_point
		spawn_chest = menu.spawn_chest

		menu.injection = True
		done = False

		chest_list.add(Chest(player.rect.x , player.rect.y, Pistol(6, fenetre), fenetre))
	
	while not menu.done:
		for event in pygame.event.get():
		
			if event.type == pygame.QUIT:
				menu.done = True
				menu.quit = True

		menu.update(maploader)
		clock.tick(60)

	quit = menu.quit

	while not done:

		fenetre.fill((0,0,0))
		fenetre.blit(maploader.level.map , (maploader.posX, maploader.posY))

		maploader.chunkUpdate(player, entity_list, player.projectile_list, chest_list, spawn_point, spawn_chest)

		entity_list.update(texture, player, wall_list, entity_list)
		player.projectile_list.update(entity_list, wall_list)

		chest_list.update(player)

		player.update(wall_list, entity_list, maploader)
		player.special_list.update()
		
		maploader.miniMap(player, entity_list, chest_list, waveGenerator)

		waveGenerator.update(texture, wall_list, entity_list, chest_list, spawn_point, maploader, player)
		
		FPS = font.render((str(int(clock.get_fps()))), False, (255,0,0))
		fenetre.blit(FPS , (10,10))

		pygame.display.flip()
		clock.tick(60)

		if pygame.mouse.get_pressed()[0]:
			player.use(inventory)

		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				done = True
				quit = True

			if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
					
				pauseMenu.update()

				if pauseMenu.finish == True:

					done = True
					menu.done = False

					waveGenerator = None

					player = None
					inventory = None

					spawn_point = None
					spawn_chest = None

					entity_list.empty()
					chest_list.empty()
					wall_list.empty()
					
					maploader.posX = 64
					maploader.posY = 64

			if event.type == pygame.KEYUP and event.key == pygame.K_e:
				inventory.open(chest_list, waveGenerator, player)
			
			if event.type == pygame.KEYDOWN:
				
				if event.key == pygame.K_LEFT or event.key == pygame.K_a:
					player.goLeft(4)
				
				if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					player.goRight(4)
				
				if event.key == pygame.K_UP or event.key == pygame.K_w:
					player.goUp(4)
				
				if event.key == pygame.K_DOWN or event.key == pygame.K_s:
					player.goDown(4)
				
				if event.key == pygame.K_1:
					player.selectSlot(0)
				
				if event.key == pygame.K_2:
					player.selectSlot(1)
				
				if event.key == pygame.K_3:
					player.selectSlot(2)
				
				if event.key == pygame.K_4:
					player.selectSlot(3)
		
			if event.type == pygame.KEYUP:
				
				if event.key == pygame.K_LEFT or event.key == pygame.K_a:
					player.stop()
				
				if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					player.stop()
				
				if event.key == pygame.K_UP or event.key == pygame.K_w:
					player.stop()
				
				if event.key == pygame.K_DOWN or event.key == pygame.K_s:
					player.stop()

pygame.quit()
