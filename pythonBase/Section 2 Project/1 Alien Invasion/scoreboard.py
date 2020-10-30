#encoding:utf-8

import pygame.font

class Scoreboard():
	def __init__(self,ai_settings,screen,status):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.status = status
		
		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None,48)
		
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		
	
	def prep_score(self):
		'''
		round() 让小数精确到小数点后多少位，小数位数由第二个实参指定。
		如果将第二个实参指定为负数，round() 将圆整到最近的10、100、1000等整数倍
		'''
		rounded_score = int(round(self.status.score,-1))
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
		
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
	

	def prep_high_score(self):
		high_score = int(round(self.status.high_score,-1))
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str,True,self.text_color,
				self.ai_settings.bg_color)
				
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top
	
	
	def prep_level(self):
		self.level_image = self.font.render(str(self.status.level),True,
				self.text_color,self.ai_settings.bg_color)
		
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10
		
	def show_score(self):
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.high_score_image,self.high_score_rect)
		self.screen.blit(self.level_image,self.level_rect)