import pygame

pygame.init()
pygame.font.init()
info = pygame.display.Info()
width = int(info.current_w * 0.75)
height = int(width * 0.5)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image,w, h, x, y, speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image),(w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y  
    def draw(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < height - 155:
            self.rect.y += self.speed

class Player2(GameSprite):
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < height - 155:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global lost
        self.rotate += self.angel
        self.rect.y += self.speed
        if self.rect.y > height:
            lost += 1
            self.rect.y = -100
            self.rect.x = randint(5, int(0.9 * width))

win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ping-Pong🏓')

player1 = Player1('rocket1.png', 90 , 150, 925, 150, 5)
player2 = Player2('rocket2.png', 90, 150, 10, 150, 5)
ball = Player('ball.png', int(width * 0.45), int(height * 0.80), 5)

win.fill((33,66,30))

end_text = pygame.font.SysFont('segoeui', 65)
clock = pygame.time.Clock()
game = True
finish = False

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
   
    win.fill((170,255,200))
   
    if not finish:
        player1.move()
        player1.draw()
        player2.move()
        player2.draw()
       
        ball.move()
        ball.draw() 

    if finish:
        win.fill((67,75,27))

    pygame.display.update()
    clock.tick(60)
