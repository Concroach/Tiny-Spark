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

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHTBLUE = (202, 228, 241)
BACKGROUND_COLOR = (104, 155, 202)

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
game_defoult_img = pygame.image.load('images/shop/level_1.png').convert_alpha()
game_defoult_selected_img = pygame.image.load('images/shop/level_1_selected.png').convert_alpha()
game_img = pygame.image.load('images/shop/level_2.png').convert_alpha()
game_closed_img = pygame.image.load('images/shop/level_2_close.png').convert_alpha()
game_selected_img = pygame.image.load('images/shop/level_2_selected.png').convert_alpha()
music_defoult_img = pygame.image.load('images/shop/defoult_music_img.png').convert_alpha()
music_defoult_selected_img = pygame.image.load('images/shop/defoult_music_selected_img.png').convert_alpha()
undead_img = pygame.image.load('images/shop/undead_img.png').convert_alpha()
undead_closed_img = pygame.image.load('images/shop/undead_close_img.png').convert_alpha()
undead_selected_img = pygame.image.load('images/shop/undead_selected_img.png').convert_alpha()
hotline_1_img = pygame.image.load('images/shop/hotline_1_img.png').convert_alpha()
hotline_1_closed_img = pygame.image.load('images/shop/hotline_1_close_img.png').convert_alpha()
hotline_1_selected_img = pygame.image.load('images/shop/hotline_1_selected_img.png').convert_alpha()


yes_img = pygame.image.load('images/menu/yes_btn.png').convert_alpha()
no_img = pygame.image.load('images/menu/no_btn.png').convert_alpha()

turn_down_img = pygame.image.load('images/menu/turn_down.png').convert_alpha()
turn_up_img = pygame.image.load('images/menu/turn_up.png').convert_alpha()

background_image = pygame.image.load('images/menu/fon.png')
background_shop = pygame.image.load('images/menu/background_shop.png')
background_settings = pygame.image.load('images/menu/background_settings.png')
volume_img = pygame.image.load('images/menu/volume.png').convert_alpha()
zerofrom10 = pygame.image.load('images/menu/0from10.png').convert_alpha()
onefrom10 = pygame.image.load('images/menu/1from10.png').convert_alpha()
twofrom10 = pygame.image.load('images/menu/2from10.png').convert_alpha()
threefrom10 = pygame.image.load('images/menu/3from10.png').convert_alpha()
fourfrom10 = pygame.image.load('images/menu/4from10.png').convert_alpha()
fivefrom10 = pygame.image.load('images/menu/5from10.png').convert_alpha()
sixfrom10 = pygame.image.load('images/menu/6from10.png').convert_alpha()
sevenfrom10 = pygame.image.load('images/menu/7from10.png').convert_alpha()
eightfrom10 = pygame.image.load('images/menu/8from10.png').convert_alpha()
ninefrom10 = pygame.image.load('images/menu/9from10.png').convert_alpha()



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
game_defoult_button = button.Button(174, 270, game_defoult_img, 1)
game_defoult_selected_button = button.Button(174, 270, game_defoult_selected_img, 1)
game_button = button.Button(324, 270, game_img, 1)
game_closed_button = button.Button(324, 270, game_closed_img, 1)
game_selected_button = button.Button(324, 270, game_selected_img, 1)
music_defoult_button = button.Button(550, 270, music_defoult_img, 1)
music_defoult_selected_button = button.Button(550, 270, music_defoult_selected_img, 1)
undead_button = button.Button(670, 270, undead_img, 1)
undead_closed_button = button.Button(670, 270, undead_closed_img, 1)
undead_selected_button = button.Button(670, 270, undead_selected_img, 1)
hotline_1_button = button.Button(790, 270, hotline_1_img, 1)
hotline_1_closed_button = button.Button(790, 270, hotline_1_closed_img, 1)
hotline_1_selected_button = button.Button(790, 270, hotline_1_selected_img, 1)


yes_button = button.Button(230, 200, yes_img, 0.15)
no_button = button.Button(660, 200, no_img, 0.15)

