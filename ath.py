import pygame
import pyganim
import ctypes

ctypes.windll.user32.SetProcessDPIAware()


class ATH:

    class SelectionButtons:
        def __init__(self):
            self.info_display_size = pygame.display.Info()

            self.selection_button_multiplication = pygame.image.load('Assets/game-selection-icon-multiplications-off.png')
            self.animated_selection_button_multiplication = pyganim.PygAnimation([('Assets/game-selection-icon-multiplications-off.png', 750),
                                                                              ('Assets/game-selection-icon4.png', 750)])
            self.animated_selection_button_multiplication.play()
            self.selection_button_multiplication_rect = self.selection_button_multiplication.get_rect()
            self.selection_button_multiplication_rect.x = self.info_display_size.current_w/2 - self.selection_button_multiplication_rect.w/2
            self.selection_button_multiplication_rect.y = self.info_display_size.current_h/5*2
