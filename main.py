import pygame
import os

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1280, 1024
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pi-Fighters")

BACKGROUND = pygame.transform.scale(pygame.image.load(
    os.path.join('assets', 'images', 'space_bg.png')), (WIDTH, HEIGHT))

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound('assets/sounds/spaceship_hit.wav')
BULLET_SHOT_SOUND = pygame.mixer.Sound('assets/sounds/laser.wav')


HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)


FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 120, 90
P1_ROTATE = 0
P2_ROTATE = 90

ROTATE_SPEED = 20

P1_BULLET_COLOR = (255, 59, 0)
P2_BULLET_COLOR = (130, 19, 28)

P1_HIT = pygame.USEREVENT + 1
P2_HIT = pygame.USEREVENT + 2

PLAYER_1_IMAGE = pygame.image.load(
    os.path.join('assets', 'images', 'zero.png'))
PLAYER_1_IMAGE = pygame.transform.rotate(pygame.transform.scale(
    PLAYER_1_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), P1_ROTATE)
PLAYER_2_IMAGE = pygame.image.load(
    os.path.join('assets', 'images', 'falcon.png'))
PLAYER_2_IMAGE = pygame.transform.rotate(pygame.transform.scale(
    PLAYER_2_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), P2_ROTATE)


def draw_window(p1, p2, p1_bullets, p2_bullets, p1_health, p2_health):
    WIN.blit(BACKGROUND, (0, 0))
    pygame.draw.rect(WIN, (0, 0, 0), BORDER)
    p1_health_text = HEALTH_FONT.render(
        "Health: " + str(p1_health), 1, (255, 255, 255))
    p2_health_text = HEALTH_FONT.render(
        "Health: " + str(p2_health), 1, (255, 255, 255))
    WIN.blit(p1_health_text, (10, 10))
    WIN.blit(p2_health_text, (WIDTH - p2_health_text.get_width() - 10, 10))

    WIN.blit(PLAYER_1_IMAGE, (p1.x, p1.y))
    WIN.blit(PLAYER_2_IMAGE, (p2.x, p2.y))

    for bullet in p1_bullets:
        pygame.draw.rect(WIN, P1_BULLET_COLOR, bullet)

    for bullet in p2_bullets:
        pygame.draw.rect(WIN, P2_BULLET_COLOR, bullet)
    pygame.display.update()


def p1_handle_movement(keys_pressed, p1):
    if keys_pressed[pygame.K_a] and p1.x - VEL > 0:  # LEFT
        p1.x -= VEL
    if keys_pressed[pygame.K_d] and p1.x + VEL + p1.width < BORDER.x:  # RIGTH
        p1.x += VEL
    if keys_pressed[pygame.K_w] and p1.y - VEL > 0:  # UP
        p1.y -= VEL
    if keys_pressed[pygame.K_s] and p1.y + VEL + p1.height < HEIGHT:  # DOWN
        p1.y += VEL
    if keys_pressed[pygame.K_r]:
        p1.P1_ROTATE += ROTATE_SPEED


def p2_handle_movement(keys_pressed, p2):
    if keys_pressed[pygame.K_LEFT] and p2.x - VEL > BORDER.x + BORDER.width:  # LEFT
        p2.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and p2.x + VEL + p2.width < WIDTH:  # RIGHT
        p2.x += VEL
    if keys_pressed[pygame.K_UP] and p2.y - VEL > 0:  # UP
        p2.y -= VEL
    if keys_pressed[pygame.K_DOWN] and p2.y + VEL + p2.height < HEIGHT:  # DOWN
        p2.y += VEL


def handle_bullets(p1_bullets, p2_bullets, p1, p2):
    for bullet in p1_bullets:
        bullet.x += BULLET_VEL
        if p2.colliderect(bullet):
            pygame.event.post(pygame.event.Event(P2_HIT))
            p1_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            p1_bullets.remove(bullet)

    for bullet in p2_bullets:
        bullet.x -= BULLET_VEL
        if p1.colliderect(bullet):
            pygame.event.post(pygame.event.Event(P1_HIT))
            p2_bullets.remove(bullet)
        elif bullet.x < 0:
            p2_bullets.remove(bullet)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, (255, 255, 255))
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width() //
             2, HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    p1 = pygame.Rect(WIDTH//3.75, HEIGHT//2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    p2 = pygame.Rect(WIDTH//1.25, HEIGHT//2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    p1_bullets = []
    p2_bullets = []

    p1_health = 20
    p2_health = 20

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(p1_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        p1.x + p1.width, p1.y + p1.height//2, 15, 5)
                    p1_bullets.append(bullet)
                    BULLET_SHOT_SOUND.play()
                    BULLET_SHOT_SOUND.set_volume(0.6)
                if event.key == pygame.K_RCTRL and len(p2_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        p2.x, p2.y + p2.height//2, 15, 5)
                    p2_bullets.append(bullet)
                    BULLET_SHOT_SOUND.play()
                    BULLET_SHOT_SOUND.set_volume(0.6)

            if event.type == P1_HIT and p1_health > 0:
                p1_health -= 1
                BULLET_HIT_SOUND.play()
                BULLET_HIT_SOUND.set_volume(5)

            if event.type == P2_HIT and p2_health > 0:
                p2_health -= 1
                BULLET_HIT_SOUND.play()
                BULLET_HIT_SOUND.set_volume(5)

        winner_text = ""
        if p1_health <= 0:
            winner_text = "Player 2 Wins !"

        if p2_health <= 0:
            winner_text = "Player 1 Wins !"

        if winner_text != "":
            draw_winner(winner_text)  # SOMEONE WON
            break

        keys_pressed = pygame.key.get_pressed()
        p1_handle_movement(keys_pressed, p1)
        p2_handle_movement(keys_pressed, p2)

        handle_bullets(p1_bullets, p2_bullets, p1, p2)

        draw_window(p1, p2, p1_bullets, p2_bullets, p1_health, p2_health)

    main()


if __name__ == "__main__":
    main()
