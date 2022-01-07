from pyglet.shapes import Circle


class Food:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.body = Circle(
            x=self.x,
            y=self.y,
            radius=5,
            color=(0, 255, 0),
        )
        self.lifetime = 100
        self.dead = False

    def update(self):
        self.lifetime -= 1
        if self.lifetime == 0:
            self.dead = True
        else:
            self.draw()

    def draw(self):
        self.body.draw()


class Plant(Food):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
