import pygame
import math
from projectile import *

# All global variables
ANGLE_SHIP1 = 90
ANGLE_SHIP2 = 0
WIDTH_VAISSEAU = 100
HEIGHT_VAISSEAU = 100
WIDTH_PROJECTILE = 10
HEIGHT_PROJECTILE = 10

SCREENWIDTH, SCREENHEIGHT = 1000, 800

SHIP1_IMG = pygame.image.load("assets/images/ships/zero.png")
SHIP1_IMG = pygame.transform.rotate(pygame.transform.scale(
    SHIP1_IMG, (WIDTH_VAISSEAU, HEIGHT_VAISSEAU)), ANGLE_SHIP1)

SHIP2_IMG = pygame.image.load("assets/images/ships/raven.png")
SHIP2_IMG = pygame.transform.rotate(pygame.transform.scale(
    SHIP2_IMG, (WIDTH_VAISSEAU, HEIGHT_VAISSEAU)), ANGLE_SHIP2)

pygame.joystick.init()

joystick1 = pygame.joystick.Joystick(0)
joystick1.init()

joystick2 = pygame.joystick.Joystick(1)
joystick2.init()

class Ship():

    def __init__(self,name, playerID, x, y):
        self.width = WIDTH_VAISSEAU
        self.height = HEIGHT_VAISSEAU
        self.x = x
        self.y = y
        self.rect = pygame.Rect((x, y, WIDTH_VAISSEAU, HEIGHT_VAISSEAU))
        self.health = 100
        self.movSpeed = 8
        self.playerID = playerID
        self.name = name
        if self.playerID == 1:
            self.image = SHIP1_IMG
            self.angle = ANGLE_SHIP1
        if self.playerID == 2:
            self.image = SHIP2_IMG
            self.angle = ANGLE_SHIP2


    def draw_ship(self, screen):
        rotated_img = pygame.transform.rotate(self.image,self.angle)
        new_rect = rotated_img.get_rect(center=self.image.get_rect(topleft=self.rect.topleft).center)
        screen.blit(rotated_img, new_rect)

    def rotate(self, left=False, right=True):
        if left:
            self.angle += self.movSpeed
        elif right:
            self.angle -= self.movSpeed

    def collision(self):
        if self.rect.left + self.movSpeed < 0:
            self.rect.left = 0

        if self.rect.right + self.movSpeed > SCREENWIDTH:
            self.rect.right = SCREENWIDTH

        if self.rect.top + self.movSpeed < 0:
            self.rect.top = 0

        if self.rect.bottom + self.movSpeed > SCREENHEIGHT:
            self.rect.bottom = SCREENHEIGHT

    def move(self):
        vertical_y = math.cos(math.radians(self.angle)) * self.movSpeed
        horizontal_x = math.sin(math.radians(self.angle)) * self.movSpeed
        self.rect.y -= vertical_y
        self.rect.x -= horizontal_x
        self.rect = pygame.Rect(self.rect.x, self.rect.y,self.width, self.height)


    def move_forward(self):
        self.movSpeed = self.movSpeed
        self.move()
        self.collision()


    def ship_movement(self):
        key = pygame.key.get_pressed()
        
        if self.playerID == 1:
            if key[pygame.K_w] or key[pygame.K_z]:
                self.move_forward()
            if joystick1:
                if joystick1.get_axis(5) > -1:
                    self.move_forward()

        if self.playerID == 2:
            if key[pygame.K_i]:
                self.move_forward()
            if joystick2:
                if joystick2.get_axis(5) > -1:
                    self.move_forward()

    def shoot_bullet(self):
        bullet = Projectile(self.rect.centerx, self.rect.y + self.height//2, WIDTH_PROJECTILE, HEIGHT_PROJECTILE, self.angle)
        return bullet