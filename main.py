import pygame as pg
import math
from random import randint

black = (0, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
YELLOWISH_WHITE = (255, 255, 240)
BLUE = (0, 0, 255)
RED = (188, 39, 50)

pg.init()
info = pg.display.Info()
window_width = info.current_w 
window_height = info.current_h
screen_display = pg.display.set_mode((window_width-150, window_height-150))
screen_display.fill(black)
pg.display.set_caption("Solar System")

class SolarSystem:
    AU=1496e11
    SCALE=285 / AU
    def __init__(self, name, color, x, y, mass, radius):
        self.name = name
        self.mass = mass
        self.color = color
        self.x = x
        self.y = y
        # self.speed = speed
        self.radius = radius
    
    def draw(self, WINDOW):
        x=self.x * SolarSystem.SCALE + window_width//2
        y=self.y * SolarSystem.SCALE + window_height//2
        pg.draw.circle(surface=WINDOW, color=self.color, center=(int(x), int(y)), radius=self.radius)
# star list
starlist =[
    {
        'color' : (randint(190, 255), randint(190, 255), randint(190, 255)),
        'radius' : randint(1, 2),
        'position' : (randint(0, window_width-5), randint(0, window_height-5))
    }
    for i in range(490)

]

sun = SolarSystem("Sun", YELLOW, 0, 0, 1.989e30, 30)
mercury = SolarSystem('Mercury', GRAY, 0.39*SolarSystem.AU, 0, 3.285e23, 6)
venus = SolarSystem('Venus', YELLOWISH_WHITE, 0.72*SolarSystem.AU, 0, 4.867e24, 14)
earth = SolarSystem('Earth', BLUE, 1*SolarSystem.AU, 0, 5.972e24, 15)
mars = SolarSystem('Mars', RED, 1.52*SolarSystem.AU, 0, 6.39e23, 8)
# draw stars
for star in starlist:
    pg.draw.circle(screen_display, star['color'], star['position'], star['radius'])

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    ss_bodies=[sun, mercury, venus, earth, mars]
    for body in ss_bodies:
        body.draw(screen_display)
    pg.display.update()