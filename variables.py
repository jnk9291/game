from os import path
import pygame as pg
from boss import *
from player import Player0, Player3

all_sprites = pg.sprite.Group()
MOB_SIZE = 32
MAX_SPEED = 4
MAX_FORCE = 0.4
RAND_TARGET_TIME = 500
WANDER_RING_DISTANCE = 100
WANDER_RING_RADIUS = 20
WANDER_TYPE = 2
vec = pg.math.Vector2
b = boss01()
gamefolder = path.abspath(__file__)
imgfolder = path.join(path.dirname(__file__), "assets","img")
sndfolder = path.join(path.dirname(__file__), "assets","snd")
all_sprites = pg.sprite.Group()
bullets = pg.sprite.Group()
enemies = pg.sprite.Group()
danmakuBullets = pg.sprite.Group()
players = pg.sprite.Group()
height = 960
width =  720
screen = pg.display.set_mode((960, 720))
screen_rect = screen.get_rect()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
spell = False
nonspell = True
INC_SPEED = pg.USEREVENT + 1
pg.time.set_timer(INC_SPEED, 1000)
SPEED = 5
SCORE = 0
white = ((255,255,255))
blue = ((0,0,255))
green = ((0,255,0))
red = ((255,0,0))
black = ((0,0,0))
orange = ((255,100,10))
yellow = ((255,255,0))
blue_green = ((0,255,170))
marroon = ((115,0,0))
lime = ((180,255,100))
pink = ((255,100,180))
purple = ((240,0,255))
gray = ((127,127,127))
magenta = ((255,0,230))
brown = ((100,40,0))
forest_green = ((0,50,0))
navy_blue = ((0,0,100))
rust = ((210,150,75))
dandilion_yellow = ((255,200,0))
highlighter = ((255,255,100))
sky_blue = ((0,255,255))
light_gray = ((200,200,200))
dark_gray = ((50,50,50))
tan = ((230,220,170))
coffee_brown =((200,190,140))
moon_glow = ((235,245,255))
playerGroup = random.choice([1,2])
player = None
if playerGroup == 1:
    player = Player0()
else:
    player = Player3()