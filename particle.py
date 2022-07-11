import pygame
from random import randint
from math import cos, sin, radians
from time import time


class Particle(pygame.sprite.Sprite):

    def __init__(self, game, image_path: str, allow_spinning=True):
        super().__init__()

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.origin_image = self.image
        self.side = self.defined_spawn_point()

        self.angle = 0
        self.defined_angle(self.side)
        self.spinning = False
        if allow_spinning:
            self.is_spinning = randint(1, 4)
            if self.is_spinning == 1:
                self.spinning = True
                self.add_to_angle = randint(1, 4)

        self.rotate()

        self.velocity = randint(2, 4) / 2
        self.x_velocity = self.velocity * cos(radians(self.angle))
        self.y_velocity = self.velocity * sin(radians(self.angle))

        self.been_on_screen = False
        self.creation_time = time()
        self.time_on_screen = None

        self.last_position = (self.rect.x, self.rect.y)

        self.game = game

        print(
            f'angle={self.angle}, spawnpoint={self.rect.x, self.rect.y}, velocity={self.velocity, self.x_velocity, self.y_velocity}')

    def defined_spawn_point(self):
        side = randint(1, 4)
        print(side)
        # left
        if side == 1:
            self.rect.x = -self.rect.w
            self.rect.y = randint(0, 1080)
        # top
        elif side == 2:
            self.rect.x = randint(0, 1920)
            self.rect.y = -self.rect.h
        # right
        elif side == 3:
            self.rect.x = 1920
            self.rect.y = randint(0, 1080)
        # bottom
        elif side == 1:
            self.rect.x = randint(0, 1920)
            self.rect.y = 1080

        return side

    def defined_angle(self, side):
        # left
        if side == 1:
            self.angle = randint(-45, 45)
        # top
        elif side == 2:
            self.angle = randint(45, 135)
        # right
        elif side == 3:
            self.angle = randint(225, 315)
        elif side == 4:
            self.angle = randint(-135, -45)

    def rotate(self):
        if self.spinning:
            self.angle += self.add_to_angle
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def destroy(self):
        self.game.all_particles.remove(self)
        self.game.spawn_particle('Assets/floating-math-particle1.png')
        print('ouch me dead')

    def move(self):
        if 0 <= self.rect.x < 1 and 0 < self.x_velocity < 1:
            self.x_velocity = 1

        if 0 <= self.rect.y < 1 and 0 < self.y_velocity < 1:
            self.y_velocity = 1

        if 0 <= self.rect.x < 1 and 0 > self.x_velocity > -1:
            self.x_velocity = -1

        if 0 <= self.rect.y < 1 and 0 > self.y_velocity > -1:
            self.y_velocity = -1

        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity

        #print(self.rect.x, self.rect.y)

        if self.spinning:
            self.rotate()

        if 0 < self.rect.x < 1920 and 0 < self.rect.y < 1080:
            self.been_on_screen = True
            self.time_on_screen = time()

        if (not self.been_on_screen and time() - self.creation_time > 1.5) or time() - self.creation_time > 20:
            self.destroy()

        if self.time_on_screen is not None:
            if time() - self.time_on_screen > 1:
                if ((self.rect.x > 1920 or (self.rect.x + self.rect.w) < 0) or
                        ((self.rect.y - self.rect.h) < 1080 or self.rect.y < 0)) and self.been_on_screen:
                    self.destroy()

        if self.last_position == (self.rect.x, self.rect.y):
            self.destroy()
