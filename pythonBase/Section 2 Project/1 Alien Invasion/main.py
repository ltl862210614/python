#! python3
#encoding:utf-8

import sys
from time import sleep
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_status import GameStatus
from button import Button
from scoreboard import Scoreboard

def check_play_button(ai_settings,screen,status,play_button,ship,aliens,
		bullets,mouse_x,mouse_y):
	if play_button.rect.collidepoint(mouse_x,mouse_y) and not status.game_active:
		ai_settings.initialize_dynamic_settings()
		#Hide cursor
		pygame.mouse.set_visible(False)
		
		status.reset_status()
		status.game_active = True
		
		aliens.empty()
		bullets.empty()
		
		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()
		
def check_events(ai_settings,screen,status,play_button,ship,aliens,bullets):
	#Listen to keyboard and mouse events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("quit.")
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings,screen,status,play_button,ship,aliens,bullets,mouse_x,mouse_y)
		elif event.type == pygame.KEYDOWN:
			print("keydown:")
			if event.key == pygame.K_RIGHT:
				print("move right start:")
				ship.move_flag_r = True
			elif event.key == pygame.K_LEFT:
				print("move left start:")
				ship.move_flag_l = True
			elif event.key == pygame.K_SPACE:
				if len(bullets)<ai_settings.bullets_allowed:
					new_bullet = Bullet(ai_settings,screen,ship)
					bullets.add(new_bullet)
			elif event.key == pygame.K_q:
				sys.exit()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				ship.move_flag_r = False
			elif event.key == pygame.K_LEFT:
				ship.move_flag_l = False

def get_number_aliens_x(ai_settings,alien_width):
	avaliable_space_x = ai_settings.screen_width - 2*alien_width
	number_aliens_x = int(avaliable_space_x / (2*alien_width))
	return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
	avaliable_space_y = ai_settings.screen_height - (3*alien_height) - ship_height
	number_rows = int(avaliable_space_y / (2*alien_height))
	return number_rows
	
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2*alien_width*alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
	aliens.add(alien)
	
def create_fleet(ai_settings,screen,ship,aliens):
	alien = Alien(ai_settings,screen)
	number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
	number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings,screen,aliens,alien_number,row_number)

def change_fleet_direction(ai_settings,aliens):
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def check_fleet_edges(ai_settings,aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break	

def ship_hit(ai_settings,status,screen,ship,aliens,bullets):
	if status.ships_left > 0:
		status.ships_left -= 1
		
		aliens.empty()
		bullets.empty()
		
		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()
		
		sleep(0.5)
	else:
		status.game_active = False
		pygame.mouse.set_visible(True)
	
def check_aliens_bottom(ai_settings,status,screen,ship,aliens,bullets):
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings,status,screen,ship,aliens,bullets)
			break
		
def update_aliens(ai_settings,status,screen,ship,aliens,bullets):
	check_fleet_edges(ai_settings,aliens)
	aliens.update()
	
	#detect collisions between aliens and ship 
	if pygame.sprite.spritecollideany(ship,aliens):
		print("ship hit!")
		ship_hit(ai_settings,status,screen,ship,aliens,bullets)
		
	check_aliens_bottom(ai_settings,status,screen,ship,aliens,bullets)

def check_bullet_alien_collosions(ai_settings,screen,status,score,ship,aliens,bullets):
	#delete alien and bullet to collide
	collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
	if collisions:
		#与每颗子弹相关的值都是一个列表
		for alien in collisions.values():
			status.score += ai_settings.alien_points*len(alien)
			score.prep_score()
		check_high_score(status,score)
	
	if len(aliens) == 0:
		bullets.empty()
		ai_settings.increase_speed()
		create_fleet(ai_settings,screen,ship,aliens)
		
		status.level += 1
		score.prep_level()

def check_high_score(status,score):
	if status.score > status.high_score:
		status.high_score = status.score
		score.prep_high_score()
		
def update_bullets(ai_settings,screen,status,score,ship,aliens,bullets):
	bullets.update()
	#delete disappear bullets
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	
	check_bullet_alien_collosions(ai_settings,screen,status,score,ship,aliens,bullets)
			
def update_screen(ai_settings,screen,status,score,ship,aliens,bullets,play_button):	
	screen.fill(ai_settings.bg_color)
	#draw a ship
	ship.blit()
	score.show_score()
	#draw aliens
	aliens.draw(screen)
	#draw bullets
	for bullet in bullets.sprites():
		bullet.draw_bullet()
		
	if not status.game_active:
		play_button.draw_button()
		
	#Make the recently drawn screen visible
	pygame.display.flip()
	
def run_game():
	ai_settings = Settings()
	#Initialize the game and create a screen object
	pygame.init()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption(ai_settings.caption)

	play_button = Button(ai_settings,screen,"Play")
	status = GameStatus(ai_settings)
	
	score = Scoreboard(ai_settings,screen,status)
	#create a ship
	ship = Ship(screen)
	
	#create a group to store bullets
	bullets = Group()
	#create a group to store aliens
	aliens = Group()
	
	create_fleet(ai_settings,screen,ship,aliens)
	
	#Start the main loop of the game
	while True:		
		check_events(ai_settings,screen,status,play_button,ship,aliens,bullets)
		if status.game_active:
			ship.update()	
			update_bullets(ai_settings,screen,status,score,ship,aliens,bullets)
			update_aliens(ai_settings,status,screen,ship,aliens,bullets)
		
		update_screen(ai_settings,screen,status,score,ship,aliens,bullets,play_button)
		
run_game()