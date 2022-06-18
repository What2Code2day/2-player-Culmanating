import pygame, sys
from pygame.locals import *
# World Generation
class World():
    def __init__(self, data):
        self.tile_list = []

        #load images
        platform_img = pygame.image.load('pixilart-drawing.png')


        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(platform_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

# Handling the player
class player():
    def __init__(self, x, y, speedx):
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = 10
        self.vel_y = 0
        self.health = 100
        self.width = 80
        self.height = 180
        self.jump = False
        dx = 0
        dy = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def move_right(self):
        newx = self.x+self.speedx
        self.ghost = pygame.Rect(newx, self.y, self.width, self.height)
        for tile in world.tile_list:
            if self.ghost.colliderect(tile[1]):
                return
        self.x = newx

    def move_left(self):
        newx = self.x-self.speedx
        self.ghost = pygame.Rect(newx, self.y, self.width, self.height)
        for tile in world.tile_list:
            if self.ghost.colliderect(tile[1]):
                return
        self.x = newx
      
                
    def move_up(self):
        newy = self.y-150
        self.ghost = pygame.Rect(self.x, newy, self.width, self.height)
        for tile in world.tile_list:
            if self.ghost.colliderect(tile[1]):
                return
        self.y = newy
        print('up')

    def move_down(self):
        newy = self.y+self.speedy
        self.ghost = pygame.Rect(self.x, newy, self.width, self.height)
        for tile in world.tile_list:
            if self.ghost.colliderect(tile[1]):
                return
        self.y = newy

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
            #print('v')


# draws a grid on the screen for refrence
def draw_grid():
    for line in range(0, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))

# Making the Text appear on the screen
def print_text(text, x, y, font, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

# Setting up the window
pygame.init()
clock = pygame.time.Clock()
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tag")
tile_size = 50
# Healthbar decay rate
LOWERHEALTHBAR = pygame.event.custom_type()
pygame.time.set_timer(LOWERHEALTHBAR, 70)
# Making the players
playerA = player(50,screen_height/2-90, 10)
playerB = player(850,screen_height/2-90, 10)
playerA.rect
playerB.rect
# Making the healthbars
playerA_healthbar = pygame.Rect(20, 50, 250, 30)
playerA_healthbar_back = pygame.Rect(10, 40, 270, 50)
playerB_healthbar = pygame.Rect(screen_width-270, 50, 250, 30)
playerB_healthbar_back = pygame.Rect(screen_width-280, 40, 270, 50)
# Fonts and endgame text
font_small = pygame.font.SysFont('Lucida Sans', 40)
font_big = pygame.font.SysFont('Lucida Sans', 80)  
game_over = False
# Making the world
world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
world = World(world_data)



while True:
    if game_over == False:

        #Drawing the Background/World
        screen.fill(pygame.Color('gray12'))
        world.draw()

        #Making the Healthbars go down
        
        playerB_healthbar_width = playerB_healthbar.width
        if playerA.rect.colliderect(playerB):
            playerA_healthbar = playerA_healthbar.inflate(-1,0)
            if not playerB_healthbar_width >= 250:
                print(playerB_healthbar_width)
                playerB_healthbar = playerB_healthbar.inflate(+1,0)    
        if playerA_healthbar.right <= 0:
            print('GAME OVER, ', 'Player A')
            game_over = True
        if playerB_healthbar_width <= 0:
            print('GAME OVER, ', 'Player B')
            game_over = True


        # Handling the Events

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == LOWERHEALTHBAR:
                    playerB_healthbar = playerB_healthbar.inflate(-1,0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerA.move_left()
        if keys[pygame.K_RIGHT]:
            playerA.move_right()
        if keys[pygame.K_a]:
            playerB.move_left()
        if keys[pygame.K_d]:
            playerB.move_right()
        if keys[pygame.K_UP]:
            playerA.move_up()
        if keys[pygame.K_w]:
            playerB.move_up()


        #Drawing the Players and healthbars
        playerB.update()
        playerB.move_down()
        playerA.move_down()
        playerA.update()
        pygame.draw.rect(screen, (30,199,250), playerA.rect)
        pygame.draw.rect(screen, (255,10,10), playerB) 
        pygame.draw.rect(screen, (255,10,10), playerB)   
        pygame.draw.rect(screen, (0,0,0), playerA_healthbar_back)
        pygame.draw.rect(screen, (30,199,250), playerA_healthbar)
        pygame.draw.rect(screen, (0,0,0), playerB_healthbar_back)
        pygame.draw.rect(screen, (255,10,10), playerB_healthbar)
    else:
        print_text('GAME OVER', screen_width/2 -(80*3), screen_height/3, font_big)
        print_text('PRESS SPACE TO PLAY AGAIN', screen_width/2 -(40*7), screen_height/2.5 + 50, font_small)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    game_over = False
                    playerA_healthbar = pygame.Rect(20, 50, 250, 30)
                    playerB_healthbar = pygame.Rect(screen_width-270, 50, 250, 30)
                    playerA = player(50,screen_height/2-90,10)
                    playerB = player(850,screen_height/2-90,10)
       
        
    
    pygame.display.update()
    clock.tick(60)
