class Brain:
    def __init__(self):
        pass

    def act(self):
        raise NotImplementedError


class Random(Brain):
    def __init__(self):
        super().__init__()

    def act(self):
        pass