turn_down = button.Button(166, 200, turn_down_img, 0.25)
turn_up = button.Button(730, 200, turn_up_img, 0.25)

# Музыка
# Логика такова: если мы запускаем игру из основного меню (с открытием игры или выйдя в него), то песня начинается заново
# если мы запускаем игру кнопкой restart, то песня продолжается с того момента, на котором игрок умер
# если игрок заходит в меню, то после выхода из него песня продолжается с того места, с которого была остановлена
volume = save_data.get('volume')


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

flag_game_defoult = save_data.get('flag_game_defoult')
flag_game = save_data.get('flag_game')
flag_game_is = save_data.get('flag_game_is')
flag_game_buy = save_data.get('flag_game_buy')

flag_music = save_data.get('flag_music')
flag_music_is = save_data.get('flag_music_is')
flag_music_buy = save_data.get('flag_music_buy')
flag_music_defoult = save_data.get('flag_music_defoult')
flag_music_hotline_1 = save_data.get('flag_music_hotline_1')
flag_music_is_hotline_1 = save_data.get('flag_music_is_hotline_1')
flag_music_buy_hotline_1 = save_data.get('flag_music_buy_hotline_1')

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
    font_volume = pygame.font.SysFont(None, 96)
    while True:
        screen.blit(background_settings, (0, 0))
        turn_down.draw(screen)
        turn_up.draw(screen)
        back_to_menu_button.draw(screen)
        drawText('Volume', font_volume, screen, 384, 70, WHITE)
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
                take_friend.set_volume(volume)
                game_over.set_volume(volume)
                pygame.mixer.music.set_volume(volume)
            if turn_up.clicked_on_btn():
                if volume <= 1:
                    volume += 0.1
                else:
                    pass
                take_friend.set_volume(volume)
                game_over.set_volume(volume)
                pygame.mixer.music.set_volume(volume)
            if back_to_menu_button.draw(screen):
                menu_after_death()
        if volume == 3.608224830031759e-16:
            screen.blit(zerofrom10, (390, 220))
        elif volume == 0.10000000000000037:
            screen.blit(onefrom10, (390, 220))
        elif volume == 0.20000000000000037:
            screen.blit(twofrom10, (390, 220))
        elif volume == 0.3000000000000004:
            screen.blit(threefrom10, (390, 220))
        elif volume == 0.40000000000000036:
            screen.blit(fourfrom10, (390, 220))
        elif volume == 0.5000000000000003:
            screen.blit(fivefrom10, (390, 220))
        elif volume == 0.6000000000000003:
            screen.blit(sixfrom10, (390, 220))
        elif volume == 0.7000000000000003:
            screen.blit(sevenfrom10, (390, 220))
        elif volume == 0.8000000000000003:
            screen.blit(eightfrom10, (390, 220))
        elif volume == 0.9000000000000002:
            screen.blit(ninefrom10, (390, 220))
        elif volume == 1.0000000000000002:
            screen.blit(volume_img, (390, 220))
        pygame.display.update()

def settings_main_menu():
    global volume
    font_volume = pygame.font.SysFont(None, 96)
    while True:
        screen.blit(background_settings, (0, 0))
        turn_down.draw(screen)
        turn_up.draw(screen)
        back_to_menu_button.draw(screen)
        drawText('Volume', font_volume, screen, 384, 70, WHITE)
        for event in pygame.event.get():
            if event.type == QUIT:
                save_files()
                pygame.quit()
                sys.exit()
            if back_to_menu_button.draw(screen):
                save_files()
                main_menu()
            if turn_down.clicked_on_btn():
                if volume > 3.608224830031759e-16:
                    volume -= 0.1
                else:
                    pass
                take_friend.set_volume(volume)
                game_over.set_volume(volume)
                pygame.mixer.music.set_volume(volume)
            if turn_up.clicked_on_btn():
                if volume <= 1:
                    volume += 0.1
                else:
                    pass
                take_friend.set_volume(volume)
                game_over.set_volume(volume)
                pygame.mixer.music.set_volume(volume)
        if volume == 3.608224830031759e-16:
            screen.blit(zerofrom10, (390, 220))
        elif volume == 0.10000000000000037:
            screen.blit(onefrom10, (390, 220))
        elif volume == 0.20000000000000037:
            screen.blit(twofrom10, (390, 220))
        elif volume == 0.3000000000000004:
            screen.blit(threefrom10, (390, 220))
        elif volume == 0.40000000000000036:
            screen.blit(fourfrom10, (390, 220))
        elif volume == 0.5000000000000003:
            screen.blit(fivefrom10, (390, 220))
        elif volume == 0.6000000000000003:
            screen.blit(sixfrom10, (390, 220))
        elif volume == 0.7000000000000003:
            screen.blit(sevenfrom10, (390, 220))
        elif volume == 0.8000000000000003:
            screen.blit(eightfrom10, (390, 220))
        elif volume == 0.9000000000000002:
            screen.blit(ninefrom10, (390, 220))
        elif volume == 1.0000000000000002:
            screen.blit(volume_img, (390, 220))
        pygame.display.update()

