from sets import Set
from typing import List

class GiantSet:
    def __init__(self, sets: List[Set]):
        if len(sets) < 3:
            raise ValueError("A giant set must contain at least 3 sets.")
        self.sets = sets

    def __repr__(self):
        return f"GiantSet({', '.join([set_obj.exercise.name for set_obj in self.sets])})"

    def get_sets(self):
        return self.sets

    def __iter__(self):
        return iter(self.sets)
