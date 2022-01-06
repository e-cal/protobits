import pyglet
from pyglet.shapes import Circle
from random import randrange
from protobit import Protobit  # type: ignore
from food import Food  # type: ignore


class World:
    """The world"""

    def update(dt):
        """
        Main update loop function.

        Args:
            dt: Delta time (since last update).
                Should be approx what is passed to `schedule_interval()` below.
        """

        window.clear()

        dead = []
        for protobit in protobits:
            protobit.update()
            if protobit.dead:
                dead.append(protobit)
        for pellet in food:
            pellet.draw()
        for d in dead:
            protobits.remove(d)

    if __name__ == "__main__":
        window = pyglet.window.Window(width=1300, height=900)

        protobits = [
            Protobit(randrange(0, window.width), randrange(0, window.height), 25)
            for _ in range(100)
        ]

        food = [
            Food(randrange(0, window.width), randrange(0, window.height))
            for _ in range(20)
        ]
        pyglet.clock.schedule_interval(update, 1)
        pyglet.app.run()
        for protobit in protobits:
            protobit.draw()
