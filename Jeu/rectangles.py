import pygame as py


class Green_Rectangle(py.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.color = (54, 238, 54)
        self.length = 70 #length of player
        self.height = 17 #height of player


class White_Rectangle(py.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.color = (255, 255, 255)
        self.length = 76 #length green rectangle + 6
        self.height = 23 #height green rectangle + 6