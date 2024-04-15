import random
from dataclasses import dataclass, asdict
from enum import Enum, StrEnum
from tkinter import *
import statistics
from collections import Counter
from tkinter import ttk

from app.setup import setup_app

dice = [1, 2, 3, 4, 5, 6]

amount_targets = 9
amount_attacks = 20
Hit_reroll = '1'  # 1 - reroll all, 2 - reroll ones only
Wound_reroll = '1'  # 1 - reroll all, 2 - reroll ones only
WS = 3
D = 1
S = 5
AP = -0
Crit_hit = 5
Crit_wound = 6
Sust_hits = 2
Leth_hits = False
Dev_wounds = False
plus_to_hit = 0
plus_to_wound = 1
W = 2
T = 4
Sv = 3
SvInv = 7
FNP = 0

tries = 10000

success_hits_list = []
success_wounds_on_list = []
success_wounds_list = []
failed_saves_list = []
failed_fnp_list = []
wounds_lost_list = []
targets_killed_list = []


def print_info():
    print('Wounds on: ', Wound_on)
    print('Successfull hits', sum(success_hits_list) / len(success_hits_list), )
    print('Successfull wounds', sum(success_wounds_list) / len(success_wounds_list), )
    print('Failed saves', sum(failed_saves_list) / len(failed_saves_list), )
    print('Failed FNP', sum(failed_fnp_list) / len(failed_fnp_list), )
    print('Wounds lost', sum(wounds_lost_list) / len(wounds_lost_list), )
    print('Targets killed', sum(targets_killed_list) / len(targets_killed_list),)

    print()
    print('Max Successfull hits', max(success_hits_list))
    print('Max successfull wounds', max(success_wounds_list))
    print('Max failed saves', max(failed_saves_list))
    print('Max failed FNP', max(failed_fnp_list))
    print('Max wounds lost', max(wounds_lost_list))
    print('Max targets killed', max(targets_killed_list))
    print()

    frequencies = {k: v/tries*100 for k, v in dict(Counter(wounds_lost_list)).items()}
    for k in sorted(list(frequencies.keys())):
        print(f'Chance to inflict {k} wounds: {frequencies[k]}%')
    print()

    frequencies = {k: v/tries*100 for k, v in dict(Counter(targets_killed_list)).items()}
    for k in sorted(list(frequencies.keys())):
        print(f'Chance to kill only {k} models: {frequencies[k]}%')
    targets_killed_quantiles = statistics.quantiles(targets_killed_list, n=500,)
    print()
    print(statistics.quantiles(targets_killed_list, n=5,))
    print()
    for k in range(len(targets_killed_quantiles)):
        next = targets_killed_quantiles[k]
        if k + 1 >= len(targets_killed_quantiles) or next != targets_killed_quantiles[k + 1]:
            print(f'{100-k/len(targets_killed_quantiles)*100}% of all times more than {targets_killed_quantiles[k]} models survived')


if __name__ == '__main__':
    root = setup_app()
    root.mainloop()





