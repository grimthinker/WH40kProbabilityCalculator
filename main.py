import random
from tkinter import *
import statistics
from collections import Counter
from tkinter import ttk

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

Wound_on = def_wound_on(S, T, plus_to_wound=plus_to_wound)

def make_hit_roll():
    Hit_roll = random.choice(dice)  # Roll a dice
    if Hit_roll >= min(WS - plus_to_hit, Crit_hit) or (
            Hit_reroll == '1' or (Hit_reroll == '2' and Hit_roll == 1) and random.choice(dice) >= WS):
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
        make_wound_roll()


def make_wound_roll():
    Wound_roll = random.choice(dice)
    if Wound_roll >= min(Wound_on, Crit_wound) or (
            Wound_reroll == '1' or (Wound_reroll == '2' and Wound_roll == 1) and random.choice(dice) >= Wound_on):
        Wound = True
    else:
        Wound = False
    if not Wound:
        return
    global success_wounds
    success_wounds += 1
    if Wound_roll >= Crit_wound and Dev_wounds:
        if FNP:
            make_fnp_rolls()
        else:
            if not targets:
                return
            damage = D if D <= targets[0] else targets[0]
            targets[0] -= damage
            global wounds_lost
            wounds_lost += damage
            if targets[0] <= 0:
                targets.pop(0)
                global targets_killed
                targets_killed += 1
    else:
        make_save_roll()


def make_save_roll():
    use_Sv = Sv if Sv + AP <= SvInv else SvInv
    Save_roll = random.choice(dice)
    if Save_roll >= use_Sv:
        return
    global failed_saves
    failed_saves += 1
    if FNP:
        make_fnp_rolls()
    else:
        if not targets:
            return
        damage = D if D <= targets[0] else targets[0]
        targets[0] -= damage
        global wounds_lost
        wounds_lost += damage
        if targets[0] <= 0:
            targets.pop(0)
            global targets_killed
            targets_killed += 1


def make_fnp_rolls():
    if not targets:
        return
    for wound_ in range(D):
        FNP_roll = random.choice(dice)
        if FNP_roll >= FNP:
            continue
        global failed_fnp
        failed_fnp += 1
        targets[0] -= 1
        global wounds_lost
        wounds_lost += 1
        if targets[0] <= 0:
            targets.pop(0)
            global targets_killed
            targets_killed += 1
            break

def calculate():
    for _ in range(tries):
        targets = [W for x in range(amount_targets)]
        attacks = amount_attacks
        success_hits = 0
        success_wounds = 0
        failed_saves = 0
        failed_fnp = 0
        wounds_lost = 0
        targets_killed = 0

        success_wounds_on_list.append(Wound_on)
        while targets and attacks:
            attacks -= 1

            make_hit_roll()

        success_hits_list.append(success_hits)
        success_wounds_list.append(success_wounds)
        failed_saves_list.append(failed_saves)
        failed_fnp_list.append(failed_fnp)
        wounds_lost_list.append(wounds_lost)
        targets_killed_list.append(targets_killed)

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


positions = {
    'labels': {
        'targets_amount_label': {
            'x': 80, 'y': 100
        },
        'attacks_amount_label': {
            'x': 80, 'y': 150
        }
    },
    'editors': {
        'targets_amount_editor': {
            'x': 20, 'y': 100
        },
        'attacks_amount_editor': {
            'x': 20, 'y': 150
        }

    },
    'radiobuttons': {

    }
}


if __name__ == '__main__':
    root = Tk()
    root.title("METANIT.COM")
    root.geometry("550x400")

    info_button = ttk.Button(text="Информация", command=calculate)
    info_button.place(x=20, y=30)

    targets_amount_label = ttk.Label(text="Количество моделей")
    targets_amount_label.place(**positions.get('labels').get('targets_amount_label'))
    targets_amount_editor = Text(height=1, width=6)
    targets_amount_editor.place(**positions.get('editors').get('targets_amount_editor'))

    attacks_amount_label = ttk.Label(text="Количество атак")
    attacks_amount_label.place(**positions.get('labels').get('attacks_amount_label'))
    attacks_amount_editor = Text(height=1, width=6)
    attacks_amount_editor.place(**positions.get('editors').get('attacks_amount_editor'))

    root.mainloop()





