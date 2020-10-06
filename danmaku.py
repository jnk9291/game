import pygame as pg
from variables import *
from pygame import Vector2
from functions import *
import random

class star(pg.sprite.Sprite):
    def __init__(self, x, y, xspd , yspd):
        pg.sprite.Sprite.__init__(self)
        self.image = random.choice(load_image(0,2,"star"))        
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = yspd
        self.speedx = xspd
        self.radius = int(self.rect.width * .40 / 2)
        self.shoottime = 150
        self.last = pg.time.get_ticks()
        self.angle = 0
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.angle += 5 % 360
        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.


class arrowhead(pg.sprite.Sprite):
    def __init__(self, pos, target, screen_rect):
        pg.sprite.Sprite.__init__(self)
        self.image = load_image(0,0,"ahead")
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
        self.velocity = direction.normalize() * 9
        self.screen_rect = screen.get_rect()
    def update(self):
        self.position += self.velocity  # Update the position vector.
        self.rect.center = self.position  # And the rect.

        # Remove the bullet when it leaves the screen.
        if not self.screen_rect.contains(self.rect):
            self.kill()
        if self.rect.bottom > height:
            self.kill()