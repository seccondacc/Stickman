from core.Troops.Troops import Troops


class Swordwrath(Troops):
    health = 120
    cost = 125
    power = 20
    speed = 1
    unit = 1
    def __init__(self,starttime):
        super().__init__(Swordwrath.health, "swordwrath",starttime)