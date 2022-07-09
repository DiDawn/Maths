import pygame
import ctypes

ctypes.windll.user32.SetProcessDPIAware()

pygame.init()

# initialisation of pygame module
pygame.init()

# summon the game's window / .set_caption is used to change the name
pygame.display.set_caption("Math Gym")

# height and width of the window
info_display_size = pygame.display.Info()
screen = pygame.display.set_mode((info_display_size.current_w, info_display_size.current_h))

# loading the background
background = pygame.image.load('Assets/menu_bg.jpg')

# loading the start buttons
play_button_off = pygame.image.load('Assets/small-start-button-off2.png')
play_button_on = pygame.image.load('Assets/small-start-button-on2.png')
# play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button_on.get_rect()
play_button_rect.x = int(info_display_size.current_w/2 - play_button_rect.w/2)
play_button_rect.y = int(info_display_size.current_h/5*3 + play_button_rect.h/1.5)

running = True

clock = pygame.time.Clock()
# loop of the game
while running:
    # set the fps
    clock.tick(144)

    # apply the background
    screen.blit(background, (0, 0))

    # grab the cursor coordinate
    cursor_pos = pygame.mouse.get_pos()
    # print(f'cursor_pos:{cursor_pos}  collide:{play_button_rect.collidepoint(cursor_pos)}')
    # display the appropriate play button
    if play_button_rect.collidepoint(cursor_pos):

        screen.blit(play_button_on, play_button_rect)
    else:
        screen.blit(play_button_off, play_button_rect)

    # update the frame :
    pygame.display.flip()

    # get the events
    for event in pygame.event.get():

        # detect if the window need to be closed
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
