from pygame import * 

FPS = 60
clock= time.Clock()

win_width = 600
win_heigth = 500

back = (200, 255, 255)
window = display.set_mode((win_width, win_heigth))
display.set_caption('Пинг понг')
window.fill(back)

game = True 

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    clock.tick(FPS)