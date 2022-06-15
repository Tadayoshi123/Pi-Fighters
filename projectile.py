
import pygame
import math
from ship import *


class Projectile():

    def __init__(self, x, y, width, height, angle):
        self.rect = pygame.Rect((x, y, width, height))
        self.movSpeed = 9
        self.power = 10
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        self.angle = angle

    def move(self):
        vertical_y = math.cos(math.radians(self.angle)) * self.movSpeed
        horizontal_x = math.sin(math.radians(self.angle)) * self.movSpeed
        self.rect.y -= vertical_y
        self.rect.x -= horizontal_x

        self.rect = pygame.Rect(self.rect.x, self.rect.y,
                                self.width, self.height)
