import pygame as py
from fire import Fire

image = py.image.load('Jeu/pictures/enfant.png')

class Player(py.sprite.Sprite):

    

    def __init__(self, velocity:int = 7, position_x:float = 200, image = py.transform.scale(image, (65, 75)), sol = 550):
        super().__init__()
        self.image_right = image
        self.image_left = py.transform.flip(self.image_right, True, False)
        self.image = self.image_right
        self.sol = sol
        self.rect = self.image.get_rect()
        self.rect.y = self.sol
        self.rect.x = position_x
        self.jump_height = 15
        self.velocity_x = velocity
        self.velocity_y = self.jump_height
        self.gravity = 1
        self.jumping = False
        self.fire = Fire(self)
        self.all_fire = py.sprite.Group()
        self.original_health = 100
        self.health = 100


    def dont_move(self):
        self.rect.x = self.rect.x

    def jump(self):
        self.rect.y -= self.velocity_y
        self.velocity_y -= self.gravity

        if self.rect.y >= self.sol:
            self.jumping = False
            self.velocity_y = self.jump_height
            self.rect.y = self.sol

    def attack(self):
        self.all_fire.add(Fire(self))
