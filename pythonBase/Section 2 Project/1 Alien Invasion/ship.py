#encoding:utf-8

import pygame

class Ship():
	def __init__(self,screen):
		self.screen = screen
		self.ship_speed = 1
		
		#Load the ship image and get its bounding rectangle
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#Place each new ship in the bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#ship move flag
		self.move_flag_r = False
		self.move_flag_l = False
		
	def blit(self):
		#Draw the ship at the specified location
		self.screen.blit(self.image,self.rect)
	
	def center_ship(self):
		self.center = self.screen_rect.centerx
		
	def update(self):
		if self.move_flag_r and self.rect.right + self.ship_speed <= self.screen_rect.right:
			self.rect.centerx += self.ship_speed
			#print("ship move right[%d]."%(self.rect.centerx))
		if self.move_flag_l and self.rect.left - self.ship_speed >= 0:
			self.rect.centerx -= self.ship_speed
			#print("ship move left[%d]."%(self.rect.centerx))
			
			