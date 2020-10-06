import pygame as pg
from variables import *
from functions import *
from bullets import *

class DanmakuOrb0(pg.sprite.Sprite):
    def __init__(self,x ,y):
        pg.sprite.Sprite.__init__(self)
        self.original_image = pg.image.load(path.join(imgfolder, "orb0.png")).convert_alpha()
        self.image = self.original_image.copy()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.radius = int(self.rect.width * .40 / 2)
        self.shoottime = 150
        self.last = pg.time.get_ticks()
        self.angle = 0
    def update(self):
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.angle += 5 % 360
        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (x, y)  # Put the new rect's center at old center.
    def shoot1(self):
        target = Vector2(b.rect.x,b.rect.y)
        time = pg.time.get_ticks()
        if time - self.last > self.shoottime:
            self.last = time
            b1 = Bullet2((self.rect.centerx,self.rect.centery),target,screen.get_rect())
            all_sprites.add(b1)
            bullets.add(b1)

    def shoot2(self):
        time = pg.time.get_ticks()
        if time - self.last > 100:
            self.last = time
            b1 = Bullet4(self.rect.centerx,self.rect.centery,0,-20)
            all_sprites.add(b1)
            bullets.add(b1)
class DanmakuOrb3(pg.sprite.Sprite):
    def __init__(self,x ,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(path.join(imgfolder, "orb3.png")).convert_alpha()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.radius = int(self.rect.width * .40 / 2)
        self.shoottime = 150
        self.last = pg.time.get_ticks()
    def update(self):
        pass
    def shoot1(self):
        time = pg.time.get_ticks()
        if time - self.last > self.shoottime:
            self.last = time
            b1 = Bullet0(self.rect.centerx,self.rect.centery,0,-10)
            all_sprites.add(b1)
            bullets.add(b1)
    def shoot2(self):
        time = pg.time.get_ticks()
        if time - self.last > 100:
            self.last = time
            b1 = Bullet0(self.rect.centerx,self.rect.centery,0,-20)
            all_sprites.add(b1)
            bullets.add(b1)


class Player0(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.images = load_image(24,31,"pl")
        self.images_left = load_image(32,38,"pl")      
        self.images_right = load_image(39,47,"pl")
        self.index = 0
        self.index2 = 0
        self.index3 = 0
        self.indextimer = 0
        self.indextimer2 = 0
        self.indextimer3 = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (512,384)
        self.radius = int(self.rect.width * .40 / 2)
        self.power = 1
        self.temp = True
        self.temp2 = True
        self.shoottime = 50
        self.last = pg.time.get_ticks()
        self.health = 3
    def shoot(self):
        time = pg.time.get_ticks()
        if time - self.last > self.shoottime:
            self.last = time
            b1 = Bullet3(self.rect.centerx - 10,self.rect.top,0,-10)
            b2 = Bullet3(self.rect.centerx + 10,self.rect.top,0,-10)
            bullets.add(b1)
            bullets.add(b2)
            all_sprites.add(b1)
            all_sprites.add(b2)
    def update(self):
        self.indextimer += 1
        self.indextimer2 += 1
        self.indextimer3 += 1
        self.speedx = 0
        self.speedy = 0
        if self.temp:
            global orb1
            global orb2
            global orb3
            global orb4
            orb1 = DanmakuOrb0(self.rect.left - 30 ,self.rect.top + 30)
            orb2 = DanmakuOrb0(self.rect.right + 30,self.rect.top + 30)
            orb3 = DanmakuOrb0(self.rect.left - 10,self.rect.bottom - 20)
            orb4 = DanmakuOrb0(self.rect.right + 10,self.rect.bottom - 20)
            all_sprites.add(orb1)
            all_sprites.add(orb2)
            all_sprites.add(orb3)
            all_sprites.add(orb4)
            self.temp = False
        orb1.rect.centerx = self.rect.left - 30
        orb1.rect.centery = self.rect.top + 30
        orb2.rect.centerx = self.rect.right + 30
        orb2.rect.centery = self.rect.top + 30
        orb3.rect.centerx = self.rect.left - 10
        orb3.rect.centery = self.rect.bottom + 10
        orb4.rect.centerx = self.rect.right + 10
        orb4.rect.centery = self.rect.bottom + 10
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.speedx = -5
        if keystate[pg.K_RIGHT]:
            self.speedx = 5
        if keystate[pg.K_UP]:
            self.speedy = -5
        if keystate[pg.K_DOWN]:            
            self.speedy = 5
        if keystate[pg.K_LEFT] and keystate[pg.K_LSHIFT]:
            self.speedx = -2.5
        if keystate[pg.K_RIGHT] and keystate[pg.K_LSHIFT]:
            self.speedx = 2.5
        if keystate[pg.K_UP] and keystate[pg.K_LSHIFT]:
            self.speedy = -2.5
        if keystate[pg.K_DOWN] and keystate[pg.K_LSHIFT]:            
            self.speedy = 2.5
        if keystate[pg.K_z]:
            self.shoot()
            orb1.shoot1()
            orb2.shoot1()
            orb3.shoot1()
            orb4.shoot1()
        if keystate[pg.K_LSHIFT]:
            orb1.rect.centerx = self.rect.left - 10
            orb1.rect.centery = self.rect.top + 10
            orb2.rect.centerx = self.rect.right + 10
            orb2.rect.centery = self.rect.top + 10
            orb3.rect.centerx = self.rect.left + 10
            orb3.rect.centery = self.rect.top - 10
            orb4.rect.centerx = self.rect.right - 10
            orb4.rect.centery = self.rect.top - 10
        if keystate[pg.K_z] and keystate[pg.K_LSHIFT]:
            self.shoot()
            orb1.shoot2()
            orb2.shoot2()
            orb3.shoot2()
            orb4.shoot2()
 
        if self.speedx == 0:
            if self.indextimer % 5 == 0:
                self.index += 1
            if self.index == len(self.images):
                self.index = 0
            self.image = self.images[self.index]
        if self.speedx > 0:
            self.image = self.images_right[6]
        if self.speedx < 0:
            self.image = self.images_left[6]
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.rect.clamp_ip(screen.get_rect())


class Player3(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.images = load_image(0,7,"pl")
        self.images_left = load_image(8,15,"pl")      
        self.images_right = load_image(15,23,"pl")
        self.index = 0
        self.index2 = 0
        self.index3 = 0
        self.indextimer = 0
        self.indextimer2 = 0
        self.indextimer3 = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (512,384)
        self.radius = int(self.rect.width * .40 / 2)
        self.power = 1
        self.temp = True
        self.temp2 = True
        self.shoottime = 50
        self.last = pg.time.get_ticks()
        self.health = 3
    def shoot(self):
        time = pg.time.get_ticks()
        if time - self.last > self.shoottime:
            self.last = time
            b1 = Bullet1(self.rect.centerx - 10,self.rect.top,0,-10)
            b2 = Bullet1(self.rect.centerx + 10,self.rect.top,0,-10)
            all_sprites.add(b1)
            all_sprites.add(b2)
            bullets.add(b1)
            bullets.add(b1)
    def update(self):
        self.indextimer += 1
        self.indextimer2 += 1
        self.indextimer3 += 1
        self.speedx = 0
        self.speedy = 0
        if self.temp:
            global orb1
            global orb2
            global orb3
            global orb4
            orb1 = DanmakuOrb3(self.rect.left - 30 ,self.rect.top + 30)
            orb2 = DanmakuOrb3(self.rect.right + 30,self.rect.top + 30)
            orb3 = DanmakuOrb3(self.rect.left - 5,self.rect.top - 20)
            orb4 = DanmakuOrb3(self.rect.right + 5,self.rect.top - 20)
            all_sprites.add(orb1)
            all_sprites.add(orb2)
            all_sprites.add(orb3)
            all_sprites.add(orb4)
            self.temp = False
        orb1.rect.centerx = self.rect.left - 30
        orb1.rect.centery = self.rect.top + 30
        orb2.rect.centerx = self.rect.right + 30
        orb2.rect.centery = self.rect.top + 30
        orb3.rect.centerx = self.rect.left - 5
        orb3.rect.centery = self.rect.top - 10
        orb4.rect.centerx = self.rect.right + 5
        orb4.rect.centery = self.rect.top - 10
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.speedx = -5
        if keystate[pg.K_RIGHT]:
            self.speedx = 5
        if keystate[pg.K_UP]:
            self.speedy = -5
        if keystate[pg.K_DOWN]:            
            self.speedy = 5
        if keystate[pg.K_LEFT] and keystate[pg.K_LSHIFT]:
            self.speedx = -2.5
        if keystate[pg.K_RIGHT] and keystate[pg.K_LSHIFT]:
            self.speedx = 2.5
        if keystate[pg.K_UP] and keystate[pg.K_LSHIFT]:
            self.speedy = -2.5
        if keystate[pg.K_DOWN] and keystate[pg.K_LSHIFT]:            
            self.speedy = 2.5
        if keystate[pg.K_z]:
            self.shoot()
            orb1.shoot1()
            orb2.shoot1()
            orb3.shoot1()
            orb4.shoot1()
        if keystate[pg.K_LSHIFT]:
            orb1.rect.centerx = self.rect.left - 10
            orb1.rect.centery = self.rect.top + 10
            orb2.rect.centerx = self.rect.right + 10
            orb2.rect.centery = self.rect.top + 10
            orb3.rect.centerx = self.rect.left + 10
            orb3.rect.centery = self.rect.top - 10
            orb4.rect.centerx = self.rect.right - 10
            orb4.rect.centery = self.rect.top - 10

        if keystate[pg.K_z] and keystate[pg.K_LSHIFT]:
            self.shoot()
            orb1.shoot2()
            orb2.shoot2()
            orb3.shoot2()
            orb4.shoot2()
 
        if self.speedx == 0:
            if self.indextimer % 10 == 0:
                self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
        if self.speedx > 0:
            self.image = self.images_right[7]
        if self.speedx < 0:
            self.image = self.images_left[7]
        self.rect.x += self.speedx
        self.rect.y += self.speedy
