import pygame as pyg
from pygame.draw import *
import math


def man(plot, x, y, width, height):
    ellipse(plot, COLOR['PURPLE'], (x, y, width, height))
    face(plot, x, y, width, height)
    hand_man(plot, x, y, width, height)
    leg_man(plot, x, y, width, height)


def woman(plot, x, y, width, height):
    # hairs
    circle(plot, COLOR['BROWN'], (x + width // 2, y - height // 5), height // 4)
    rect(plot, COLOR['BROWN'], (x + int(width * 0.08), y - height // 5, height // 2, height // 2))
    polygon(plot, COLOR['PINK'],
            [(x + width // 2, y), (x, y + height), (x + width, y + height)])
    face(plot, x, y, width, height)
    hand_woman(plot, x, y, width, height)
    leg_woman(plot, x, y, width, height)

    
def face(plot, x, y, width, height):
    circle(plot, COLOR['FACE_COLOR'], (x + width // 2, y - height // 6), height // 5)
    eyes(plot, x, y, width, height)
    nose(plot, x, y, width, height)
    mouth(plot, x, y, width, height)
    

def eyes(plot, x, y, width, height):
    circle(plot, COLOR['WHITE'], (x + int(0.33 * width), y - int(0.22 * height)), height // 17)
    circle(plot, COLOR['BLACK'], (x + int(0.33 * width), y - int(0.22 * height)), height // 34)    
    circle(plot, COLOR['WHITE'], (x + int(0.67 * width), y - int(0.22 * height)), height // 17)
    circle(plot, COLOR['BLACK'], (x + int(0.67 * width), y - int(0.22 * height)), height // 34)
        

def nose(plot, x, y, width, height):
    line(plot, COLOR['BLACK'], (x + width // 2, y - int(0.2 * height)), (x + width // 2, y - int(height * 0.2)), 1)
    

def mouth(plot, x, y, width, height):
    arc(plot, COLOR['BLACK'], 
        (x + int(0.35 * width), y - int(0.18 * height), int(0.3 * width), height // 6), 
        1.1 * math.pi, 1.9 * math.pi, 2)
    

def hand_man(plot, x, y, width, height):
    line(plot, COLOR['BLACK'], (x + width // 5, y + height // 10), (x - width // 2, y + int(0.65 * height)), 2)
    line(plot, COLOR['BLACK'], (x + int(0.8 * width), y + height // 10), (x + int(1.6 * width), y + height // 2))

    
def hand_woman(plot, x, y, width, height):
    line(plot, COLOR['BLACK'], 
         (x + width//5, y + height//10), (x - width // 2, y + int(0.65 * height)), 2)
    line(plot, COLOR['BLACK'],
         (x + int(0.75 * width), y + height//10), (x + int(1.3 * width), y + int(0.3 * height)), 2)
    line(plot, COLOR['BLACK'],
         (x + int(1.3 * width), y + int(0.3 * height)), (x + int(1.9 * width), y + height // 4), 2)

    
def leg_man(plot, x, y, width, height):
    line(plot, COLOR['BLACK'],
         (x + width // 3, y + int(0.95 * height)), (x + width // 20, y + int(1.5 * height)), 2)
    line(plot, COLOR['BLACK'],
         (x + width // 20, y + int(1.5 * height)), (x - width // 4, y + int(1.5 * height) + 2), 2)
    line(plot, COLOR['BLACK'],
         (x + 2 * width // 3, y + int(0.95 * height)), (x + 3 * width // 4, y + int(1.49 * height)), 2)
    line(plot, COLOR['BLACK'],
         (x + 3 * width//4, y + int(1.49 * height)), (x + width, y + int(1.5 * height)), 2)
    
    
def leg_woman(plot, x, y, width, height):
    line(plot, COLOR['BLACK'],
            (x + width // 3, y + height), (x - width // 10, y + int(1.45 * height)), 2)
    line(plot, COLOR['BLACK'],
            (x - width // 10, y + int(1.45 * height)), (x - int(0.4 * width), y + int(1.45 * height)), 2)
    line(plot, COLOR['BLACK'],
            (x + int(width * 0.6), y + height), (x + int(width * 0.8), y + int(1.45 * height)), 2)
    line(plot, COLOR['BLACK'],
            (x + int(width * 0.8), y + int(1.45 * height)), (x + int(1.1 * width), y + int(1.5 * height)), 2)
    
    
def balloons(plot, x, y, angle, size=80):
    x2 = int(x - size * math.cos(math.radians(angle)))
    y2 = int(y - size * math.sin(math.radians(angle)))
    x3 = int(x + size * math.cos(math.radians(180 - angle - 60)))
    y3 = int(y - size * math.sin(math.radians(180 - angle - 60)))
    polygon(screen, COLOR['RED'],
            [(x, y), (x2, y2), (x3, y3)])
    circle(plot, COLOR['RED'], (int(0.25*x2 + 0.75*x3), int(0.25*y2 + 0.75*y3)), size//4)
    circle(plot, COLOR['RED'], (int(0.75*x2 + 0.25*x3), int(0.75*y2 + 0.25*y3)), size//4)


def ice_cream(plot, x, y, angle, size):
    x2 = int(x - size * math.cos(math.radians(angle)))
    y2 = int(y - size * math.sin(math.radians(angle)))
    x3 = int(x + size * math.cos(math.radians(180 - angle - 60)))
    y3 = int(y - size * math.sin(math.radians(180 - angle - 60)))
    polygon(screen, COLOR['YELLOW'],
            [(x, y), (x2, y2), (x3, y3)])
    circle(plot, COLOR['BROWN'], (int(0.25 * x2 + 0.75 * x3), int(0.25 * y2 + 0.75 * y3)), size//4)
    circle(plot, COLOR['RED'], (int(0.75 * x2 + 0.25 * x3), int(0.75 * y2 + 0.25 * y3)), size//4)
    x_white = (x2 + x3)/2 - size//4 * math.cos(math.radians(30+angle))
    y_white = (y2 + y3)/2 - size//4 * math.sin(math.radians(30+angle))
    circle(plot, COLOR['WHITE'], (int(x_white), int(y_white)), size//4)


pyg.init()
FPS = 60
COLOR = {
    'GREEN': (55, 200, 113),
    'BLUE': (170, 238, 255),
    'FACE_COLOR': (244, 227, 215),
    'PINK': (255, 85, 221),
    'PURPLE': (167, 147, 172),
    'RED': (255, 0, 0),
    'WHITE': (255, 255, 255),
    'BROWN': (85, 0, 0),
    'YELLOW': (255, 204, 0),
    'BLACK': (0, 0, 0),
}
w, h = 1032, 768

screen = pyg.display.set_mode((w, h))
screen.fill(COLOR['GREEN'])
# sky
rect(screen, COLOR['BLUE'], (0, 0, w, h // 2))

# right couple
man(screen, 130, 380, 100, 170)
woman(screen, 320, 360, 100, 170)
new = pyg.transform.flip(screen, True, False)
screen.blit(new, (0, 0))
# left couple
man(screen, 130, 380, 100, 170)
woman(screen, 320, 360, 100, 170)

line(screen, COLOR['BLACK'], (80, 510), (65, 300), 2)
balloons(screen, 65, 300, 50)

line(screen, COLOR['BLACK'], (w//2, 30+h//2), (20+w//2, h//4), 2)
balloons(screen, 20+w//2, h//4, 60, size=120)

ice_cream(screen, 940, 500, 90, size=80)

# display and quit event handling
pyg.display.update()
clock = pyg.time.Clock()
finished = False

while not finished:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            finished = True
pyg.quit()