from typing import List, Union
from sets import Set
from superset import Superset
from giantset import GiantSet
from datetime import date
from input import *
#from exercise import Exercise

class Session:
    def __init__(self, sets: List[Union[Set, Superset, GiantSet]], date: date):
        self.sets = sets 
        self.date = date

    def get_workout_summary(self):
        for workout in self.sets:
            if isinstance(workout, Set):
                print(f"Set: {workout.exercise.name}, Weight: {workout.weight}, Reps: {workout.reps}")
            elif isinstance(workout, Superset):
                print(f"Superset: {', '.join([s.exercise.name for s in workout.get_sets()])}")
            elif isinstance(workout, GiantSet):
                print(f"Giant Set: {', '.join([s.exercise.name for s in workout.get_sets()])}")

    def get_all_sets(self) -> list:
        l = [item for item in self.sets if isinstance(item, Set)]
        ls = [item for item in self.sets if isinstance(item, Superset)] 
        lg = [item for item in self.sets if isinstance(item, GiantSet)]
        for ss in ls:
            l.append(ss.sets[0])
            l.append(ss.sets[1])
        for gs in lg:
            for s in gs:
                l.append(s)

        return l

    def total_set_score_by_name(self):
        li = self.get_all_sets()
        for s in li:
            print(s.exercise.name," , ",s.reps)


se = Session(l,date.today())
#li = se.get_all_sets()

#for s in li:
#    print(s)

se.total_set_score_by_name()

