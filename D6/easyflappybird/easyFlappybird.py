import pygame
import random
# import time

pygame.init()
win_w = 1280
win_h = 720
win = pygame.display.set_mode((win_w, win_h))
clock = pygame.time.Clock()

class Bird:
	def __init__(self):
		self.x = win_w * 0.2
		self.y = win_h * 0.5
		#vsp is short for vertical speed
		self.vsp = 0
		self.jumpsp = win_w * 0.0075
		#grv is short for = gravity
		self.grv = win_h * 0.001
		# modify the size of the rectangle
		self.body = pygame.Rect(self.x,self.y,win_h*0.05,win_h*0.05)

	def jump(self):
		self.vsp = -self.jumpsp

	def move(self):
		self.vsp += self.grv
		self.y += self.vsp
		self.body.y = self.y

	def checkfordeath(self,obstacles):
		for obstacle in obstacles:
			if self.y>win_h or self.y < 0 or bird.body.colliderect(obstacle) \
			or bird.body.colliderect(pygame.Rect(
					obstacle.x,
					obstacle.y-win_h*1.25,
					obstacle.width,
					obstacle.height
				)) :
				pygame.quit()

class ObstaclesManager:
	def __init__(self):
		self.obstacles_list = []

	def generateobstacles(self):
		can_gen = True
		for obstacle in self.obstacles_list:
			if obstacle.x > win_w*0.5:			#调障碍物之间的宽度
				can_gen = False
		if can_gen:
			self.obstacles_list.append(
				pygame.Rect(
						win_w,
						random.randint(win_h*0.25,win_h*0.75),	#随机生成障碍物的高度
						win_w*0.1,								#调障碍物的宽度
						win_h
					)
				)

	def scrollscene(self):
		for obstacle in self.obstacles_list:
			obstacle.x -= win_w*0.0075
			if obstacle.x  < -obstacle.width:
				self.obstacles_list.remove(obstacle)
 

manager = ObstaclesManager()
bird = Bird()
game_resumed = False

# time.sleep(10)

while True:
	clock.tick(60)
	win.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				bird.jump()

	manager.generateobstacles()
	manager.scrollscene()
	bird.move()
	bird.checkfordeath(obstacles=manager.obstacles_list)

	pygame.draw.rect(win,(255,255,255), bird.body)
	for obstacle in manager.obstacles_list:
		pygame.draw.rect(win,(255,0,0),obstacle)
		pygame.draw.rect(win,(255,0,0),pygame.Rect(
				obstacle.x,
				obstacle.y - win_h*1.25,
				obstacle.width,
				obstacle.height	
			)
		)
	pygame.display.update()

     