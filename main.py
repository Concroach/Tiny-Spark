import pygame, random, sys
from pygame.locals import *
import button

# Константы
FPS = 60
ENEMYSIZE = 10
ENEMYMAXSIZE = 40
ENEMYMINSPEED = 1
ENEMYMAXSPEED = 8
ADDNEWENEMYRATE = 6
PLAYERMOVERATE = 3

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHTBLUE = (202, 228, 241)
BLUE = (34, 145, 230)


def enemyhit(playerRect, enemy):
    for b in enemy:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def drawText(text, font, surface, x, y, color):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

pygame.init()
Clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)
pygame.display.set_caption("Tiny Spark")
font_menu_name = pygame.font.SysFont(None, 96)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Загрузка изображений в меню
start_img = pygame.image.load('images\menu\start_btn.png').convert_alpha()
setting_img = pygame.image.load('images\menu\setting_btn.png').convert_alpha()
exit_img = pygame.image.load('images\menu\exit_btn.png').convert_alpha()
shop_img = pygame.image.load('images\menu\shop.png').convert_alpha()

# Загрузка скинов
player_image = pygame.image.load('images\items\creature-3.png')
player_rect = player_image.get_rect()
enemy_image = pygame.image.load('images\items\enemy.jpg')

# Устанавливаем кнопки
start_button = button.Button(420, 250, start_img, 1.6)
setting_button = button.Button(420, 340, setting_img, 1.6)
exit_button = button.Button(420, 430, exit_img, 1.6)
shop_button = button.Button(860, 560, shop_img, 0.8)

running = True
while running:
    screen.fill(LIGHTBLUE)
    drawText('Tiny Spark', font_menu_name, screen, 346, 140, BLUE)
    
    if start_button.draw(screen):
        print('start the game')
        pygame.mouse.set_visible(False)
        top_score = 0
        while True:
            enemy = []
            score = 0
            player_rect.topleft = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50)
            moveLeft = False
            moveRight = False
            moveUp = False
            moveDown = False
            reverseCheat = False
            slowCheat = False
            baddieAddCounter = 0

            while True:
                score += 1
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    # Управление
                    if event.type == KEYDOWN:
                        if event.key == K_LEFT or event.key == ord('a'):
                            moveLeft = True
                        if event.key == K_RIGHT or event.key == ord('d'):
                            moveRight = True
                        if event.key == K_UP or event.key == ord('w'):
                            moveUp = True
                        if event.key == K_DOWN or event.key == ord('s'):
                            moveDown = True

                    if event.type == KEYUP:
                        if event.key == K_LEFT or event.key == ord('a'):
                            moveLeft = False
                        if event.key == K_RIGHT or event.key == ord('d'):
                            moveRight = False
                        if event.key == K_UP or event.key == ord('w'):
                            moveUp = False
                        if event.key == K_DOWN or event.key == ord('s'):
                            moveDown = False
                        if event.key == K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                # Спавн enemy
                if True:
                    baddieAddCounter += 1
                if baddieAddCounter == ADDNEWENEMYRATE:
                    baddieAddCounter = 0
                    enemyize = random.randint(ENEMYSIZE, ENEMYMAXSIZE)
                    new_enemy = {
                        'rect': pygame.Rect(random.randint(0, SCREEN_WIDTH-enemyize), 0 - enemyize, enemyize, enemyize),
                        'speed': random.randint(ENEMYMINSPEED, ENEMYMAXSPEED),
                        'surface':pygame.transform.scale(enemy_image, (enemyize, enemyize)),
                        }
                    enemy.append(new_enemy)

                # Персонаж не выходит за рамки и не поднимался выше половины высоты (позже стилизую так лвлa)
                if moveLeft and player_rect.left > 0:
                    player_rect.move_ip(-1 * PLAYERMOVERATE, 0)
                if moveRight and player_rect.right < SCREEN_WIDTH:
                    player_rect.move_ip(PLAYERMOVERATE, 0)
                if moveUp and player_rect.top > SCREEN_HEIGHT // 2:
                    player_rect.move_ip(0, -1 * PLAYERMOVERATE)
                if moveDown and player_rect.bottom < SCREEN_HEIGHT:
                    player_rect.move_ip(0, PLAYERMOVERATE)

                # Движение enemy
                for i in enemy:
                    i['rect'].move_ip(0, i['speed'])

                # Удаляем enemy, вышедшие за экран
                for i in enemy:
                    if i['rect'].top > SCREEN_HEIGHT:
                        enemy.remove(i)

                screen.fill(BLACK)

                # Отрисовка очков
                drawText('Score: %s' % (score), font, screen, 10, 10, WHITE)
                drawText('Top Score: %s' % (top_score), font, screen, 10, 50, WHITE)
                drawText('To exit press esc', font, screen, 10, 90, WHITE)

                # Отрисовка игрока
                screen.blit(player_image, player_rect)

                # Отрисовка врагов
                for i in enemy:
                    screen.blit(i['surface'], i['rect'])

                pygame.display.update()

                if enemyhit(player_rect, enemy):
                    if score > top_score:
                        top_score = score
                    break

                Clock.tick(FPS)


    if setting_button.draw(screen):
        print('settings')
    if exit_button.draw(screen):
        pygame.quit()
        sys.exit()
    if shop_button.draw(screen):
        print('shop')
    
    # Отрисовка кнопок через файл button.py
    start_button.draw(screen)
    setting_button.draw(screen)
    exit_button.draw(screen)
    shop_button.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
