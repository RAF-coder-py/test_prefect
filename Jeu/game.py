import pygame as py
from player import Player
from rectangles import White_Rectangle, Green_Rectangle

image = py.image.load('Jeu/pictures/zombie.png')
image = py.transform.scale(image, (100, 100))

class Game:


    def __init__(self, width:int = 1080, height:int = 720):
        self.player_2 = Player()
        self.player_1 = Player(position_x=800, image=py.transform.flip(image, True, False), sol=535)
        self.screen = py.display.set_mode((width, height))
        self.screen_rect = self.screen.get_rect()
        self.w_rectangle = White_Rectangle()
        self.g_rectangle = Green_Rectangle()
        self.all_player_1 = py.sprite.Group()
        self.all_player_1.add(self.player_1)
        self.all_player_2 = py.sprite.Group()
        self.all_player_2.add(self.player_2)

    def draw_player(self, player):
        self.screen.blit(player.image, (player.rect.x, player.rect.y))

    def player_move_right(self, player):
        if player.rect.x <= 1030:
            player.rect.x += player.velocity_x

    def player_move_left(self, player):
        if player.rect.x >= -10:
            player.rect.x -= player.velocity_x

    def draw_rectangle(self, player):
        py.draw.rect(self.screen, self.w_rectangle.color, (player.rect.x-3, player.rect.y - 33, self.w_rectangle.length, self.w_rectangle.height))
        py.draw.rect(self.screen, self.g_rectangle.color, (player.rect.x, player.rect.y - 30, int((player.health/player.original_health)*self.g_rectangle.length), self.g_rectangle.height))

    def check_collision(self, sprite, group):
        return bool(py.sprite.spritecollide(sprite, group, False, py.sprite.collide_mask))