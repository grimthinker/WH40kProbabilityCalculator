import random
from typing import Any

from app.classes import Data, ResultData

DICE = [1, 2, 3, 4, 5, 6]


def info():
    pass


class Calculator(Data, ResultData):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._targets: list[int] = [1]
        self._wounds_on: int = 6
        self._attacks: int = 1
        self.failed_fnp: int = 0
        self.targets_killed: int = 0
        self.wounds_lost: int = 0
        self.targets_killed: int = 0

    @property
    def attacks(self):
        return self._attacks

    @attacks.setter
    def attacks(self, val):
        self._attacks = val

    def calculate(self):
        self.wound_on = def_wound_on(self.S, self.T, plus_to_wound=self.PTW)
        for _ in range(self.tries):
            self.targets = [self.W for x in range(self.targets_amount)]
            self.attacks = self.attacks_amount
            success_hits = 0
            success_wounds = 0
            failed_saves = 0
            failed_fnp = 0
            wounds_lost = 0
            targets_killed = 0

            self.success_wounds_on_list.append(self.wound_on)
            while self.targets and self.attacks:
                self.attacks -= 1

                self.make_hit_roll()

            self.success_hits_list.append(success_hits)
            self.success_wounds_list.append(success_wounds)
            self.failed_saves_list.append(failed_saves)
            self.failed_fnp_list.append(failed_fnp)
            self.wounds_lost_list.append(wounds_lost)
            self.targets_killed_list.append(targets_killed)


    def make_hit_roll(self):
        Hit_roll = random.choice(DICE)  # Roll a dice
        if Hit_roll >= min(self.WS - self.PTH, self.Crit_hit) or (
                Hit_reroll == '1' or (Hit_reroll == '2' and Hit_roll == 1) and random.choice(DICE) >= WS):
            Hit = True
        else:
            Hit = False
        if not Hit:
            return
        global success_hits
        global success_wounds
        success_hits += 1
        hits_total = 1
        if Hit_roll >= Crit_hit:
            if Sust_hits:
                success_hits += Sust_hits
                hits_total += Sust_hits
            if Leth_hits:
                success_wounds += 1
                hits_total -= 1
                make_save_roll()
        for hit in range(hits_total):
            self.make_wound_roll()


    def make_wound_roll(self):
        Wound_roll = random.choice(DICE)
        if Wound_roll >= min(Wound_on, Crit_wound) or (
                Wound_reroll == '1' or (Wound_reroll == '2' and Wound_roll == 1) and random.choice(DICE) >= Wound_on):
            Wound = True
        else:
            Wound = False
        if not Wound:
            return
        global success_wounds
        success_wounds += 1
        if Wound_roll >= Crit_wound and Dev_wounds:
            if self.FNP:
                self.make_fnp_rolls()
            else:
                if not self.targets:
                    return
                damage = self.D if self.D <= self.targets[0] else self.targets[0]
                self.targets[0] -= damage
                self.wounds_lost += damage
                if self.targets[0] <= 0:
                    self.targets.pop(0)
                    self.targets_killed += 1
        else:
            self.make_save_roll()


    def make_save_roll(self):
        use_Sv = self.Sv if self.Sv + self.AP <= self.SvInv else self.SvInv
        Save_roll = random.choice(DICE)
        if Save_roll >= use_Sv:
            return
        global failed_saves
        failed_saves += 1
        if self.FNP:
            self.make_fnp_rolls()
        else:
            if not self.targets:
                return
            damage = self.D if self.D <= self.targets[0] else self.targets[0]
            self.targets[0] -= damage
            self.wounds_lost += damage
            if self.targets[0] <= 0:
                self.targets.pop(0)
                self.targets_killed += 1


    def make_fnp_rolls(self):
        if not self.targets:
            return
        for wound_ in range(self.D):
            FNP_roll = random.choice(DICE)
            if FNP_roll >= self.FNP:
                continue
            global failed_fnp
            self.failed_fnp += 1
            self.targets[0] -= 1
            self.wounds_lost += 1
            if self.targets[0] <= 0:
                self.targets.pop(0)
                self.targets_killed += 1
                break


def def_wound_on(S, T, plus_to_wound=None):
    if 2 * S <= T:
        wound_on = 6
    elif S < T:
        wound_on = 5
    elif S == T:
        wound_on = 4
    elif S > T:
        wound_on = 3
    else:
        wound_on = 2
    if plus_to_wound:
        wound_on -= plus_to_wound
    return wound_on


def is_int(val: Any) -> bool:
    try:
        int(val)
        return True
    except:
        return False

