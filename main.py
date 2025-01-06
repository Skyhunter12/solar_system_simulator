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
    AU=1.496e11
    SCALE=274 / AU
    G = 6.6743e-11
    FPS = 60
    def __init__(self, name, color, x, y, mass, radius):
        self.name = name
        self.mass = mass
        self.color = color
        self.x = x
        self.y = y
        # self.speed = speed
        self.radius = radius
        self.orbit = []
        self.x_vel = 0
        self.y_vel = 0
        self.TIME_STEP = 60*60*24
        
        # distance_to_center = math.sqrt(self.x**2 + self.y**2) or 1
        # orbital_velocity = math.sqrt(self.G * mass / distance_to_center)
        # self.x_vel = -orbital_velocity * (self.y / distance_to_center)
        # self.y_vel = orbital_velocity * (self.x / distance_to_center)

    def draw(self, WINDOW):
        x=self.x * SolarSystem.SCALE + window_width//2
        y=self.y * SolarSystem.SCALE + window_height//2
        pg.draw.circle(surface=WINDOW, color=self.color, center=(int(x), int(y)), radius=self.radius)

    def gravity_between_mass(self, body):
        # f =GMm/r^2
        x_diff = body.x - self.x 
        y_diff = body.y - self.y 
        distance = math.sqrt(x_diff**2 + y_diff**2)
        if distance == 0:
            return 0, 0
        force = SolarSystem.G * self.mass * body.mass / distance**2
        theta = math.atan2(y_diff, x_diff)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y
    
    def update_position(self, ss_bodies):
        net_fx, net_fy = 0, 0
        for ss_body in ss_bodies:
            if(self != ss_body):
                f_x, f_y = self.gravity_between_mass(ss_body)
                net_fx += f_x
                net_fy += f_y
        self.x_vel += net_fx / self.mass * self.TIME_STEP
        self.y_vel += net_fy / self.mass * self.TIME_STEP 
        self.x += self.x_vel * self.TIME_STEP
        self.y += self.y_vel * self.TIME_STEP
        self.orbit.append((self.x, self.y))
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
mercury.y_vel = -47.87e3
venus = SolarSystem('Venus', YELLOWISH_WHITE, 0.72*SolarSystem.AU, 0, 4.867e24, 14)
venus.y_vel = -35e3
earth = SolarSystem('Earth', BLUE, 1*SolarSystem.AU, 0, 5.972e24, 15)
earth.y_vel = -29.8e3
mars = SolarSystem('Mars', RED, 1.52*SolarSystem.AU, 0, 6.39e23, 8)
mars.y_vel = -24.1e3
# draw stars
def draw_stars(starlist):
    for star in starlist:
        pg.draw.circle(screen_display, star['color'], star['position'], star['radius'])

run = True
paused = False
while run:
    clock = pg.time.Clock()
    clock.tick(SolarSystem.FPS)
    screen_display.fill(black)
    draw_stars(starlist)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False
            elif event.key == pg.K_SPACE:
                paused = not paused
    if not paused:
        ss_bodies=[sun, mercury, venus, earth, mars]
        for body in ss_bodies:
            body.update_position(ss_bodies)
            body.draw(screen_display)
        pg.display.update()