from random import randrange
from pyglet.shapes import Circle

from ..brain import Brain, Genome


class Protobit:
    def __init__(
        self,
        x: int,
        y: int,
        brain: Brain,
        genome: Genome,
    ) -> None:
        self.x = x
        self.y = y
        self.body = Circle(
            x=self.x,
            y=self.y,
            radius=10,
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
