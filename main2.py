from idlelib.pyshell import restart_line

import pygame


pygame.init()

#set frame rate
clock = pygame.time.Clock()
FPS = 60
#size of one block
tile_size = 40
#game window chatacteristics
screen_width = 1400
screen_height = 750
#create game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tryer')
#images
picture = pygame.image.load('images/pictures/Picture4.jpg')
restart_image = pygame.image.load('images/objects/button/restart_button.png')
#game_over
game_over = 0
def game_over_f():
    game_over_img = pygame.image.load('images/pictures/game_over.png')
    game_over_img = pygame.transform.scale(game_over_img, (screen_width, screen_height))
    screen.blit(game_over_img, (0, 0))

def text(output, x, y):
    text_score = font.render(output, True, (255, 255, 255))
    screen.blit(text_score, (x, y))

#score

score_count = 0
font = pygame.font.Font(None, 36)

#time
start_ticks = pygame.time.get_ticks()
def time():
    elapsed_ms = pygame.time.get_ticks() - start_ticks
    elapsed_sec = elapsed_ms // 1000  # Общее количество секунд
    minutes = elapsed_sec // 60
    seconds = elapsed_sec % 60
    return (text(str(minutes)+' : ' + str(seconds), 700, 5))

#here is grid for my project
# def draw_grid():
#     for line in range(0, 35):
#         pygame.draw.line(screen, (255, 255, 255), (tile_size*line, 0), (tile_size*line, screen_height))
#     for line in range(0, 21):
#         pygame.draw.line(screen, (255, 255, 255), (0, 35.5*line), (screen_width, 35.5*line))

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.image_rect = self.image.get_rect()
        self.image_rect.x = x
        self.image_rect.y = y
    def draw(self):
        screen.blit(self.image, self.image_rect)

restart_button = Button(620, 450, restart_image)

class World():
    def __init__(self, data):
        self.tile_list = []
        object = pygame.image.load('images/objects/object1.png')
        spike_img = pygame.image.load('images/objects/spike_block.png')
        lava_img = pygame.image.load('images/objects/Lava.png')
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    block = pygame.transform.scale(object, (tile_size, 35.5))
                    block_rect = block.get_rect()
                    block_rect.x = col_count*tile_size
                    block_rect.y = row_count*35.5
                    self.tile_list.append((block, block_rect, tile))
                if tile == 2:
                    spike = pygame.transform.scale(spike_img, (tile_size, 49))
                    spike_rect = spike.get_rect()
                    spike_rect.x = col_count*tile_size
                    spike_rect.y = row_count*34
                    self.tile_list.append((spike, spike_rect, tile))
                if tile == 3:
                    lava = pygame.transform.scale(lava_img, (tile_size*3, 17))
                    lava_rect = lava.get_rect()
                    lava_rect.x = col_count*tile_size
                    lava_rect.y = row_count*36.35
                    self.tile_list.append((lava, lava_rect, tile))
                col_count += 1
            row_count += 1
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)


world_data = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 4, 0, 4, 0, 4, 0, 0, 0, 0, 1, 3, 3, 3, 3, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

]
world = World(world_data)


#button
# class Button():
#     def __init__(self, x, y):
#         self.button_active = []
#         self.index = 0
#         for num in range(0, 3):
#             img = pygame.image.load(f'images/objects/button/button{num}.png')
#             img = pygame.transform.scale(img, (50, 15))
#             self.button_active.append(img)
#         self.button = self.button_active[self.index]
#         self.button_rect = self.button.get_rect()
#         self.button_rect.center = (x, y)
#
#     def draw(self):
#         screen.blit(self.button, self.button_rect)
#         pygame.draw.rect(screen, (255, 255, 255), self.button_rect, 2)

class Coin():
    def __init__(self, x, y):
        self.coin = pygame.image.load('images/coin.png')
        self.coin = pygame.transform.scale(self.coin, (30, 30))
        self.coin_rect = self.coin.get_rect()
        self.coin_rect.center = (x, y)
        self.get = 0
    def draw(self):
        screen.blit(self.coin, self.coin_rect)
        pygame.draw.rect(screen, (255, 255 ,255), self.coin_rect, 2)

coin1 = Coin(780, 620)
coin2 = Coin(1320, 585)
coin3 = Coin(125, 290)
coin4 = Coin(560, 240)
coin5 = Coin(1200, 150)
coin = [coin1, coin2, coin3, coin4, coin5]

class Platform():
    def __init__(self, x, y):
        self.platform = pygame.image.load('images/objects/Platform.png')
        self.platform = pygame.transform.scale(self.platform, (150, 40))
        self.platform_rect = self.platform.get_rect()
        self.platform_rect.center = (x, y)
    def draw(self):
        screen.blit(self.platform, self.platform_rect)
        pygame.draw.rect(screen, 'Red', self.platform_rect, 2)
