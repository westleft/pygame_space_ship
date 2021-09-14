import pygame
import random

FPS = 60
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH, HEIGHT = 500, 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("肥宅大冒險")
running = True

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2) 
        self.rect.bottom = HEIGHT - 10
        self.speedx = 8

    def update(self):
        key_presses = pygame.key.get_pressed()
        # 左右
        if key_presses[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if key_presses[pygame.K_LEFT]:
            self.rect.x -= self.speedx

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0

        # 上下
        if key_presses[pygame.K_UP]:
            self.rect.y -= self.speedx
        if key_presses[pygame.K_DOWN]:
            self.rect.y += self.speedx

        if self.rect.y > HEIGHT:
            self.rect.y = HEIGHT
        elif self.rect.y < 0:
            self.rect.y = 0

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(2, 10)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right <0:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 10)
            self.speedx = random.randrange(-3, 3)


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for i in range(8):
    r = Rock()
    all_sprites.add(r)

rock = Rock()
all_sprites.add(rock)


while running:
    clock.tick(FPS)  # 一秒最多執行10次(FPS)
    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新遊戲
    all_sprites.update()


    # 畫面顯示
    screen.fill((WHITE)) # RGB
    all_sprites.draw(screen)
    pygame.display.update()


pygame.quit()