import pygame as pg
from variables import *
from functions import load_image

class Background():
      def __init__(self,image):
            self.bgimage = load_image(0,0,image)

            self.rectBGimg = self.bgimage.get_rect()
            self.bgY1 = 0
            self.bgX1 = 0
 
            self.bgY2 = self.rectBGimg.height
            self.bgX2 = 0
 
            self.movingUpSpeed = -7
         
      def update(self):
        self.bgY1 += self.movingUpSpeed
        self.bgY2 += self.movingUpSpeed
        if self.bgY1 <= -self.rectBGimg.height:
            self.bgY1 = self.rectBGimg.height
        if self.bgY2 <= -self.rectBGimg.height:
            self.bgY2 = self.rectBGimg.height
             
      def render(self):
         screen.blit(self.bgimage, (self.bgX1, -self.bgY1))
         screen.blit(self.bgimage, (self.bgX2, -self.bgY2))
