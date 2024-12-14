
import pygame
from pygame.examples.cursors import image

#Игровые часы
pygame.init()
#Игровые чачы
clock = pygame.time.Clock()
#Самая базовая база
screen = pygame.display.set_mode((1400, 750))
pygame.display.set_caption('Platformer X')
icon = pygame.image.load('images/Platformer_X_icon_demo.png')
pygame.display.set_icon(icon)
picture_orig = pygame.image.load('images/pictures/picture4.jpg')
new_width = int(image.get_width()*11.2)
new_height = int(image.get_height()*37.47)
picture = pygame.transform.scale(picture_orig, (new_width, new_height))

#Далее создаю персонажа
player_right = pygame.image.load('images/Idle/Idle.png')
player_right_rect = player_right.get_rect(center = (0, 9))
player_left = pygame.image.load('images/Idle/Idle2.png')
player_left_rect = player_left.get_rect()


#Функционал для реализации анимации ходьбы
walk_right = [ pygame.image.load('images/right/Walk.png'),
               pygame.image.load('images/right/Walk2.png'),
               pygame.image.load('images/right/Walk3.png'),
               pygame.image.load('images/right/Walk4.png'),
               pygame.image.load('images/right/Walk5.png'),
               pygame.image.load('images/right/Walk6.png'),
               pygame.image.load('images/right/Walk7.png'),
               pygame.image.load('images/right/Walk8.png')
               ]
walk_left = [
               pygame.image.load('images/left/Walk8.png'),
               pygame.image.load('images/left/Walk7.png'),
               pygame.image.load('images/left/Walk6.png'),
               pygame.image.load('images/left/Walk5.png'),
               pygame.image.load('images/left/Walk4.png'),
               pygame.image.load('images/left/Walk3.png'),
               pygame.image.load('images/left/Walk2.png'),
               pygame.image.load('images/left/Walk.png')
            ]



player_anim_count = 0
player_x = 44 #Кордината персонажа по x в начальный момент времени
player_y = 630 # Коридната персонажа по y в начальный момент времени
side = 'right'


#Переменные для прыжка
# jump = [pygame.image.load('images/jump/Jump.png'),
#     pygame.image.load('images/jump/Jump1.png'),
#     pygame.image.load('images/jump/Jump3.png'),
#     pygame.image.load('images/jump/Jump4.png'),
#     pygame.image.load('images/jump/Jump5.png'),
#     pygame.image.load('images/jump/Jump6.png'),
#     pygame.image.load('images/jump/Jump7.png'),
#     pygame.image.load('images/jump/Jump8.png'),
#     pygame.image.load('images/jump/Jump9.png'),
#     pygame.image.load('images/jump/Jump10.png'),
#     pygame.image.load('images/jump/Jump11.png'),
#     pygame.image.load('images/jump/Jump12.png')
# ]
jump_count = 30
space = False


#Функция для прыжка
def jump():
    global player_y, jump_count, is_jump
    if jump_count >= -30:
        player_y -= jump_count / 2
        jump_count -= 2
    else:
        jump_count =30
        is_jump = False

is_jump = False

#Объекты в игре
block = pygame.Surface((100, 50))
block.fill((255, 255, 255))
block_rect = block.get_rect()

#Отдельная переменная для закрытия игры черезе ее окно
flag = 0

#Сам цикл для создания игры
while flag == 0:

    #ъ9Задаю начальные параметры для дисплея
    pygame.display.update()
    screen.blit(picture, (0, 0))
    screen.blit(block, (500, 600))
    keys = pygame.key.get_pressed()#Массив хранящий данные о нажатых клавишах
    pygame.draw.rect(screen, (255, 255, 255), player_right_rect, 2)
    #Далее все касательно движения
    if keys[pygame.K_LEFT] and player_x >= 44:  #Обращаюсь к клавише LEFT и проверяю нажата ли она
        side = 'left'
        player_x -= 6
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    elif keys[pygame.K_RIGHT] and player_x <= 1320: #Обращаюсь к клавише RIGTH и проверяю нажата ли она
        side = 'right'
        player_x += 6
        if is_jump == False:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))
        else:
            screen.blit(player_right, (player_x, player_y))
    else: # Если ничего не нажато, то персонаж стачен и не двигается
        if side == 'right':
            screen.blit(player_right, (player_x, player_y))
        elif side == 'left':
            screen.blit(player_left, (player_x, player_y))

    #Счетчик кадров для того, чтобы была анимация ходьбы
    if player_anim_count == 7:
        player_anim_count = 0
    else:
        player_anim_count += 1

    #Отдельно от отсальных команд я реализую прыжок
    if keys[pygame.K_SPACE]:
        is_jump = True
        default_y = player_y
    if is_jump:
        jump()

    if player_right_rect.colliderect(block_rect):
        if player_right_rect.left >= block_rect.left and player_right_rect.right <= block_rect.right:
            if player_right_rect.bottom >= block_rect.top:
                player_y = block_rect.y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = 1
            pygame.quit()
    clock.tick(30)




