import pygame
import ctypes
from game import Game

ctypes.windll.user32.SetProcessDPIAware()

pygame.init()
display_info = pygame.display.Info()
screen = pygame.display.set_mode((display_info.current_w, display_info.current_h), pygame.FULLSCREEN)
frame_rate = 144
game = Game(display_size=display_info, frame_rate=frame_rate)

running = True
in_home_menu = True
in_selection_menu = False
in_game = False

clock = pygame.time.Clock()
# loop of the game
while game.running:
    # set the fps
    clock.tick(frame_rate)

    # get the events
    for event in pygame.event.get():

        game.event_gestion(event)

    # grab the mouse position
    cursor_position = pygame.mouse.get_pos()
    # apply the modifications to the image
    game.update_screen(cursor_pos=cursor_position, screen=screen)

    # refresh the image with all the modifications
    pygame.display.flip()
