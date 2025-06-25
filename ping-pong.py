from pygame import * 

class GameSprite(sprite.Sprite):
    def __init__(self, player_x, player_y, size1, size2,player_image, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size1, size2))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed

    def draw(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_heigth-150:
            self.rect.y += self.speed

    def update_2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_heigth-150:
            self.rect.y += self.speed

FPS = 60
clock= time.Clock()

win_width = 600
win_heigth = 500

back = (200, 255, 255)
window = display.set_mode((win_width, win_heigth))
display.set_caption('Пинг понг')
window.fill(back)

finish = False
game = True 

player_1 = Player(30, 200, 50, 150, 'платформа.png', 10)
player_2 = Player(520, 200, 50, 150, 'платформа.png', 10)
ball = GameSprite(300, 250, 50, 50, 'tennis.png', 4)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        player_1.draw()
        player_2.draw()
        player_1.update_1()
        player_2.update_2()
        ball.draw()

    display.update()
    clock.tick(FPS)
