import pygame
import random
import sys
import time
import button
from PIL import Image
from pygame.locals import *
from save import *

# Константы
FPS = 60
ENEMYSIZE = 15
FRIENDSIZE = 35
ENEMYMAXSIZE = 40
FRIENDMAXSIZE = 50
ENEMYMINSPEED = 1
ENEMYMAXSPEED = 5
ADDNEWENEMYRATE = 6
ADDNEWFRIENDRATE = 30
PLAYERMOVERATE = 4

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHTBLUE = (202, 228, 241)
BLUE = (34, 145, 230)
RED = (255, 0, 0)
GREEN = (0, 214, 120)


pygame.init()
save_data = save()
Clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)
pygame.display.set_caption("Tiny Spark")
font_menu_name = pygame.font.SysFont(None, 96)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Загрузка изображений кнопок
start_img = pygame.image.load('images/menu/start_btn.png').convert_alpha()
setting_img = pygame.image.load('images/menu/setting_btn.png').convert_alpha()
quit_img = pygame.image.load('images/menu/quit_btn.png').convert_alpha()
shop_img = pygame.image.load('images/menu/shop.png').convert_alpha()
restart_img = pygame.image.load('images/menu/why.png').convert_alpha()
back_to_menu_img = pygame.image.load('images/menu/exit_btn.png').convert_alpha()
resume_img = pygame.image.load('images/menu/resume_btn.png').convert_alpha()
packet_minecraft_img = pygame.image.load('images/shop/packet_minecraft.png').convert_alpha()
packet_minecraft_closed_img = pygame.image.load('images/shop/packet_minecraft_closed.png').convert_alpha()
packet_minecraft_selected_img = pygame.image.load('images/shop/packet_minecraft_selected.png').convert_alpha()
packet_space_img = pygame.image.load('images/shop/packet_space.png').convert_alpha()
packet_space_selected_img = pygame.image.load('images/shop/packet_space_selected.png').convert_alpha()
packet_space_closed_img = pygame.image.load('images/shop/packet_space_closed.png').convert_alpha()
packet_mario_img = pygame.image.load('images/shop/packet_mario.png').convert_alpha()
packet_mario_selected_img = pygame.image.load('images/shop/packet_mario_selected.png').convert_alpha()

yes_img = pygame.image.load('images/menu/yes_btn.png').convert_alpha()
no_img = pygame.image.load('images/menu/no_btn.png').convert_alpha()

turn_down_img = pygame.image.load('images/menu/volume_minus.png').convert_alpha()
turn_up_img = pygame.image.load('images/menu/volume_plus.png').convert_alpha()

background_image = pygame.image.load('images/menu/fon.png')

# Загрузка скинов
player_skin = 'images/items/player_mario.png'
player_image = pygame.image.load(player_skin)
player_rect = player_image.get_rect()
enemy_skin = 'images/items/enemy_mushr.png'
enemy_image = pygame.image.load(enemy_skin)
friend_skin = 'images/items/friend_coin.png'
friend_image = pygame.image.load(friend_skin)

# Устанавливаем кнопки
resume_button = button.Button(420, 160, resume_img, 1.6)
resume_button_for_pause = button.Button(420, 250, resume_img, 1.6)
start_button = button.Button(420, 250, start_img, 1.6)
restart_button = button.Button(420, 250, restart_img, 1.6)
restart_button_for_pause = button.Button(420, 340, restart_img, 1.6)
setting_button = button.Button(420, 340, setting_img, 1.6)
quit_button = button.Button(420, 430, quit_img, 1.6)
back_to_menu_button = button.Button(420, 430, back_to_menu_img, 1.6)
back_to_menu_button_for_pause = button.Button(420, 430, back_to_menu_img, 1.6)
shop_button = button.Button(860, 560, shop_img, 0.8)
packet_mario_button = button.Button(324, 100, packet_mario_img, 1)
packet_mario_selected_button = button.Button(324, 100, packet_mario_selected_img, 1)
packet_minecraft_button = button.Button(474, 100, packet_minecraft_img, 1)
packet_minecraft_closed_button = button.Button(474, 100, packet_minecraft_closed_img, 1)
packet_minecraft_selected_button = button.Button(474, 100, packet_minecraft_selected_img, 1)
packet_space_button = button.Button(624, 100, packet_space_img, 1)
packet_space_closed_button = button.Button(624, 100, packet_space_closed_img, 1)
packet_space_selected_button = button.Button(624, 100, packet_space_selected_img, 1)

