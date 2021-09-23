import pygame


class Ship():
    """Класс для управления кораблем."""

    def __init__(self, screen):
        """Инициализирует корабль и задает его начальную позицию."""

        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
