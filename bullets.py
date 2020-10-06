import pygame as pg
from variables import *
from pygame.math import Vector2

from functions import *

class Bullet0(pg.sprite.Sprite):
    def __init__(self, x, y, xspd , yspd):
        pg.sprite.Sprite.__init__(self)
        self.images = load_image(0,3,"bullet")        
        self.index = 0
        self.indextimer = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = yspd
        self.speedx = xspd
        self.radius = int(self.rect.width * .40 / 2)
        
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom > height:
            self.kill()
        self.indextimer +=1            
        if self.indextimer % 5 == 0:
            self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]

class Bullet1(pg.sprite.Sprite):
    def __init__(self, x, y, xspd , yspd):
        pg.sprite.Sprite.__init__(self)
        self.image = load_image(0,0,"bullet4")
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = yspd
        self.speedx = xspd
        self.radius = int(self.rect.width * .40 / 2)
        
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom > height:
            self.kill()

class Bullet2(pg.sprite.Sprite):
    def __init__(self, pos, target, screen_rect):
        pg.sprite.Sprite.__init__(self)
        self.image = load_image(0,0,"bullet5")
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .40 / 2)
        self.position = Vector2(pos)  # The position of the bullet.

        # This vector points from the mouse pos to the target.
        direction = target - pos
        # The polar coordinates of the direction vector.
        radius, angle = direction.as_polar()
        # Rotate the image by the negative angle (because the y-axis is flipped).
        self.image = pg.transform.rotozoom(self.image, -angle, 1)
        # The velocity is the normalized direction vector scaled to the desired length.
        self.velocity = direction.normalize() * 30
        self.screen_rect = screen.get_rect()
    def update(self):
        self.position += self.velocity  # Update the position vector.
        self.rect.center = self.position  # And the rect.

        # Remove the bullet when it leaves the screen.
        if not self.screen_rect.contains(self.rect):
            self.kill()
        if self.rect.bottom > height:
            self.kill()

class Bullet3(pg.sprite.Sprite):
    def __init__(self, x, y, xspd , yspd):
        pg.sprite.Sprite.__init__(self)
        self.images = load_image(8,10,"bullet")        
        self.index = 0
        self.indextimer = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = yspd
        self.speedx = xspd
        self.radius = int(self.rect.width * .40 / 2)
        
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom > height:
            self.kill()
        self.indextimer +=1            
        if self.indextimer % 5 == 0:
            self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]


class Bullet4(pg.sprite.Sprite):
    def __init__(self, x, y, xspd , yspd):
        pg.sprite.Sprite.__init__(self)
        self.images = load_image(6,7,"bullet")        
        self.index = 0
        self.indextimer = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = yspd
        self.speedx = xspd
        self.radius = int(self.rect.width * .40 / 2)
        
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom > height:
            self.kill()
        self.indextimer +=1            
        if self.indextimer % 5 == 0:
            self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]
