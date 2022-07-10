import pygame
import pyganim
import ctypes
from ath import ATH

ctypes.windll.user32.SetProcessDPIAware()

pygame.init()

# initialisation of pygame module
pygame.init()

# summon the game's window / .set_caption is used to change the name
pygame.display.set_caption("Math Gym")
# setting the icon of the window
icon = pygame.image.load('Assets/the-brain.png')
pygame.display.set_icon(icon)
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('Assets/the-brain.png')

# height and width of the window
info_display_size = pygame.display.Info()
screen = pygame.display.set_mode((info_display_size.current_w, info_display_size.current_h), pygame.FULLSCREEN)

# loading the backgrounds
home_menu_background = pygame.image.load('Assets/home-menu-bg.jpg')
selection_menu_background = pygame.image.load('Assets/background3.png')


# loading the start buttons
play_button_off = pygame.image.load('Assets/small-start-button-off2.png')
play_button_on = pygame.image.load('Assets/small-start-button-on2.png')
# play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button_on.get_rect()
# adjust the position of the button on the screen
play_button_rect.x = int(info_display_size.current_w/2 - play_button_rect.w/2)
play_button_rect.y = int(info_display_size.current_h/5*3 + play_button_rect.h/1.5)

# loading the close buttons
close_button_off = pygame.image.load('Assets/close-button-off3.png')
close_button_on = pygame.image.load('Assets/close-button-on3.png')
close_button_rect = close_button_on.get_rect()
# adjust the position of the button on the screen
close_button_rect.x = int(info_display_size.current_w - close_button_rect.w*1.1)
close_button_rect.y = int(0.1*close_button_rect.h)

# loading the minimize button
minimize_button_off = pygame.image.load('Assets/minimize-icon-off.png')
minimize_button_on = pygame.image.load('Assets/minimize-icon-on.png')
minimize_button_rect = minimize_button_on.get_rect()
# adjust the position of the button on the screen
minimize_button_rect.x = int(info_display_size.current_w - minimize_button_rect.w*1.5 - close_button_rect.w)
minimize_button_rect.y = int(0.15*minimize_button_rect.h)


# loading the selection_menu_title
selection_menu_title = pygame.image.load('Assets/selection-menu-title.png')
selection_menu_title_rect = selection_menu_title.get_rect()
selection_menu_title_rect.x = int(info_display_size.current_w/2 - selection_menu_title_rect.w/2)
selection_menu_title_rect.y = int(info_display_size.current_h/5 - selection_menu_title_rect.h)

# initialize the Selection Buttons class
selection_buttons = ATH.SelectionButtons()

# loading the particle of the first selection button
selection_menu_button_particles = pygame.image.load('Assets/game-selection-particle-icon.png')
animated_selection_menu_button_particles = pyganim.PygAnimation([('Assets/game-selection-particle-icon.png', 750),
                                                                 ('Assets/game-selection-particle-icon-off.png', 750)])
animated_selection_menu_button_particles.play()
selection_menu_button_particles_rect = selection_menu_button_particles.get_rect()
selection_multiplications_button_rect = selection_buttons.selection_button_multiplication_rect
selection_menu_button_particles_rect.x = int(info_display_size.current_w/2 - selection_multiplications_button_rect.w*0.6)
selection_menu_button_particles_rect.y = int(info_display_size.current_h/5*2 - selection_multiplications_button_rect.h*0.5)

# loading the floating particles


running = True
in_home_menu = True
in_selection_menu = False
in_game = False

clock = pygame.time.Clock()
# loop of the game
while running:
    # set the fps
    clock.tick(244)

    # apply the background
    if in_home_menu:
        screen.blit(home_menu_background, (0, 0))
    elif in_selection_menu:
        screen.blit(selection_menu_background, (0, 0))

    # grab the cursor coordinate
    cursor_pos = pygame.mouse.get_pos()
    # display the appropriate play button
    if in_home_menu and play_button_rect.collidepoint(cursor_pos):
        screen.blit(play_button_on, play_button_rect)
    elif in_home_menu:
        screen.blit(play_button_off, play_button_rect)
    # display the appropriate close button
    if close_button_rect.collidepoint(cursor_pos):
        screen.blit(close_button_on, close_button_rect)
    else:
        screen.blit(close_button_off, close_button_rect)
    # display the appropriate minimize button
    if minimize_button_rect.collidepoint(cursor_pos):
        screen.blit(minimize_button_on, minimize_button_rect)
    else:
        screen.blit(minimize_button_off, minimize_button_rect)
    # display the appropriate multiplications button
    if in_selection_menu:

        if selection_buttons.selection_button_multiplication_rect.collidepoint(cursor_pos):
            selection_buttons.animated_selection_button_multiplication.blit(screen, selection_buttons.selection_button_multiplication_rect)
            animated_selection_menu_button_particles.blit(screen, selection_menu_button_particles_rect)
        else:
            screen.blit(selection_buttons.selection_button_multiplication,
                        selection_buttons.selection_button_multiplication_rect)
            screen.blit(selection_menu_button_particles, selection_menu_button_particles_rect)

    if in_selection_menu:
        screen.blit(selection_menu_title, selection_menu_title_rect)

    # update the frame :
    pygame.display.flip()

    # get the events
    for event in pygame.event.get():

        # detect if the window need to be closed
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if close_button_rect.collidepoint(event.pos):
                running = False
                pygame.quit()
            elif minimize_button_rect.collidepoint(event.pos):
                pygame.display.iconify()

        # detect if the player interact with a button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if in_home_menu and play_button_rect.collidepoint(event.pos):
                in_home_menu = False
                in_selection_menu = True
