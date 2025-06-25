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

speed_x = 3
speed_y = 3

font.init()
font = font.Font(None,35)
lose1 = font.render('Player 1 lose!', True, (180,0,0))
lose2 = font.render('Player 2 lose!', True, (180,0,0))

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
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_heigth-50 or ball.rect.y <0 :
            speed_y *= -1
        if sprite.collide_rect(player_1,ball) or sprite.collide_rect(player_2,ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,(200,200))
        if ball.rect.x > win_width-50:
            finish = True
            window.blit(lose2,(200,200))


    display.update()
    clock.tick(FPS)
