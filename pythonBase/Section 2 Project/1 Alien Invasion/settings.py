#! python3
#encoding:utf-8

class Settings():
	def __init__(self):
		self.caption = "Alien Invasion"
		self.screen_width = 1200
		self.screen_height = 800
		#background color
		self.bg_color = (255,255,255)#(230,230,230)
		
		#bullet setting
		self.bullet_speed = 10
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 0,0,255
		self.bullets_allowed = 10
		
		#alien setting
		self.alien_speed = 1
		self.fleet_drop_speed = 10
		#fleet_direction = 1,move right; -1,move left
		self.fleet_direction = 1
		
		#ship setting
		self.ship_speed = 1
		self.ship_limit = 3
		
		self.speedup_scale = 1.1
		self.initialize_dynamic_settings()
		
		self.score_scale = 1.5
		
	def initialize_dynamic_settings(self):
		self.ship_speed = 1
		self.bullet_speed = 10
		self.alien_speed = 1
		
		self.fleet_direction = 1
		
		self.alien_points = 50
		
		
	def increase_speed(self):
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		
		self.alien_points = int(self.alien_points*self.score_scale)
		print(self.alien_points)
		
		