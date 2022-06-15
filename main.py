import pygame

from ship import *
from projectile import *

pygame.init()
pygame.mixer.init()

TIME_FONT = pygame.font.SysFont('comicsans', 40)

SCORE_FONT = pygame.font.SysFont('comicsans', 20)

HEALTH_FONT = pygame.font.SysFont('comicsans', 20)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
PSEUDO_PLAYER_FONT = pygame.font.SysFont('comicsans', 20)

WINNER_TEXT = ""


FPS = 60

SCREENWIDTH, SCREENHEIGHT = 1000, 800

screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Pi-Fighters")

bgImage = pygame.transform.scale(pygame.image.load("assets/images/backgrounds/space_bg.png"), (SCREENWIDTH, SCREENHEIGHT))


# drawing
def draw_background(screen):
    screen.blit(bgImage, (0, 0))

def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, pygame.Color('red'), (x, y, 400, 15))
    if health >= 10:
        pygame.draw.rect(screen, pygame.Color('yellow'), (x, y, 400 * ratio, 15))   


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, (255, 255, 255))
    screen.blit(draw_text, (SCREENWIDTH//2 - draw_text.get_width() //
             2, SCREENHEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)
    pygame.quit()

def draw_projectile(Player1_bullet, Player2_bullet):
    for item in Player1_bullet:
        pygame.draw.rect(screen, pygame.Color('orange'), item)
    for item in Player2_bullet:
        pygame.draw.rect(screen, pygame.Color('red'), item)


# movement
def handle_movement_Player(Ship1, Ship2):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_q] or joystick1.get_axis(0) < -0.1:
        Ship1.rotate(left=True)

    if keys_pressed[pygame.K_d] or joystick1.get_axis(0) > 0.1:
        Ship1.rotate(right=True)

    if keys_pressed[pygame.K_j] or joystick2.get_axis(0) < -0.1:
        Ship2.rotate(left=True)

    if keys_pressed[pygame.K_l] or joystick2.get_axis(0) > 0.1:
        Ship2.rotate(right=True)



def handle_movement_projectile(Player1_bullet, Player2_bullet, Ship1, Ship2):
    for item in Player1_bullet:
        item.move()
        if Ship2.rect.colliderect(item):
            Player1_bullet.remove(item)
            Ship2.health -= item.power
        elif item.rect.x > SCREENWIDTH or item.rect.x < 0 or item.rect.y > SCREENHEIGHT or item.rect.y < 0 :
            Player1_bullet.remove(item)
    for item in Player2_bullet:
        item.move()
        if Ship1.rect.colliderect(item):
            Player2_bullet.remove(item)
            Ship1.health -= item.power
        elif item.rect.x > SCREENWIDTH or item.rect.x < 0 or item.rect.y > SCREENHEIGHT or item.rect.y < 0:
            Player2_bullet.remove(item)


def main():
    clock = pygame.time.Clock()
    Ship1 = Ship("Yanis",1, 100, 350)
    Ship2 = Ship("Marc",2, 700, 350)

    #Empty lists that will stock the bullets
    Player1_bullet = []
    Player2_bullet = []

    run = True

    while run:
        # set game speed
        clock.tick(FPS)
        # draw background

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                # exit pygame
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    Player1_bullet.append(Ship1.shoot_bullet())
                if event.key == pygame.K_o:
                    Player2_bullet.append(Ship2.shoot_bullet())
            if event.type == pygame.JOYBUTTONDOWN:
                if joystick1.get_button(5):
                    Player1_bullet.append(Ship1.shoot_bullet())
                if joystick2.get_button(5):
                    Player2_bullet.append(Ship2.shoot_bullet())

        draw_background(screen)

        # draw healthbars
        draw_health_bar(Ship1.health, 20, 20)
        draw_health_bar(Ship2.health, 580, 20)

        # draw ships
        Ship1.draw_ship(screen)
        Ship2.draw_ship(screen)

        # ensure the movement and the collision detection of the bullets
        handle_movement_projectile(
            Player1_bullet, Player2_bullet, Ship1, Ship2)

        Ship.ship_movement(Ship1)
        Ship.ship_movement(Ship2)
        handle_movement_Player(Ship1, Ship2)

        draw_projectile(Player1_bullet, Player2_bullet)

        if Ship1.health <= 0:
            WINNER_TEXT = Ship2.name + " wins !"
            draw_winner(WINNER_TEXT)
        
        if Ship2.health <= 0:
            WINNER_TEXT = Ship1.name + " wins !"
            draw_winner(WINNER_TEXT)

        # update display
        pygame.display.update()


if __name__ == '__main__':
    main()
