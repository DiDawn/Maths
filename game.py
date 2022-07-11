import pygame
from ath import ATH
import ctypes
from particle import Particle


class Game:
    def __init__(self, display_size, frame_rate):

        # summon the game's window / .set_caption is used to change the name
        pygame.display.set_caption("Math Gym")
        # setting the icon of the window
        icon = pygame.image.load('Assets/the-brain.png')
        pygame.display.set_icon(icon)
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('Assets/the-brain.png')

        # initializing the screen
        self.display_size = display_size

        # initializing the statement of the game
        self.running = True
        self.in_home_menu = True
        self.in_selection_menu = False
        self.in_game = False

        # initializing the component of the game
        self.ath = None
        self.global_ath = None
        self.home_menu = None
        self.selection_menu = None
        self.load_component()

        self.all_particles = pygame.sprite.Group()

        self.spawn_particle('Assets/floating-math-particle1.png')
        self.spawn_particle('Assets/floating-math-particle1.png')
        self.spawn_particle('Assets/floating-math-particle1.png')
        self.spawn_particle('Assets/floating-math-particle1.png')
        self.spawn_particle('Assets/floating-math-particle1.png')
        self.spawn_particle('Assets/floating-math-particle1.png')
        self.spawn_particle('Assets/floating-math-particle1.png')
        self.spawn_particle('Assets/floating-math-particle1.png')
        self.spawn_particle('Assets/floating-math-particle1.png')


    def load_component(self):
        self.ath = ATH(display_size=self.display_size)

        print("loading ... 0%")
        self.global_ath = self.ath.initialize_global_ath()
        print("loading ... 33%")
        self.home_menu = self.ath.initialize_home_menu()
        print("loading ... 66%")
        self.selection_menu = self.ath.initialize_selection_menu()
        print("loading ... 100%")

    def update_screen(self, cursor_pos, screen):
        if self.in_home_menu:
            self.update_home_menu(cursor_pos, screen)
        elif self.in_selection_menu:
            self.update_selection_menu(cursor_pos, screen)

        self.update_global_ath(cursor_pos, screen)

    def update_global_ath(self, cursor_pos, screen):
        if self.global_ath.close_button_rect.collidepoint(cursor_pos):
            screen.blit(self.global_ath.close_button_on, self.global_ath.close_button_rect)
        else:
            screen.blit(self.global_ath.close_button_off, self.global_ath.close_button_rect)

        if self.global_ath.minimize_button_rect.collidepoint(cursor_pos):
            screen.blit(self.global_ath.minimize_button_on, self.global_ath.minimize_button_rect)
        else:
            screen.blit(self.global_ath.minimize_button_off, self.global_ath.minimize_button_rect)

    def update_home_menu(self, cursor_pos, screen):
        screen.blit(self.home_menu.background, (0, 0))

        if self.home_menu.play_button_rect.collidepoint(cursor_pos):
            screen.blit(self.home_menu.play_button_on, self.home_menu.play_button_rect)
        else:
            screen.blit(self.home_menu.play_button_off, self.home_menu.play_button_rect)

    def update_selection_menu(self, cursor_pos, screen):
        screen.blit(self.selection_menu.background, (0, 0))
        screen.blit(self.selection_menu.title, self.selection_menu.title_rect)

        if self.selection_menu.button_multiplication_rect.collidepoint(cursor_pos):
            self.selection_menu.animated_button_multiplication.blit(screen,
                                                                    self.selection_menu.button_multiplication_rect)
            self.selection_menu.animated_button_particles.blit(screen, self.selection_menu.button_particles_rect)
        else:
            screen.blit(self.selection_menu.button_multiplication, self.selection_menu.button_multiplication_rect)
            screen.blit(self.selection_menu.button_particles, self.selection_menu.button_particles_rect)

        if self.selection_menu.button_square_root_rect.collidepoint(cursor_pos):
            self.selection_menu.animated_button_square_root.blit(screen, self.selection_menu.button_square_root_rect)
        else:
            screen.blit(self.selection_menu.button_square_root, self.selection_menu.button_square_root_rect)

        self.update_particles()
        self.all_particles.draw(screen)

    def event_gestion(self, event):

        # detect if the window need to be closed or minimized
        if event.type == pygame.QUIT or\
                (event.type == pygame.MOUSEBUTTONDOWN and self.global_ath.close_button_rect.collidepoint(event.pos)):
            self.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and self.global_ath.minimize_button_rect.collidepoint(event.pos):
            pygame.display.iconify()

        # detect if the player interact with a button:
        elif event.type == pygame.MOUSEBUTTONDOWN and self.home_menu.play_button_rect.collidepoint(event.pos):
            self.in_home_menu = False
            self.in_selection_menu = True

    def spawn_particle(self, image_path):
        self.all_particles.add(Particle(self, image_path=image_path, allow_spinning=True))

    def update_particles(self):
        for particle in self.all_particles:
            particle.move()
