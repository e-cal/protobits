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

    def draw(self):
        self.body.draw()
