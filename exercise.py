from typing import Tuple

class Exercise:
    def __init__(self, name: str, set_no: int, rep_range : Tuple[int,int] ):
        self.name = name
        self.set_no = set_no
        self.rep_range = rep_range
