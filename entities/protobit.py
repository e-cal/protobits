from pyglet.shapes import Circle
from random import randrange


class Protobit:
    def __init__(self, x, y, size) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.body = Circle(
            x=self.x,
            y=self.y,
            radius=self.size,
            color=(255, 255, 255),
        )
        self.nourishment = randrange(1, 11)
        self.dead = False

    def update(self):
        self.nourishment -= 1
        if self.nourishment == 0:
            self.dead = True
        else:
            self.draw()

    def draw(self):
        self.body.draw()
