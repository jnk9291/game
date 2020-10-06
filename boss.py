import pygame as pg
from functions import load_image
from random import randint
from variables import *
from danmaku import *

class boss01(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.images = load_image(1,4,"boss")
        self.images_right = load_image(5,8,"boss")
        self.images_left = load_image(9,12,"boss")
        self.image_attack = load_image(0,0,"boss13")
        self.indextimer = 0
        self.index = 0
        self.indextimer2 = 0
        self.index2 = 0
        self.indextimer3 = 0
        self.index3 = 0
        self.speedx = 3
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = 480,100
        self.radius = int(self.rect.width * .40 / 2)
        self.health = 250
        self.bulletdirectiony = 0
        self.bulletdirectiony2 = 0
    def update(self):
        self.bulletdirectiony += 1
        if self.bulletdirectiony > 8:
            self.bulletdirectiony = -7
        if self.bulletdirectiony == 0:
            self.bulletdirectiony = 1
        self.bulletdirectiony2 -= 1
        if self.bulletdirectiony2 < -8:
            self.bulletdirectiony2 = 8
        if self.bulletdirectiony2 == 0:
            self.bulletdirectiony2 = -1
        if self.health <= 250 and self.health >= 200:
            self.nonspell()
        elif self.health < 200 and self.health >= 100:
            self.spell1()
        elif self.health < 100:
            self.last()
        if self.rect.right == height or self.rect.left == 0:
            self.speedx = -1*self.speedx
        self.rect.x += self.speedx
        if self.speedx == 0:
            if self.indextimer % 100 == 0:
                self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
        if self.speedx > 0:
            if self.index2 == len(self.images_left) - 1:
                self.index2 = 3
            else:
                if self.indextimer2 % 100 == 0:
                    self.index2 += 1
            self.image = self.images_right[self.index2]
        if self.speedx < 0:
            if self.index3 == len(self.images_left) - 1:
                self.index3 = 3
            else:
                if self.indextimer3 % 100 == 0:
                    self.index3 += 1
            self.image = self.images_left[self.index3]
        # Remove the bullet when it leaves the screen.
        self.rect.clamp_ip(screen_rect)
    def nonspell(self):
        b1 = star(self.rect.center,self.rect.center,randint(-2,2),self.bulletdirectiony)
        b2 = star(self.rect.center,self.rect.center,randint(-2,2),self.bulletdirectiony)
        all_sprites.add(b1)
        all_sprites.add(b2)
    def spell1(self):
        target = Vector2((player.rect.center,player.rect.center))
        b3 = arrowhead((self.rect.center,self.rect.center),target,screen_rect)
        all_sprites.add(b3)