# Функция сохранения
def save_files():
    save_data.save('flag_music_defoult', flag_music_defoult)
    save_data.save('flag_music', flag_music)
    save_data.save('flag_music_is', flag_music_is)
    save_data.save('flag_music_buy', flag_music_buy)
    save_data.save('flag_music_hotline_1', flag_music_hotline_1)
    save_data.save('flag_music_is_hotline_1', flag_music_is_hotline_1)
    save_data.save('flag_music_buy_hotline_1', flag_music_buy_hotline_1)
    save_data.save('flag_game_defoult', flag_game_defoult)
    save_data.save('flag_game', flag_game)
    save_data.save('flag_game_buy', flag_game_buy)
    save_data.save('flag_game_is', flag_game_is)
    save_data.save('max_lvl2', top_score_lvl2)
    save_data.save('max', top_score)
    save_data.save('all', all_scores)
    save_data.save('volume', volume)
    save_data.save('flag_mario', flag_mario)
    save_data.save('flag_rocket', flag_rocket)
    save_data.save('flag_rocket_is', flag_rocket_is)
    save_data.save('flag_rocket_buy', flag_rocket_buy)
    save_data.save('flag_mine', flag_mine)
    save_data.save('flag_mine_is', flag_mine_is)
    save_data.save('flag_mine_buy', flag_mine_buy)

# Покупка предметов
def check(flag_of_check):
    global flag_rocket, flag_mine
    global flag_mine_is, flag_mine_buy
    global flag_rocket_is, flag_rocket_buy, all_scores, flag_game_buy, flag_game_is, flag_game, flag_game_defoult
    global flag_music_defoult, flag_music_buy
    global flag_music_is, flag_music, flag_music_hotline_1
    global flag_music_is_hotline_1, flag_music_buy_hotline_1
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
                        shop()
                    else:
                        no_points = True
                if no_button.clicked_on_btn() or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    shop()
                if back_to_menu_button.clicked_on_btn():
                    shop()
            if flag_of_check == 'mine':
                if yes_button.clicked_on_btn() or (event.type == KEYDOWN and event.key == K_RETURN):
                    if all_scores >= 30:
                        all_scores -= 30
                        flag_mine_is = True
                        flag_mine_buy = False
                        flag_mine = True
                        shop()
                    else:
                        no_points = True
                if no_button.clicked_on_btn() or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    shop()
                if back_to_menu_button.clicked_on_btn():
                    shop()
            if flag_of_check == 'game':
                if yes_button.clicked_on_btn() or (event.type == KEYDOWN and event.key == K_RETURN):
                    if all_scores >= 100:
                        all_scores -= 100
                        flag_game_is = True
                        flag_game_buy = False
                        flag_game = True
                        flag_game_defoult = False
                        flag_music_hotline_1 = False
                        shop()
                    else:
                        no_points = True
                if no_button.clicked_on_btn() or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    shop()
                if back_to_menu_button.clicked_on_btn():
                    shop()
            if flag_of_check == 'music':
                if yes_button.clicked_on_btn() or (event.type == KEYDOWN and event.key == K_RETURN):
                    if all_scores >= 50:
                        all_scores -= 50
                        pygame.mixer.music.load('sounds/undead.mp3')
                        pygame.mixer.music.set_volume(volume)
                        flag_music_is = True
                        flag_music_buy = False
                        flag_music = True
                        flag_music_defoult = False
                        flag_music_hotline_1 = False
                        shop()
                    else:
                        no_points = True
                if no_button.clicked_on_btn() or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    shop()
                if back_to_menu_button.clicked_on_btn():
                    shop()
            if flag_of_check == 'hotline':
                if yes_button.clicked_on_btn() or (event.type == KEYDOWN and event.key == K_RETURN):
                    if all_scores >= 50:
                        all_scores -= 50
                        pygame.mixer.music.load('sounds/hotline_1.mp3')
                        pygame.mixer.music.set_volume(volume)
                        flag_music_is_hotline_1 = True
                        flag_music_buy_hotline_1 = False
                        flag_music_hotline_1 = True
                        flag_music_defoult = False
                        flag_music = False
                        shop()
                    else:
                        no_points = True
                if no_button.clicked_on_btn() or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    shop()
                if back_to_menu_button.clicked_on_btn():
                    shop()
        pygame.display.update()

