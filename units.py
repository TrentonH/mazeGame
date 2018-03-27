__author__ = 'Trenton'
import pygame

import graphics

pygame.init()
space = pygame.mixer.music.load('Spacetime.mp3')
pygame.mixer.music.play(-1)

foot = pygame.mixer.Sound('Footsteps2.wav')


class unit(object):
	def __init__(self, x, y):
			self.x = x
			self.y = y
			self.frame = 0.0

class George(unit):
	def __init__(self, x, y):
		super(George, self).__init__(x, y)
		self.spritesheet = graphics.load("trainer.png")
		self.mapping = {
			"down" : [(46.75  * i , 0, 46.75 ,64) for i in range(4)],
			"left" : [(46.75 * i , 65, 46.75 ,64) for i in range(4)],
			"right": [(46.75 * i ,  128, 46.75 ,64) for i in range(4)],
			"up"   : [(46.75 * i , 192, 46.75 ,64) for i in range(4)],
			"s_down" : [(0, 0, 46.75 ,64) for i in range(4)],
			"s_left" : [(0, 65, 46.75 ,64) for i in range(4)],
			"s_right": [(0,  128, 46.75 ,64) for i in range(4)],
			"s_up"   : [(0, 192, 46.75 ,64) for i in range(4)]
		}
		self.facing = "down"
		self.speed = 0.3

	def update(self):
		self.frame = (self.frame + self.speed) % 4

	def render(self, surface):
		surface.blit(self.spritesheet,
		             (self.x, self.y, 46.75,64),
		             self.mapping[self.facing][int(self.frame)])

	def handler(self, event):
		if event.type == pygame.KEYDOWN:
			foot.play()


			if event.key == pygame.K_UP:
				self.facing = "up"
				self.y -= 2

				if self.y < 0:
					self.y = 0
			elif event.key == pygame.K_DOWN:
				self.facing = "down"
				self.y += 2

				if self.y > (599 - 48):
					self.y = 599 - 48
			elif event.key == pygame.K_LEFT:
				self.facing = "left"
				self.x -= 2

				if self.x < 0:
					self.x = 0
			elif event.key == pygame.K_RIGHT:
				self.facing = "right"
				self.x += 2

				if self.x > (799 - 48):
					self.x = 799 - 48
		if event.type == pygame.KEYUP:
			foot.stop()
			if event.key == pygame.K_UP:
				self.facing = "s_up"
				if self.y < 0:
					self.y = 0
			elif event.key == pygame.K_DOWN:
				self.facing = "s_down"
				if self.y > (599 - 48):
					self.y = 599 - 48
			elif event.key == pygame.K_LEFT:
				self.facing = "s_left"
				if self.x < 0:
					self.x = 0
			elif event.key == pygame.K_RIGHT:
				self.facing = "s_right"
				if self.x > (799 - 48):
					self.x = 799 - 48