yes_button = button.Button(230, 200, yes_img, 0.15)
no_button = button.Button(660, 200, no_img, 0.15)

turn_down = button.Button(230, 200, turn_down_img, 0.15)
turn_up = button.Button(430, 200, turn_up_img, 0.15)

# Музыка
# Логика такова: если мы запускаем игру из основного меню (с открытием игры или выйдя в него), то песня начинается заново
# если мы запускаем игру кнопкой restart, то песня продолжается с того момента, на котором игрок умер
# если игрок заходит в меню, то после выхода из него песня продолжается с того места, с которого была остановлена
volume = save_data.get('volume')
pygame.mixer.music.load('sounds/undead.mp3')
pygame.mixer.music.set_volume(volume)
game_over = pygame.mixer.Sound('sounds/game_over.mp3')
game_over.set_volume(volume)
take_friend = pygame.mixer.Sound('sounds/take_sound.mp3')
take_friend.set_volume(volume)

# Флаги для магазина
flag_mario = save_data.get('flag_mario')

flag_mine = save_data.get('flag_mine')
flag_mine_buy = save_data.get('flag_mine_buy')
flag_mine_is = save_data.get('flag_mine_is')

flag_rocket = save_data.get('flag_rocket')
flag_rocket_buy = save_data.get('flag_rocket_buy')
flag_rocket_is = save_data.get('flag_rocket_is')

# Соприкасание игрока с friend
def friendhit(player_rect, friend):
    for i in friend:
        if player_rect.colliderect(i['rect']):
            return True
    return False

# Соприкасание игрока с enemy
def enemyhit(player_rect, enemy):
    for i in enemy:
        if player_rect.colliderect(i['rect']):
            return True
    return False

