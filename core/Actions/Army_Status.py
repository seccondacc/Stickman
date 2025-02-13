from core.Automate.Timestamps import Timestaps
from core.Troops.Troops import Troops
from core.Automate.Decorators.Attack_Enemy import attack_enemy
from core.Automate.Decorators.Check_Enemy import check_enemy
from core.Automate.Decorators.Check_Money import check_money


@check_money
@attack_enemy
@check_enemy
def army_status(timestamps):
    time_in_seconds = Timestaps(timestamps)
    troops_dict = {"giant": 0, "magikill": 0, "spearton": 0, "archidon": 0, "swordwrath": 0, "miner": 0}
    #todo chenge for like ids in trooops_dict
    for i in list(Troops.troops.items()):
        if not i[1].endtime:
            troop = i[1].type
            troops_dict[troop] += 1
    return " ".join(map(str, reversed(list(troops_dict.values()))))