import pygame


class Ship():
	"""Класс для управления кораблем."""
	def __init__(self, ai_game):
		"""Инициализирует корабль и задаёт его начальную позицию."""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings

		# Загружает изображение корабля и получает прямоугольник.
		self.image = pygame.image.load('images/ship_5.jpg')
		self.image = pygame.transform.scale(self.image, (210, 140))
		self.image.set_colorkey((255, 255, 255))
		self.rect = self.image.get_rect()

		# Настройки корабля.
		self.ship_speed = 1.5

		# Каждый новый корабль появляется у нижнего края экрана.
		self.rect.midbottom = self.screen_rect.midbottom

		# Сохранение вещественной координаты корабля.
		self.x = float(self.rect.x)

		# Флаги перемещения
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Обновление позоции корабля с учётом флагов."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.ship_speed
		elif self.moving_left and self.rect.x > 0:
			self.x -= self.ship_speed
		self.rect.x = self.x
			
	def blitme(self):
		"""Рисует корабль в текущей позиции"""
		self.screen.blit(self.image, self.rect)