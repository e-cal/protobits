from .environment.world import World

if __name__ == "__main__":

    # set of brain algorithms (classes)
    brains = [
        # Algo1
        # Algo2
        # ...
    ]

    # probabilities of brain algorithms being selected
    # must add up to 100 and be same len as brains
    # equal prob if not provided
    brain_weights = [
        10,
        40,
        # ...,
    ]

    # set of default genomes (initialized classes)
    genomes = [
        # Genome(a=True, b=False, ...)
        # ...
    ]

    # probabilities of default genomes being selected
    # must add up to 100 and be same len as genomes
    # equal prob if not provided
    genome_weights = [
        30,
        10,
        # ...,
    ]

    # generate protobits by sampling from brains and genomes
    # brains / genomes will be sampled from default sets

    # initialize world
    world = World(
        width=100,
        height=100,
        init_pop=10,
        init_species=3,
        brains=brains,
        brain_weights=brain_weights,
        genomes=genomes,
        genome_weights=genome_weights,
    )
