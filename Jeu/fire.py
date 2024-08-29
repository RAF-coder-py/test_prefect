import pygame as py



class Fire(py.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.image= py.image.load('Jeu/pictures/fire.png')
        self.image = py.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 35
        self.rect.y = player.rect.y + 20
        self.velocity = 11
        self.side = ''
        self.player = player
        self.original_image = self.image
        self.angle = 0
        self.rotatet_speed = 15
        self.given_side = False
        self.confirmed = False
        self.damage = 8

    def remove(self):
        self.player.all_fire.remove(self)

    def rotate_right(self):
        self.angle -= self.rotatet_speed
        self.image = py.transform.rotozoom(self.original_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)

    def rotate_left(self):
        self.angle += self.rotatet_speed
        self.image = py.transform.rotozoom(self.original_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)

         

    def move_right(self):
        self.rect.x += self.velocity
        self.rotate_right()
        if self.rect.x > 1080:
            self.remove()
            

    def move_left(self):
        self.rect.x -= self.velocity
        self.rotate_left()
        if self.rect.x < -50:
            self.remove()

    def fire_collision(self, group):
        return bool(py.sprite.spritecollide(self, group, False, py.sprite.collide_mask))