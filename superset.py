from sets import Set

class Superset:
    def __init__(self, set1: Set, set2: Set):
        self.sets = [set1, set2]

    def __repr__(self):
        return f"Superset({self.sets[0].exercise.name}, {self.sets[1].exercise.name})"

    def get_sets(self):
        return self.sets

    def __iter__(self):
        return iter(self.sets)
