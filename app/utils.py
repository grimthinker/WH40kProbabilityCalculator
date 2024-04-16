import random
from enum import StrEnum


class DICE_NAMES(StrEnum):
    D3_NAME = 'D3'
    D6_NAME = 'D6'


class CRO(StrEnum):
    """
    CanRerollOptions
    """
    NOT = 'not'
    ALL = 'all'
    ONES_ONLY = 'ones only'


class WRO(StrEnum):
    """
    WillRerollOptions
    """
    A_E_S = 'all except successes'
    A_E_C = 'all except crits'

D6 = [1, 2, 3, 4, 5, 6]
D3 = [1, 2, 3]
D1 = [1]
D0 = [0]

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


def is_int(val) -> bool:
    try:
        int(val)
        return True
    except:
        return False


def get_damage(base_damage: str) -> int:
    """
    :param base_damage: "[{mult}][{dice}][+{const}]" or "{const}", examples: 12, D3, 3D6, 2D3+2
    :return:
    """
    damage_list = base_damage.split("+")
    if len(damage_list) == 2:
        rand_damage, const_damage = damage_list
    elif len(damage_list) == 1:
        [rand_damage, const_damage] = [damage_list[0], '0'] if ('D' in damage_list[0]) else ['0', damage_list[0]]
    else:
        return 1
    mult = 1
    if len(rand_damage) > 2:  # like in 3D6
        mult = int(rand_damage[:2]) if is_int(rand_damage[:2]) else mult
    match rand_damage:
        case DICE_NAMES.D3_NAME:
            dice = D3
        case DICE_NAMES.D6_NAME:
            dice = D6
        case _:
            dice = D0
    const_damage = int(const_damage) if is_int(const_damage) else 1
    full_damage = const_damage + random.choice(dice) * mult
    return full_damage

