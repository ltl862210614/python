#encoding:utf-8

import pygame
#通过使用精灵，可将游戏中相关的元素编组
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self,ai_setting,screen,ship):
		super(Bullet,self).__init__()	#python2.7
		#super().__init__()
		self.screen = screen
		
		self.rect = pygame.Rect(0,0,ai_setting.bullet_width,ai_setting.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		self.y = float(self.rect.y)
		print("ship[%d %d],bullet[%d %d]"%(ship.rect.top,ship.rect.centerx,self.rect.top,self.rect.centerx))
		self.bullet_color = ai_setting.bullet_color
		self.bullet_speed = ai_setting.bullet_speed
		
	def update(self):
		self.y -= self.bullet_speed
		self.rect.y = self.y
		
	def draw_bullet(self):
		pygame.draw.rect(self.screen,self.bullet_color,self.rect)
		

		
		