# Магазин для выбора скинов
def shop():
    global flag_rocket
    global flag_mine
    global flag_mine_buy
    global flag_mine_is
    global flag_rocket_buy
    global flag_rocket_is
    global flag_mario
    global all_scores
    global flag_game_is
    global flag_game_buy
    global flag_game
    global flag_game_defoult
    global flag_music
    global flag_music_is
    global flag_music_buy
    global flag_music_defoult
    global flag_music_hotline_1
    global flag_music_is_hotline_1
    global flag_music_buy_hotline_1
    while True:
        screen.blit(background_shop, (0, 0))
        drawText('Scores: %s' % (all_scores), font, screen, 440, 50, WHITE)
        back_to_menu_button.draw(screen)
        packet_space_button.draw(screen)
        packet_minecraft_button.draw(screen)
        packet_mario_button.draw(screen)
        game_button.draw(screen)
        undead_button.draw(screen)
        game_defoult_button.draw(screen)
        music_defoult_button.draw(screen)
        hotline_1_button.draw(screen)
        # Если предметы не куплены, то отрисовываем картинку с замком и пишем цену
        if flag_rocket_buy:
            packet_space_closed_button.draw(screen)
            drawText('50$', font, screen, 646, 204, WHITE)
        if flag_mine_buy:
            drawText('30$', font, screen, 496, 204, WHITE)
            packet_minecraft_closed_button.draw(screen)
        if flag_game_buy:
            game_closed_button.draw(screen)
            drawText('100$', font, screen, 336, 376, WHITE)
        if flag_music_buy:
            undead_closed_button.draw(screen)
            drawText('50$', font, screen, 696, 376, WHITE)
        if flag_music_buy_hotline_1:
            hotline_1_closed_button.draw(screen)
            drawText('50$', font, screen, 816, 376, WHITE)
        # Отрисовка выбранных Скинов
        if flag_mine:
            packet_minecraft_selected_button.draw(screen)
        elif flag_rocket:
            packet_space_selected_button.draw(screen)
        elif flag_mario:
            packet_mario_selected_button.draw(screen)
        if flag_music:
            undead_selected_button.draw(screen)
        elif flag_music_defoult:
            music_defoult_selected_button.draw(screen)
        elif flag_music_hotline_1:
            hotline_1_selected_button.draw(screen)
        if flag_game:
            game_selected_button.draw(screen)
        elif flag_game_defoult:
            game_defoult_selected_button.draw(screen)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                save_files()
                pygame.quit()
                sys.exit()
            # Backdoor :)
            if event.type == KEYUP and event.key == ord(';'):
                all_scores += 100000
            if back_to_menu_button.draw(screen):
                main_menu()
                
            # Вызываем функцию покупки
            if packet_space_button.clicked_on_btn() and flag_rocket_buy:
                flag_of_check = 'space'
                check(flag_of_check)
            if packet_minecraft_button.clicked_on_btn() and flag_mine_buy:
                flag_of_check = 'mine'
                check(flag_of_check)
            if game_button.clicked_on_btn() and flag_game_buy:
                flag_of_check = 'game'
                check(flag_of_check)
            if undead_button.clicked_on_btn() and flag_music_buy:
                flag_of_check = 'music'
                check(flag_of_check)
            if hotline_1_button.clicked_on_btn() and flag_music_buy_hotline_1:
                flag_of_check = 'hotline'
                check(flag_of_check)

            # Выбираем предмет
            if packet_mario_button.clicked_on_btn():
                flag_mario = True
                flag_mine = False
                flag_rocket = False
            if flag_mine_is:
                if packet_minecraft_button.clicked_on_btn():
                    flag_mine = True
                    flag_rocket = False
                    flag_mario = False
            if flag_rocket_is:
                if packet_space_button.clicked_on_btn():
                    flag_mine = False
                    flag_rocket = True
                    flag_mario = False
            if flag_game_is:
                if game_button.clicked_on_btn():
                    flag_game_defoult = False
                    flag_game = True
            if game_defoult_button.clicked_on_btn():
                flag_game = False
                flag_game_defoult = True
            if flag_music_is:
                if undead_button.clicked_on_btn():
                    pygame.mixer.music.load('sounds/undead.mp3')
                    pygame.mixer.music.set_volume(volume)
                    flag_music = True
                    flag_music_defoult = False
                    flag_music_hotline_1 = False
            if music_defoult_button.clicked_on_btn():
                pygame.mixer.music.load('sounds/music_background.mp3')
                pygame.mixer.music.set_volume(volume)
                flag_music = False
                flag_music_hotline_1 = False

                flag_music_defoult = True
            if flag_music_is_hotline_1:
                if hotline_1_button.clicked_on_btn():
                    pygame.mixer.music.load('sounds/hotline_1.mp3')
                    pygame.mixer.music.set_volume(volume)
                    flag_music_hotline_1 = True
                    flag_music = False
                    flag_music_defoult = False

        pygame.display.flip()

