import random
from dataclasses import dataclass
from warnings import warn

import pyglet

from ..brain import Brain, Genome
from ..entities import Protobit, Food


@dataclass
class Entities:
    protobits: list[Protobit]
    food: list[Food]


class World:
    """The world in which Protobits exist and act.

    Attributes:
        width (int):
            The width of the world (window).

        height (int):
            The height of the world (window).

        init_pop (int):
            The number of protobits to initially spawn.

        init_species (int):
            The number of different species (genomes) to spawn protobits into.

        brains (Set[Brain]):
            The set of brains to select from when spawning protobits.

        brain_weights (List[float] | None):
            Optional; Probability of each corresponding brain algorithm being
            selected. Must add up to 100 and be the same length as the brains
            list. Brains are selected with equal probabaility if not provided.

        genomes (Set[Genome]):
            Optional; The set of initial genomes to select from when spawning protobits.
            If empty or less than init_species, the remaining genomes will be
            randomly generated.

        genome_weights (List[float] | None):
            Optional; Probability of each corresponding genome being
            selected. Must add up to 100 and be the same length as the brains
            list. Brains are selected with equal probabaility if not provided.
    """

    def __init__(
        self,
        width: int,
        height: int,
        init_pop: int,
        init_species: int,
        brains: set[Brain],
        brain_weights: list[float] | None = None,
        genomes: set[Genome] | None = None,
        genome_weights: list[float] | None = None,
    ) -> None:
        # Window
        self.width = width
        self.height = height
        self.window = pyglet.window.Window(width=self.width, height=self.height)

        # Metadata
        self.pop = init_pop
        self.species = init_species

        # Entities

        # Handle missing genomes
        if genomes is None:
            missing = init_species
            genomes = set()
        else:
            missing = init_species - len(genomes)
            if missing < 0:
                warn(
                    f"More genomes specefied than species. Using the first {init_species} genomes (after set to list conversion, order may not be preserved)."
                )
                missing = 0
                genomes = set(list(genomes)[:init_species])

        for _ in range(missing):
            genomes.add(Genome.random())

        # Generate initial protobits
        protobits = self.gen_protobits(
            init_pop, brains, brain_weights, genomes, genome_weights
        )

        food = self._gen_food()

        self.entities = Entities(
            protobits=protobits,
            food=food,
        )

        # pyglet.clock.schedule_interval(update, 1)
        # pyglet.app.run()
        # for protobit in protobits:
        #     protobit.draw()

    def gen_protobits(
        self,
        num: int,
        brains: set[Brain],
        brain_weights: list[float] | None,
        genomes: set[Genome],
        genome_weights: list[float] | None,
    ) -> list[Protobit]:
        """Generates a list of protobits."""

        if brain_weights is None:
            brain_weights = [100 / len(brains)] * len(brains)
        if genome_weights is None:
            genome_weights = [100 / len(genomes)] * len(brains)

        # pre-calculate and use cumulative weights to avoid implicit
        # in the following loop
        cum_weights = [sum(brain_weights[:i]) for i in range(1, len(brain_weights) + 1)]

        protobits = []
        for _ in range(num):
            random.choices(list(brains), cum_weights=cum_weights)

        return protobits

    def _gen_food(self) -> list[Food]:
        return []

    def spawn(self):
        """Directly spawn entities into the world."""
        pass

    def update(self, dt):
        """
        Update the state of the world.

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
