from enum import Enum
from exercise import Exercise

class SetType(Enum):
    NORMAL = "normal"
    DROP = "drop"
    REST_PAUSE = "rest-pause"
    PARTIAL = "partial"
    AMRAP = "AMRAP"

set_types = [SetType.NORMAL, SetType.DROP, SetType.REST_PAUSE, SetType.PARTIAL, SetType.AMRAP]

class Set:
    def __init__(self, weight: float, reps: int, set_type: SetType , exercise: Exercise):
        self.weight = weight
        self.reps = reps
        self.set_type = set_type
        self.exercise = exercise

    def __repr__(self):
        return f"Set(weight={self.weight}, reps={self.reps}, set_type={self.set_type.name}, exercise={self.exercise.name}:{self.exercise.set_no}x{self.exercise.rep_range[0]}-{self.exercise.rep_range[1]})"
   
    def Get_Upper(self) -> int:
       return self.exercise.rep_range[1]
    def Get_Lower(self) -> int:
        return self.exercise.rep_range[0]

def compute_score(set1 : Set) -> float:
    Excess = 0
    d = 0.55
    discount = 0

    if(set1.reps > set1.Get_Upper()):
        Excess = set1.reps - set1.Get_Upper()
        s = Set(set1.weight, set1.Get_Upper(), set1.set_type, set1.exercise)
    else:
        s = Set(set1.weight, set1.reps, set1.set_type, set1.exercise)

    if s.weight >= 2.5:
        ep = Set(s.weight - 2.5,s.Get_Upper(), s.set_type,s.exercise)
        score = compute_score(ep) + ((s.reps-s.Get_Lower())/(s.Get_Upper()-s.Get_Lower()))
    elif s.weight == 0:
        return 0
    else:
        score = (s.weight*s.reps)/(2.5*s.Get_Upper())
        
    for _ in range(Excess):
        discount += score/s.reps*d
        d=d*0.85

    return score + discount