# Функция меню после смерти
def menu_after_death():
    if flag_game_defoult:
        save_data.save('max', top_score)
    elif flag_game:
        save_data.save('max_lvl2', top_score_lvl2)
    save_data.save('all', all_scores)
    pygame.mixer.music.pause()
    death_menu = True
    while death_menu:
        screen.blit(background_image, (0, 0))
        drawText('YOU DIED', font_menu_name, screen, 360, 140, RED)
        pygame.mouse.set_visible(True)
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
                    game()
            if restart_button.draw(screen):
                pygame.mixer.music.unpause()
                game()
            if setting_button.draw(screen):
                    settings_menu_after_death()
            if back_to_menu_button.draw(screen):
                main_menu()

# Меню в которое мы выходим из "меню" при помощи esc или из "меню" после смерти
def main_menu():
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
                game()

            if setting_button.draw(screen):
                settings_main_menu()

            if quit_button.draw(screen):
                save_files()
                pygame.quit()
                sys.exit()

            if shop_button.draw(screen):
                shop()

            pygame.display.flip()


top_score = save_data.get('max')
top_score_lvl2 = save_data.get('max_lvl2')
all_scores = save_data.get('all')

if flag_music_defoult:
    pygame.mixer.music.load('sounds/music_background.mp3')
    pygame.mixer.music.set_volume(volume)
if flag_music:
    pygame.mixer.music.load('sounds/undead.mp3')
    pygame.mixer.music.set_volume(volume)
if flag_music_hotline_1:
    pygame.mixer.music.load('sounds/hotline_1.mp3')
    pygame.mixer.music.set_volume(volume)