# Функция для отрисовки текста
def drawText(text, font, surface, x, y, color):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Настройки звука
def settings_menu_after_death():
    global volume
    while True:
        screen.fill(BLACK)
        turn_down.draw(screen)
        turn_up.draw(screen)
        back_to_menu_button.draw(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                save_files()
                pygame.quit()
                sys.exit()
            if turn_down.clicked_on_btn():
                if volume > 3.608224830031759e-16:
                    volume -= 0.1
                else:
                    pass
                print(volume)
                take_friend.set_volume(volume)
                game_over.set_volume(volume)
                pygame.mixer.music.set_volume(volume)
            if turn_up.clicked_on_btn():
                if volume <= 1:
                    volume += 0.1
                else:
                    pass
                print(volume)
                take_friend.set_volume(volume)
                game_over.set_volume(volume)
                pygame.mixer.music.set_volume(volume)
            if back_to_menu_button.draw(screen):
                menu_after_death(player_image, player_rect, player_skin, enemy_image, friend_image)
        pygame.display.update()

def settings_main_menu():
    global volume
    while True:
        screen.fill(BLACK)
        turn_down.draw(screen)
        turn_up.draw(screen)
        back_to_menu_button.draw(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                save_files()
                pygame.quit()
                sys.exit()
            if back_to_menu_button.draw(screen):
                save_files()
                main_menu(player_image, player_rect, player_skin, enemy_image, friend_image)
            if turn_down.clicked_on_btn():
                if volume > 3.608224830031759e-16:
                    volume -= 0.1
                else:
                    pass
                print(volume)
                take_friend.set_volume(volume)
                game_over.set_volume(volume)
                pygame.mixer.music.set_volume(volume)
            if turn_up.clicked_on_btn():
                if volume <= 1:
                    volume += 0.1
                else:
                    pass
                print(volume)
                take_friend.set_volume(volume)
                game_over.set_volume(volume)
                pygame.mixer.music.set_volume(volume)

        pygame.display.update()

    # если volume = 1 выводим изображение со всеми палочками и тд

# Функция сохранения очков, скинов и их состояний
def save_files():
    save_data.save('max', top_score)
    save_data.save('all', all_scores)
    save_data.save('volume', volume)
    print(volume)
    save_data.save('flag_mario', flag_mario)
    save_data.save('flag_rocket', flag_rocket)
    save_data.save('flag_rocket_is', flag_rocket_is)
    save_data.save('flag_rocket_buy', flag_rocket_buy)
    save_data.save('flag_mine', flag_mine)
    save_data.save('flag_mine_is', flag_mine_is)
    save_data.save('flag_mine_buy', flag_mine_buy)

# Покупка скина
def check(player_image, player_rect, player_skin, enemy_image, friend_image, flag_of_check):
    global flag_rocket, flag_mine
    global flag_mine_is, flag_mine_buy
    global flag_rocket_is, flag_rocket_buy, all_scores
    no_points = False
    while True:
        screen.fill(BLACK)
        back_to_menu_button.draw(screen)
        yes_button.draw(screen)
        no_button.draw(screen)
        drawText('Вы уверены, что хотите купить?', font, screen, 240, 50, WHITE)
        if no_points:
            drawText('Не хватает очков', font, screen, 174, 346, RED)
        for event in pygame.event.get():
            # отслеживаем нажатие кнопок
            if event.type == QUIT:
                save_files()
                pygame.quit()
                sys.exit()
            if flag_of_check == 'space':
                if yes_button.clicked_on_btn() or (event.type == KEYDOWN and event.key == K_RETURN):
                    if all_scores >= 50:
                        all_scores -= 50
                        flag_rocket_is = True
                        flag_rocket_buy = False
                        flag_rocket = True
                        flag_mine = False
                        player_skin = 'images/items/player_rocket.png'
                        player_image = pygame.image.load(player_skin)
                        player_rect = player_image.get_rect()
                        enemy_skin = 'images/items/enemy_asteroid.png'
                        enemy_image = pygame.image.load(enemy_skin)
                        friend_skin = 'images/items/friend_star.png'
                        friend_image = pygame.image.load(friend_skin)
                        shop(player_image, player_rect, player_skin, enemy_image, friend_image)
                    else:
                        no_points = True
                if no_button.clicked_on_btn() or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    shop(player_image, player_rect, player_skin, enemy_image, friend_image)
                if back_to_menu_button.clicked_on_btn():
                    shop(player_image, player_rect, player_skin, enemy_image, friend_image)
            if flag_of_check == 'mine':
                if yes_button.clicked_on_btn() or (event.type == KEYDOWN and event.key == K_RETURN):
                    if all_scores >= 30:
                        all_scores -= 30
                        flag_mine_is = True
                        flag_mine_buy = False
                        flag_mine = True
                        player_skin = 'images/items/minecraft_steve.jpg'
                        player_image = pygame.image.load(player_skin)
                        player_rect = player_image.get_rect()
                        enemy_skin = 'images/items/minecraft_crepper.jpg'
                        enemy_image = pygame.image.load(enemy_skin)
                        friend_skin = 'images/items/friend_diamond.png'
                        friend_image = pygame.image.load(friend_skin)
                        shop(player_image, player_rect, player_skin, enemy_image, friend_image)
                    else:
                        no_points = True
                if no_button.clicked_on_btn() or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    shop(player_image, player_rect, player_skin, enemy_image, friend_image)
                if back_to_menu_button.clicked_on_btn():
                    shop(player_image, player_rect, player_skin, enemy_image, friend_image)
        pygame.display.update()

# Магазин для выбора скинов
def shop(player_image, player_rect, player_skin, enemy_image, friend_image):
    global flag_rocket
    global flag_mine
    global flag_mine_buy
    global flag_mine_is
    global flag_rocket_buy
    global flag_rocket_is
    global flag_mario
    global all_scores
    while True:
        screen.fill(GREEN)
        drawText('Scores: %s' % (all_scores), font, screen, 10, 50, WHITE)
        back_to_menu_button.draw(screen)
        packet_space_button.draw(screen)
        packet_minecraft_button.draw(screen)
        packet_mario_button.draw(screen)
        if flag_rocket_buy:
            packet_space_closed_button.draw(screen)
            drawText('20$', font, screen, 646, 204, WHITE)
        if flag_mine_buy:
            drawText('10$', font, screen, 496, 204, WHITE)
            packet_minecraft_closed_button.draw(screen)
        if flag_mine:
            packet_minecraft_selected_button.draw(screen)
        elif flag_rocket:
            packet_space_selected_button.draw(screen)
        elif flag_mario:
            packet_mario_selected_button.draw(screen)
        for event in pygame.event.get():
            # отслеживаем нажатие кнопок
            if event.type == QUIT:
                save_files()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == ord(';'):
                all_scores += 100000
            if back_to_menu_button.draw(screen):
                main_menu(player_image, player_rect, player_skin, enemy_image, friend_image)
            if packet_space_button.clicked_on_btn() and flag_rocket_buy:
                flag_of_check = 'space'
                check(player_image, player_rect, player_skin, enemy_image, friend_image, flag_of_check)
            if packet_minecraft_button.clicked_on_btn() and flag_mine_buy:
                flag_of_check = 'mine'
                check(player_image, player_rect, player_skin, enemy_image, friend_image, flag_of_check)
            if packet_mario_button.clicked_on_btn():
                player_skin = 'images/items/player_mario.png'
                player_image = pygame.image.load(player_skin)
                player_rect = player_image.get_rect()
                enemy_skin = 'images/items/enemy_mushr.png'
                enemy_image = pygame.image.load(enemy_skin)
                friend_skin = 'images/items/friend_coin.png'
                friend_image = pygame.image.load(friend_skin)
                flag_mario = True
                flag_mine = False
                flag_rocket = False
            if flag_mine_is:
                if packet_minecraft_button.clicked_on_btn():
                    player_skin = 'images/items/minecraft_steve.jpg'
                    player_image = pygame.image.load(player_skin)
                    player_rect = player_image.get_rect()
                    enemy_skin = 'images/items/minecraft_crepper.jpg'
                    enemy_image = pygame.image.load(enemy_skin)
                    friend_skin = 'images/items/friend_diamond.png'
                    friend_image = pygame.image.load(friend_skin)
                    flag_mine = True
                    flag_rocket = False
                    flag_mario = False
            if flag_rocket_is:
                if packet_space_button.clicked_on_btn():
                    flag_mine = False
                    flag_rocket = True
                    flag_mario = False
                    player_skin = 'images/items/player_rocket.png'
                    player_image = pygame.image.load(player_skin)
                    player_rect = player_image.get_rect()
                    enemy_skin = 'images/items/enemy_asteroid.png'
                    enemy_image = pygame.image.load(enemy_skin)
                    friend_skin = 'images/items/friend_star.png'
                    friend_image = pygame.image.load(friend_skin)
        pygame.display.flip()

# Функция меню после смерти
def menu_after_death(player_image, player_rect, player_skin, enemy_image, friend_image):
    save_data.save('max', top_score)
    save_data.save('all', all_scores)
    pygame.mixer.music.pause()
    death_menu = True
    while death_menu:
        screen.blit(background_image, (0, 0))
        drawText('YOU DIED', font_menu_name, screen, 360, 140, RED)
        pygame.mouse.set_visible(True)
        # создаём нужные кнопки
        restart_button.draw(screen)
        setting_button.draw(screen)
        back_to_menu_button.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            # отслеживаем нажатие кнопок
            if event.type == QUIT:
                save_files()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    save_files()
                    pygame.quit()
                    sys.exit()
                if event.key == ord('r') or event.key == K_SPACE or event.key == K_RETURN:
                    pygame.mixer.music.unpause()
                    game(player_image, player_rect, player_skin, enemy_image, friend_image)
            if restart_button.draw(screen):
                pygame.mixer.music.unpause()
                game(player_image, player_rect, player_skin, enemy_image, friend_image)
            if setting_button.draw(screen):
                    settings_menu_after_death()
            if back_to_menu_button.draw(screen):
                main_menu(player_image, player_rect, player_skin, enemy_image, friend_image)

# Меню в которое мы выходим из "меню" при помощи esc или из "меню" после смерти
def main_menu(player_image, player_rect, player_skin, enemy_image, friend_image):
    while True:
        screen.fill(LIGHTBLUE)
        drawText('Tiny Spark', font_menu_name, screen, 346, 140, BLUE)
        for event in pygame.event.get():
            if event.type == QUIT:
                        save_files()
                        pygame.quit()
                        sys.exit()
            if start_button.draw(screen):
                pygame.mixer.music.play()
                game(player_image, player_rect, player_skin, enemy_image, friend_image)
            if setting_button.draw(screen):
                settings_main_menu()
            if quit_button.draw(screen):
                save_files()
                pygame.quit()
                sys.exit()
            if shop_button.draw(screen):
                shop(player_image, player_rect, player_skin, enemy_image, friend_image)
            pygame.display.flip()


top_score = save_data.get('max')
all_scores = save_data.get('all')

running = True
while running:
    screen.fill(LIGHTBLUE)
    drawText('Tiny Spark', font_menu_name, screen, 346, 140, BLUE)
    if start_button.draw(screen):
        pygame.mixer.music.play()
        game(player_image, player_rect, player_skin, enemy_image, friend_image)
    if setting_button.draw(screen):
        settings_main_menu()
    if quit_button.draw(screen):
        save_files()
        pygame.quit()
        sys.exit()
    if shop_button.draw(screen):
        shop(player_image, player_rect, player_skin, enemy_image, friend_image)

    # Функция гемплея
    def game(player_image, player_rect, player_skin, enemy_image, friend_image):
        global top_score
        global all_scores
        pygame.mouse.set_visible(False)
        while True:
            enemy = []
            friend = []
            score = 0
            im = Image.open(player_skin)
            (player_width, player_height) = im.size
            player_rect.topleft = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - player_height)
            moveLeft = False
            moveRight = False
            moveUp = False
            moveDown = False
            reverseCheat = False
            slowCheat = False
            EnemyCounter = 0
            FriendCounter = 0
            while True:                
                for event in pygame.event.get():
                    if event.type == QUIT:
                        save_files()
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
                        # Пауза
                        if event.key == K_ESCAPE:
                            screen.blit(background_image, (0, 0))
                            pause = True
                            x = 0
                            while pause:
                                pygame.mouse.set_visible(True)
                                drawText('PAUSE', font_menu_name, screen, 408, 150, GREEN)
                                resume_button_for_pause.draw(screen)
                                restart_button_for_pause.draw(screen)
                                # setting_button.draw(screen)
                                back_to_menu_button_for_pause.draw(screen)
                                pygame.display.flip()
                                for event in pygame.event.get():
                                    # отслеживаем нажатие кнопок
                                    if event.type == QUIT:
                                        top_score = score
                                        save_files()
                                        pygame.quit()
                                        sys.exit()
                                    if event.type == KEYUP:
                                        x += 1
                                        if event.key == K_ESCAPE and x % 2 == 0:
                                            pause = False
                                            pygame.mixer.music.unpause()
                                            pygame.mouse.set_visible(False)
                                        else:
                                            pause = True
                                            pygame.mixer.music.pause()
                                    if resume_button_for_pause.draw(screen):
                                        pause = False    
                                        pygame.mouse.set_visible(False)
                                        pygame.mixer.music.unpause()
                                    if restart_button_for_pause.draw(screen):
                                        if score > top_score:
                                            top_score = score
                                        pygame.mixer.music.unpause()
                                        game(player_image, player_rect, player_skin, enemy_image, friend_image)
                                    '''if setting_button.draw(screen):
                                        settings()'''
                                    if back_to_menu_button_for_pause.draw(screen):
                                        if score > top_score:
                                            top_score = score
                                        main_menu(player_image, player_rect, player_skin, enemy_image, friend_image)

                    if event.type == KEYUP:
                        if event.key == K_LEFT or event.key == ord('a'):
                            moveLeft = False
                        if event.key == K_RIGHT or event.key == ord('d'):
                            moveRight = False
                        if event.key == K_UP or event.key == ord('w'):
                            moveUp = False
                        if event.key == K_DOWN or event.key == ord('s'):
                            moveDown = False
                # Спавн enemy
                if True:
                    EnemyCounter += 1
                if EnemyCounter == ADDNEWENEMYRATE:
                    EnemyCounter = 0
                    enemyize = random.randint(ENEMYSIZE, ENEMYMAXSIZE)
                    new_enemy = {
                        'rect': pygame.Rect(random.randint(0, SCREEN_WIDTH - enemyize), 0 - enemyize, enemyize, enemyize),
                        'speed': random.randint(ENEMYMINSPEED, ENEMYMAXSPEED),
                        'surface':pygame.transform.scale(enemy_image, (enemyize, enemyize)),
                        }
                    enemy.append(new_enemy)
                # Спавн friend
                if True:
                    FriendCounter += 1
                if FriendCounter == ADDNEWFRIENDRATE:
                    FriendCounter = 0
                    friend_size = random.randint(FRIENDSIZE, FRIENDMAXSIZE)
                    new_friend = {
                        'rect': pygame.Rect(random.randint(0, SCREEN_WIDTH - friend_size), 0 - friend_size, friend_size, friend_size),
                        'speed': random.randint(ENEMYMINSPEED, ENEMYMAXSPEED),
                        'surface':pygame.transform.scale(friend_image, (friend_size, friend_size)),
                        }
                    friend.append(new_friend)

                # Персонаж не выходит за рамки и не поднимался выше половины высоты (позже стилизую так лвлa)
                if moveLeft and player_rect.left > 0:
                    player_rect.move_ip(-1 * PLAYERMOVERATE, 0)
                if moveRight and player_rect.right < SCREEN_WIDTH:
                    player_rect.move_ip(PLAYERMOVERATE, 0)
                if moveUp and player_rect.top > SCREEN_HEIGHT // 2:
                    player_rect.move_ip(0, -1 * PLAYERMOVERATE)
                if moveDown and player_rect.bottom < SCREEN_HEIGHT:
                    player_rect.move_ip(0, PLAYERMOVERATE)

                # Движение enemy и friend
                for i in enemy:
                    i['rect'].move_ip(0, i['speed'])

                for i in friend:
                    i['rect'].move_ip(0, i['speed'])

                # Удаляем enemy и friend, вышедшие за экран
                for i in enemy:
                    if i['rect'].top > SCREEN_HEIGHT:
                        enemy.remove(i)

                for i in friend:
                    if i['rect'].top > SCREEN_HEIGHT:
                        friend.remove(i)

                screen.fill(BLACK)

                # Отрисовка очков
                drawText('Score: %s' % (score), font, screen, 10, 10, WHITE)
                drawText('Top Score: %s' % (top_score), font, screen, 10, 50, WHITE)

                # Отрисовка игрока
                screen.blit(player_image, player_rect)

                #.Отрисовка врагов
                for i in enemy:
                    screen.blit(i['surface'], i['rect'])
                # Отрисовка друзей
                for i in friend:
                    screen.blit(i['surface'], i['rect'])
                pygame.display.update()
                
                # Проверка на соприкасание игрока и friend 
                if friendhit(player_rect, friend):
                    score += 1
                    all_scores += 1
                    take_friend.play()
                    for i in friend:
                        if player_rect.colliderect(i['rect']):                            
                            friend.remove(i)

                            
                # Проверка на соприкасание игрока и enemy
                if enemyhit(player_rect, enemy):
                    if score > top_score:
                        top_score = score
                    break

                Clock.tick(FPS)

            game_over.play()
            take_friend.stop()
            menu_after_death(player_image, player_rect, player_skin, enemy_image, friend_image)

            pygame.display.update()

    # Отрисовка кнопок через файл button.py
    start_button.draw(screen)
    setting_button.draw(screen)
    quit_button.draw(screen)
    shop_button.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_files()
            running = False
        if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    save_files()
                    pygame.quit()
                    sys.exit()
        
    pygame.display.update()
