import random
from typing import Any

from app.classes import DataAccessor, ResultData, OneTryData, BaseData
from app.utils import D6, CRO, get_damage


def info():
    pass


class Calculator(DataAccessor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data: BaseData | None = None
        self._try: OneTryData | None = None
        self.result: ResultData = ResultData()



    def calculate(self):
        self.data = self.get_data()
        for _ in range(self.tries):
            self._try = self.data.prepare_try()

            while self._try.targets and self._try.attacks:
                self._try.attacks -= 1
                self.make_hit_roll()

            self.result.success_hits_list.append(self._try.success_hits)
            self.result.success_wounds_list.append(self._try.success_wounds)
            self.result.failed_saves_list.append(self._try.failed_saves)
            self.result.failed_fnp_list.append(self._try.failed_fnp)
            self.result.wounds_lost_list.append(self._try.wounds_lost)
            self.result.targets_killed_list.append(self._try.targets_killed)

    def check_hit_roll(self, hit_roll):
        return hit_roll >= min(self.data.WS - self.data.PTH, self.data.CH)

    def check_wound_roll(self, wound_roll):
        return wound_roll >= min(self.data.wound_on, self.data.CW)

    def check_can_reroll_hit(self, hit_roll):
        return self.data.CRH == CRO.ALL or (self.data.CRH == CRO.ONES_ONLY and hit_roll == 1)

    def check_can_reroll_wound(self, wound_roll):
        return self.data.CRW == CRO.ALL or (self.data.CRW == CRO.ONES_ONLY and wound_roll == 1)

    def make_hit_roll(self):
        hit_roll = random.choice(D6)  # Roll a dice
        Hit = self.check_hit_roll(hit_roll)
        CRR = self.check_can_reroll_hit(hit_roll)  # can_reroll_the_roll
        if not Hit and CRR:
            hit_roll = random.choice(D6)
            Hit = self.check_hit_roll(hit_roll)
        if not Hit:
            return
        self._try.success_hits += 1
        hits_total = 1
        if hit_roll >= self.crit_hit_on:
            if self.data.sustained_hits:
                self._try.success_hits += self.data.sustained_hits_val
                hits_total += self.data.sustained_hits_val
            if self.data.lethal_hits:
                self._try.success_wounds += 1
                hits_total -= 1
                self.make_save_roll()
        for hit in range(hits_total):
            self.make_wound_roll()
        return


    def make_wound_roll(self):
        wound_roll = random.choice(D6)  # Roll a dice
        Wound = self.check_wound_roll(wound_roll)
        CRR = self.check_can_reroll_hit(wound_roll)  # can_reroll_the_roll
        if not Wound and CRR:
            wound_roll = random.choice(D6)
            Wound = self.check_wound_roll(wound_roll)
        if not Wound:
            return
        self._try.success_wounds += 1
        if wound_roll >= self.data.CW and self.data.devastating_wounds:
            if self.data.FNP:
                self.make_fnp_rolls()
            else:
                if not self._try.targets:
                    return
                damage = get_damage(self.data.D)
                damage = damage if damage <= self._try.targets[0] else self._try.targets[0]
                self._try.targets[0] -= damage
                self._try.wounds_lost += damage
                if self._try.targets[0] <= 0:
                    self._try.targets.pop(0)
                    self._try.targets_killed += 1
        else:
            self.make_save_roll()


    def make_save_roll(self):
        use_Sv = self.Sv if self.Sv + self.AP <= self.SvInv else self.SvInv
        Save_roll = random.choice(D6)
        if Save_roll >= use_Sv:
            return
        global failed_saves
        failed_saves += 1
        if self.FNP:
            self.make_fnp_rolls()
        else:
            if not self._try.targets:
                return
            damage = get_damage(self.data.D)
            damage = damage if damage <= self._try.targets[0] else self._try.targets[0]
            self._try.targets[0] -= damage
            self._try.wounds_lost += damage
            if self._try.targets[0] <= 0:
                self._try.targets.pop(0)
                self._try.targets_killed += 1


    def make_fnp_rolls(self):
        if not self._try.targets:
            return
        damage = get_damage(self.data.D)
        damage = damage if damage <= self._try.targets[0] else self._try.targets[0]
        for wound_ in range(damage):
            FNP_roll = random.choice(D6)
            if FNP_roll >= self.FNP:
                continue
            global failed_fnp
            self._try.failed_fnp += 1
            self._try.targets[0] -= 1
            self._try.wounds_lost += 1
            if self._try.targets[0] <= 0:
                self._try.targets.pop(0)
                self._try.targets_killed += 1
                break

