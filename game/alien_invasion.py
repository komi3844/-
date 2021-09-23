import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """" Класс для управления ресурсами и поведением игры """

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        ai_settings = Settings()
        screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        pygame.display.set_caption('spac')
        self.ship = Ship(screen)

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            # Отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # При каждом проходе цикла перерисовывается экран.
                #self.screen.fill(ai_settings.bg_color)
                pygame.display.update()
                self.ship.blitme()
                # Отображение последнего прорисованного экрана.
                pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
