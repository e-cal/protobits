import random
from dataclasses import dataclass
from warnings import warn

import pyglet

from ..brain import Brain, Genome
from ..entities import Protobit, Food, Plant


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
        brains: list[Brain],
        brain_weights: list[float] | None = None,
        genomes: list[Genome] | None = None,
        genome_weights: list[float] | None = None,
    ) -> None:
        # Window
        self.width = width
        self.height = height
        self.window = pyglet.window.Window(width=self.width, height=self.height)

        self.app = pyglet.app
        self.clock = pyglet.clock

        # Metadata
        self.pop = init_pop
        self.species = init_species

        # Entities

        # Handle missing genomes
        if genomes is None:
            missing = init_species
            genomes = []
        else:
            missing = init_species - len(genomes)
            if missing < 0:
                warn(
                    f"More genomes specefied than species. Using the first {init_species} genomes."
                )
                missing = 0
                genomes = genomes[:init_species]

        for _ in range(missing):
            genomes.append(Genome.random())

        # Generate initial protobits
        protobits = self.gen_protobits(
            init_pop, brains, brain_weights, genomes, genome_weights
        )

        food = self._gen_plants()

        self.entities = Entities(
            protobits=protobits,
            food=food,
        )

    def gen_protobits(
        self,
        num: int,
        brains: list[Brain],
        brain_weights: list[float] | None,
        genomes: list[Genome],
        genome_weights: list[float] | None,
    ) -> list[Protobit]:
        """Generates a list of protobits."""
        locs = [
            (random.randrange(1, self.width), random.randrange(1, self.height))
            for _ in range(num)
        ]

        if brain_weights is None:
            brain_weights = [100 / len(brains)] * len(brains)
        if genome_weights is None:
            genome_weights = [100 / len(genomes)] * len(genomes)
        brain = random.choices(brains, brain_weights, k=num)
        genome = random.choices(genomes, weights=genome_weights, k=num)

        return [
            Protobit(x, y, brain, genome)
            for (x, y), brain, genome in zip(locs, brain, genome)
        ]

    def _gen_plants(self) -> list[Food]:
        """Internal function to generate food during world initialization.

        On-demand food spawning should be done with `spawn`.
        """

        locs = [
            (random.randrange(1, self.width), random.randrange(1, self.height))
            for _ in range(random.randrange(self.pop // 2, int(self.pop * 1.5)))
        ]
        return [Plant(x, y) for x, y in locs]

    def spawn(self):
        """Directly spawn entities into the world."""
        pass

    def update(self, _=None):
        """Update the state of the world."""
        self.window.clear()

        for food in self.entities.food:
            food.update()

        dead = []
        for protobit in self.entities.protobits:
            protobit.update()
            if protobit.dead:
                dead.append(protobit)
        for d in dead:
            self.entities.protobits.remove(d)

    def run(self, framerate: float = 1 / 60):
        """Run the world simulation at the set framerate.

        Args:
            framerate (float): Minimum update time interval.
        """
        self.update()
        self.clock.schedule_interval(self.update, framerate)
        self.app.run()