#player
class Player():
    def __init__(self, x, y):
        #base variables
        self.walk_right = []
        self.index = 0
        self.counter = 0
        self.player_static = pygame.image.load('images/Pers1/Walk0.png')
        self.walk_right.append(pygame.transform.scale(self.player_static, (30, 60)))
        #images if walk
        for num in range(1, 9):
            img_right = pygame.image.load(f'images/Pers1/Walk{num}.png')
            img_right = pygame.transform.scale(img_right, (30, 60))
            self.walk_right.append(img_right)
        self.player = self.walk_right[self.index]
        self.player_rect = self.player.get_rect()
        self.width = self.player.get_width()
        self.height = self.player.get_height()
        self.player_rect.center = (x, y)
        self.vel_y = 0
        self.flip = False
        self.jump = False
        self.is_jump = False
    #fuction thaw draw my character and all that associated with him
    def draw(self):
        #Here is static player and his rectangle
        screen.blit(pygame.transform.flip(self.player, self.flip, False), self.player_rect)
        pygame.draw.rect(screen, (255, 255, 255), self.player_rect, 2)
    #funtion that desribes moves of character
    def move(self):
        global game_over
        global score_count
        dx = 0
        dy = 0
        walk_cooldown = 3
        # Here is actions if someone press any key
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.jump == False:
            self.vel_y = -20
            self.jump = True
            self.is_jump = True
        if keys[pygame.K_SPACE] == False:
            self.jump = False
        if keys[pygame.K_LEFT] and self.player_rect.left > 40:
            if self.is_jump == True:
                dx -= 5
                self.counter += 1.5
            else:
                dx -= 4
                self.counter += 1
            self.flip = True
        if keys[pygame.K_RIGHT] and self.player_rect.right < 1360:
            if self.is_jump == True:
                dx += 5
                self.counter += 1.5
            else:
                dx += 4
                self.counter += 1
            self.flip = False
        if keys[pygame.K_LEFT] == False and keys[pygame.K_RIGHT] == False:
            self.counter = 0
            self.index = 0
            self.player = self.walk_right[self.index]


        #here is an animation of walk:
        if self.counter > walk_cooldown:
            self.index += 1
            if self.index >= len(self.walk_right):
                self.index = 1
            self.player = self.walk_right[self.index]
            self.counter = 0

        #describe of jump
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y//1.7
        if self.player_rect.top < 40:
            dy = 40 - self.player_rect.top
            self.vel_y = 0



#COLLUSION CHECK OF COLLUSON CHECK OF COLLUSION CHECK OF COLLUSION COLLUSION CHECK OF COLLUSON CHECK OF COLLUSION CHECK OF
        dt = 0
        for tile in world.tile_list:
            dt += 1
            #collusion for y
            if tile[1].colliderect(self.player_rect.x, self.player_rect.y + dy, self.width, self.height) and (tile[2] == 3 or tile[2] == 2):
                if tile[2] == 3:
                    game_over = -1
                if tile[2] == 2 and self.vel_y >= 0:
                    game_over = -1
            if tile[1].colliderect(self.player_rect.x, self.player_rect.y + dy, self.width, self.height) and tile[2] != 3:
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.player_rect.top
                    self.vel_y = 0
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.player_rect.bottom
                    self.is_jump = False
            #collusion for x
            if tile[1].colliderect(self.player_rect.x + dx, self.player_rect.y, self.width, self.height) and tile[2] != 3 and tile[2] != 4:
              dx = 0
#COLLUSION CHECK OF COLLUSON WITH COIN #COLLUSION CHECK OF COLLUSON WITH COIN #COLLUSION CHECK OF COLLUSON WITH COIN
        for i in range(0, 5):
            if coin[i].coin_rect.colliderect(self.player_rect.x, self.player_rect.y + dy, self.width, self.height) or coin[i].coin_rect.colliderect(self.player_rect.x + dx, self.player_rect.y, self.width, self.height):
                coin[i].get = -1
                coin[i].coin_rect.center = (0, 0)
                score_count += 1

#COLLUSION CHECK OF COLLUSON WITH PLATFORM COLLUSION CHECK OF COLLUSON WITH PLATFORM COLLUSION CHECK OF COLLUSON WITH PLATFORM
        platform = Platform(120, 334)
        platform.draw()
        if platform.platform_rect.colliderect(self.player_rect.x + dx, self.player_rect.y, self.width, self.height):
            dx = 0
        if platform.platform_rect.colliderect(self.player_rect.x, self.player_rect.y + dy, self.width, self.height):
            # if self.vel_y < 0:
            #     dy = platform.platform_rect.bottom - self.player_rect.top
            #     self.vel_y = 0

            if self.vel_y >= 0:
                dy = platform.platform_rect.top - self.player_rect.bottom

        self.player_rect.x += dx
        self.player_rect.y += dy

        if self.player_rect.bottom > screen_height-40:
            self.player_rect.bottom = screen_height-40
            self.is_jump = False


