import random
import pygame as pg
from bullets import *
from variables import *
from background import *
from boss import boss01


pg.init()
background0 = Background("bg0")
pg.mixer.init()
clock = pg.time.Clock()
b = boss01()


all_sprites.add(player)

all_sprites.add(b)
players.add(player)
done = False
while not done:
    for event in pg.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5  
        if event.type == pg.QUIT:
            done = True
    if spell:
        background0.movingUpSpeed = 0
    if nonspell:
        background0.movingUpSpeed = -7
    background0.update()
    background0.render()
    all_sprites.update()
    if b.health < 0:
        done = True
    collision1 = pg.sprite.spritecollide(b,bullets,True, pg.sprite.collide_circle)
    for col in collision1:
        b.health -= 1
    collision2 = pg.sprite.spritecollide(player,danmakuBullets,True,pg.sprite.collide_circle)
    for col1 in collision2:
        player.health = -1
    all_sprites.draw(screen)
    pg.display.update()
    pg.display.flip()
    clock.tick(60)
pg.quit()