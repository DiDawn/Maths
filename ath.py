import pygame
import pyganim
import ctypes
from math import cos, sin, radians
from random import randint

ctypes.windll.user32.SetProcessDPIAware()


class ATH:

    def __init__(self, display_size):
        self.info_display_size = display_size

    def initialize_global_ath(self):
        return self.GlobalAth(self.info_display_size)

    def initialize_selection_menu(self):
        return self.SelectionMenu(self.info_display_size)

    def initialize_home_menu(self):
        return self.HomeMenu(self.info_display_size)

    class GlobalAth:
        def __init__(self, display_size):
            self.display_size = display_size

            # loading the close buttons
            self.close_button_off = pygame.image.load('Assets/close-button-off3.png')
            self.close_button_on = pygame.image.load('Assets/close-button-on3.png')
            self.close_button_rect = self.close_button_on.get_rect()
            # adjust the position of the button on the screen
            self.close_button_rect.x = int(self.display_size.current_w - self.close_button_rect.w * 1.1)
            self.close_button_rect.y = int(0.1 * self.close_button_rect.h)

            # loading the minimize button
            self.minimize_button_off = pygame.image.load('Assets/minimize-icon-off.png')
            self.minimize_button_on = pygame.image.load('Assets/minimize-icon-on.png')
            self.minimize_button_rect = self.minimize_button_on.get_rect()
            # adjust the position of the button on the screen
            self.minimize_button_rect.x = int(
                self.display_size.current_w - self.minimize_button_rect.w * 1.5 - self.close_button_rect.w)
            self.minimize_button_rect.y = int(0.15 * self.minimize_button_rect.h)

    class HomeMenu:
        def __init__(self, display_size):
            self.display_size = display_size

            # loading the background
            self.background = pygame.image.load('Assets/home-menu-bg.jpg')

            # loading the start buttons
            self.play_button_off = pygame.image.load('Assets/small-start-button-off2.png')
            self.play_button_on = pygame.image.load('Assets/small-start-button-on2.png')
            # play_button = pygame.transform.scale(play_button, (400, 150))
            self.play_button_rect = self.play_button_on.get_rect()
            # adjust the position of the button on the screen
            self.play_button_rect.x = int(self.display_size.current_w / 2 - self.play_button_rect.w / 2)
            self.play_button_rect.y = int(self.display_size.current_h / 5 * 3 + self.play_button_rect.h / 1.5)

    class SelectionMenu:
        def __init__(self, display_size):
            self.display_size = display_size

            # loadin the background
            self.background = pygame.image.load('Assets/background3.2.png')

            # loading the selection_menu_title
            self.title = pygame.image.load('Assets/selection-menu-title.png')
            self.title_rect = self.title.get_rect()
            self.title_rect.x = int(self.display_size.current_w / 2 - self.title_rect.w / 2)
            self.title_rect.y = int(self.display_size.current_h / 5 - self.title_rect.h)

            # loading the selection buttons
            # loading the multiplication button
            self.button_multiplication = pygame.image.load(
                'Assets/game-selection-icon-multiplications-off.png')
            self.animated_button_multiplication = pyganim.PygAnimation(
                [('Assets/game-selection-icon-multiplications-off.png', 750),
                 ('Assets/game-selection-icon4.png', 750)])
            self.animated_button_multiplication.play()
            self.button_multiplication_rect = self.button_multiplication.get_rect()
            self.button_multiplication_rect.x = self.display_size.current_w / 2 - self.button_multiplication_rect.w / 2
            self.button_multiplication_rect.y = self.display_size.current_h / 5 * 2
            # loading the square root button
            self.button_square_root = pygame.image.load(
                'Assets/game-selection-icon-square-root.png')
            self.animated_button_square_root = pyganim.PygAnimation(
                [('Assets/game-selection-icon-square-root.png', 750),
                 ('Assets/game-selection-icon4.png', 750)])
            self.animated_button_square_root.play()
            self.button_square_root_rect = self.button_square_root.get_rect()
            self.button_square_root_rect.x = self.display_size.current_w / 2 - self.button_multiplication_rect.w / 2
            self.button_square_root_rect.y = self.display_size.current_h / 5 * 3

            # loading the particle of the first selection button
            self.button_particles = pygame.image.load('Assets/game-selection-particle-icon.png')
            self.animated_button_particles = pyganim.PygAnimation(
                [('Assets/game-selection-particle-icon.png', 750),
                 ('Assets/game-selection-particle-icon-off.png', 750)])
            self.animated_button_particles.play()
            self.button_particles_rect = self.button_particles.get_rect()
            self.button_particles_rect.x = int(
                self.display_size.current_w / 2 - self.button_multiplication_rect.w * 0.6)
            self.button_particles_rect.y = int(
                self.display_size.current_h / 5 * 2 - self.button_multiplication_rect.h * 0.5)