# class Player2():
#     def __init__(self, x, y):
#         #base variables
#         self.walk_right = []
#         self.index = 0
#         self.counter = 0
#         self.player_static = pygame.image.load('images/Pers2/Idle.png')
#         self.walk_right.append(pygame.transform.scale(self.player_static, (30, 60)))
#         #images if walk
#         for num in range(1, 9):
#             img_right = pygame.image.load(f'images/Pers2/Walk{num}.png')
#             img_right = pygame.transform.scale(img_right, (30, 60))
#             self.walk_right.append(img_right)
#         self.player = self.walk_right[self.index]
#         self.player_rect = self.player.get_rect()
#         self.width = self.player.get_width()
#         self.height = self.player.get_height()
#         self.player_rect.center = (x, y)
#         self.vel_y = 0
#         self.flip = False
#         self.jump = False
#         self.is_jump = False
#     #fuction thaw draw my character and all that associated with him
#     def draw(self):
#         #Here is static player and his rectangle
#         screen.blit(pygame.transform.flip(self.player, self.flip, False), self.player_rect)
#         pygame.draw.rect(screen, (255, 255, 255), self.player_rect, 2)
#     #funtion that desribes moves of character
#     def move(self):
#         dx = 0
#         dy = 0
#         walk_cooldown = 3
#         # Here is actions if someone press any key
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_w] and self.jump == False:
#             self.vel_y = -22
#             self.jump = True
#             self.is_jump = True
#         if keys[pygame.K_w] == False:
#             self.jump = False
#         if keys[pygame.K_a] and self.player_rect.left > 40:
#             if self.is_jump == True:
#                 dx -= 5
#                 self.counter += 1.5
#             else:
#                 dx -= 4
#                 self.counter += 1
#             self.flip = True
#         if keys[pygame.K_d] and self.player_rect.right < 1360:
#             if self.is_jump == True:
#                 dx += 5
#                 self.counter += 1.5
#             else:
#                 dx += 4
#                 self.counter += 1
#             self.flip = False
#         if keys[pygame.K_a] == False and keys[pygame.K_d] == False:
#             self.counter = 0
#             self.index = 0
#             self.player = self.walk_right[self.index]
#
#
#         #here is an animation of walk:
#         if self.counter > walk_cooldown:
#             self.index += 1
#             if self.index >= len(self.walk_right):
#                 self.index = 1
#             self.player = self.walk_right[self.index]
#             self.counter = 0
#
#         #describe of jump
#         self.vel_y += 1
#         if self.vel_y > 10:
#             self.vel_y = 10
#         dy += self.vel_y//2
#         if self.player_rect.top < 40:
#             dy = 40 - self.player_rect.top
#             self.vel_y = 0
#
#         # check for collusion
#         for tile in world.tile_list:
#             #collusion for y
#             if tile[1].colliderect(self.player_rect.x, self.player_rect.y + dy, self.width, self.height):
#                 if self.vel_y < 0:
#                     dy = tile[1].bottom - self.player_rect.top
#                     self.vel_y = 0
#                 elif self.vel_y >= 0:
#                     dy = tile[1].top - self.player_rect.bottom
#                     self.is_jump = False
#
#             #collusion for x
#             if tile[1].colliderect(self.player_rect.x + dx, self.player_rect.y, self.width, self.height):
#               dx = 0
#
#
#         platform = Platform(120, 334)
#         platform.draw()
#         if platform.platform_rect.colliderect(self.player_rect.x + dx, self.player_rect.y, self.width, self.height):
#             dx = 0
#         if platform.platform_rect.colliderect(self.player_rect.x, self.player_rect.y + dy, self.width, self.height):
#             # if self.vel_y < 0:
#             #     dy = platform.platform_rect.bottom - self.player_rect.top
#             #     self.vel_y = 0
#
#             if self.vel_y >= 0:
#                 dy = platform.platform_rect.top - self.player_rect.bottom
#
#
#
#
#
#         # if button.button_rect.colliderect(self.player_rect):
#         #     self.player_rect.y = 500
#
#
#         self.player_rect.x += dx
#         self.player_rect.y += dy
#
#         if self.player_rect.bottom > screen_height-40:
#             self.player_rect.bottom = screen_height-40
#             self.is_jump = False




#active class Player in player
player1 = Player(60, 670)
# player2 = Player2(60, 580)

#game start
run = True
while run:
    clock.tick(60)
    #display something in the window of my game
    screen.blit(picture, (0, 0))
    #grid
    # draw_grid()
    #draw sprites
    # player2.draw()
    # player2.move()
    #draw objects
    world.draw()
    for i in range(0, 5):
        if coin[i].get == 0:
            coin[i].draw()
    player1.draw()
    text('Score: ' + str(score_count), 10, 5)
    if game_over != -1:
        player1.move()
        time()
    else:
        game_over_f()
        restart_button.draw()
    #close and stop the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update display
    pygame.display.update()

pygame.quit()