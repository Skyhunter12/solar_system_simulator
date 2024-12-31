import pygame as pg
import math
from random import randint

black = (0, 0, 0)
pg.init()
info = pg.display.Info()
window_width = info.current_w 
window_height = info.current_h
screen_display = pg.display.set_mode((window_width-150, window_height-150))
screen_display.fill(black)
pg.display.set_caption("Solar System")

# star list
starlist =[
    {
        'color' : (randint(190, 255), randint(190, 255), randint(190, 255)),
        'radius' : randint(1, 2),
        'position' : (randint(0, window_width-5), randint(0, window_height-5))
    }
    for i in range(490)

]

# draw stars
for star in starlist:
    pg.draw.circle(screen_display, star['color'], star['position'], star['radius'])

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.update()