running = True
while running:
    screen.fill(LIGHTBLUE)
    drawText('Tiny Spark', font_menu_name, screen, 346, 140, BLUE)

    if start_button.draw(screen):
        pygame.mixer.music.play()
        game()

    if setting_button.draw(screen):
        settings_main_menu()

    if quit_button.draw(screen):
        save_files()
        pygame.quit()
        sys.exit()

    if shop_button.draw(screen):
        shop()

    # Функция гемплея
    def game():
        global top_score
        global top_score_lvl2
        global all_scores
        global flag_game, flag_game_defoult, flag_music, flag_music_defoult
        pygame.mouse.set_visible(False)
        while True:
            if flag_mario:
                player_skin = 'images/items/player_mario.png'
                player_image = pygame.image.load(player_skin)
                player_rect = player_image.get_rect()
                enemy_skin = 'images/items/enemy_mushr.png'
                enemy_image = pygame.image.load(enemy_skin)
                friend_skin = 'images/items/friend_coin.png'
                friend_image = pygame.image.load(friend_skin)

            if flag_mine:
                player_skin = 'images/items/minecraft_steve.jpg'
                player_image = pygame.image.load(player_skin)
                player_rect = player_image.get_rect()
                enemy_skin = 'images/items/minecraft_crepper.jpg'
                enemy_image = pygame.image.load(enemy_skin)
                friend_skin = 'images/items/friend_diamond.png'
                friend_image = pygame.image.load(friend_skin)

            if flag_rocket:
                player_skin = 'images/items/player_rocket.png'
                player_image = pygame.image.load(player_skin)
                player_rect = player_image.get_rect()
                enemy_skin = 'images/items/enemy_asteroid.png'
                enemy_image = pygame.image.load(enemy_skin)
                friend_skin = 'images/items/friend_star.png'
                friend_image = pygame.image.load(friend_skin)

            if flag_game_defoult:
                ENEMYSIZE = 20
                FRIENDSIZE = 35
                ENEMYMAXSIZE = 40
                FRIENDMAXSIZE = 50
                ENEMYMINSPEED = 1
                ENEMYMAXSPEED = 5
                ADDNEWENEMYRATE = 6
                ADDNEWFRIENDRATE = 10
                PLAYERMOVERATE = 4

            if flag_game:
                ENEMYSIZE = 60
                FRIENDSIZE = 25
                ENEMYMAXSIZE = 70
                FRIENDMAXSIZE = 35
                ENEMYMINSPEED = 3
                ENEMYMAXSPEED = 5
                ADDNEWENEMYRATE = 6
                ADDNEWFRIENDRATE = 9
                PLAYERMOVERATE = 4
            
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
                                back_to_menu_button_for_pause.draw(screen)
                                pygame.display.flip()
                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        if flag_game_defoult:
                                            top_score = score
                                        else:
                                            top_score_lvl2 = score
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
                                        if flag_game_defoult:
                                            if score > top_score:
                                                top_score = score
                                        else:
                                            if score > top_score_lvl2:
                                                top_score_lvl2 = score
                                        pygame.mixer.music.unpause()
                                        game()
                                    if back_to_menu_button_for_pause.draw(screen):
                                        if flag_game_defoult:
                                            if score > top_score:
                                                top_score = score
                                        else:
                                            if score > top_score_lvl2:
                                                top_score_lvl2 = score
                                        main_menu()

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

                # Персонаж не выходит за рамки и не поднимался выше половины высоты
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

                # Отрисовка очков
                drawText('Score: %s' % (score), font, screen, 10, 10, WHITE)
                if flag_game_defoult:
                    drawText('Top Score: %s' % (top_score), font, screen, 10, 50, WHITE)
                else:
                    drawText('Top Score: %s' % (top_score_lvl2), font, screen, 10, 50, WHITE)

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
                    if flag_game_defoult:
                        if score > top_score:
                            top_score = score
                    else:
                        if score > top_score_lvl2:
                            top_score_lvl2 = score
                    break
                    
                if flag_game_defoult:
                    screen.fill(BLACK)

                if flag_game:
                    screen.fill(BACKGROUND_COLOR)

                Clock.tick(FPS)

            game_over.play()
            take_friend.stop()
            menu_after_death()

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
