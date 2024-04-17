from dataclasses import asdict
from tkinter import ttk, StringVar, Tk, IntVar

from app.classes import DataAccessor
from app.service import Calculator, info
from app.utils import is_int, WRO, CRO
from config import positions, WINDOW_SIZE, WINDOW_NAME


def place_can_reroll_hits_rbtn(can_reroll_hits_variable: StringVar):
    can_reroll_hits_label = ttk.Label(text="Can reroll\nHIT ROLLS")
    can_reroll_hits_label.place(**asdict(positions.labels.can_reroll_hits_label))

    can_reroll_hits_not_btn = ttk.Radiobutton(text=CRO.NOT.value, value=CRO.NOT.value, variable=can_reroll_hits_variable)
    can_reroll_hits_not_btn.place(**asdict(positions.buttons.can_reroll_hits.none))

    can_reroll_hits_all_btn = ttk.Radiobutton(text=CRO.ALL.value, value=CRO.ALL.value, variable=can_reroll_hits_variable)
    can_reroll_hits_all_btn.place(**asdict(positions.buttons.can_reroll_hits.all))

    can_reroll_hits_ones_btn = ttk.Radiobutton(text=CRO.ONES_ONLY.value, value=CRO.ONES_ONLY.value, variable=can_reroll_hits_variable)
    can_reroll_hits_ones_btn.place(**asdict(positions.buttons.can_reroll_hits.ones_only))

def place_can_reroll_wounds_rbtn(can_reroll_wounds_variable: StringVar):
    can_reroll_wounds_label = ttk.Label(text="Can reroll\nWOUND ROLLS")
    can_reroll_wounds_label.place(**asdict(positions.labels.can_reroll_wounds_label))

    can_reroll_wounds_not_btn = ttk.Radiobutton(text=CRO.NOT.value, value=CRO.NOT.value, variable=can_reroll_wounds_variable)
    can_reroll_wounds_not_btn.place(**asdict(positions.buttons.can_reroll_wounds.none))

    can_reroll_wounds_all_btn = ttk.Radiobutton(text=CRO.ALL.value, value=CRO.ALL.value, variable=can_reroll_wounds_variable)
    can_reroll_wounds_all_btn.place(**asdict(positions.buttons.can_reroll_wounds.all))

    can_reroll_wounds_ones_btn = ttk.Radiobutton(text=CRO.ONES_ONLY.value, value=CRO.ONES_ONLY.value, variable=can_reroll_wounds_variable)
    can_reroll_wounds_ones_btn.place(**asdict(positions.buttons.can_reroll_wounds.ones_only))


def place_will_reroll_hits_rbtn(will_reroll_hits_variable: StringVar):
    will_reroll_hits_label = ttk.Label(text="Will reroll\nHIT ROLLS")
    will_reroll_hits_label.place(**asdict(positions.labels.will_reroll_hits_label))

    will_reroll_wounds_1_btn = ttk.Radiobutton(text=WRO.A_E_S.value, value=WRO.A_E_S.value, variable=will_reroll_hits_variable)
    will_reroll_wounds_1_btn.place(**asdict(positions.buttons.will_reroll_hit.except_success))

    will_reroll_wounds_2_btn = ttk.Radiobutton(text=WRO.A_E_C.value, value=WRO.A_E_C.value, variable=will_reroll_hits_variable)
    will_reroll_wounds_2_btn.place(**asdict(positions.buttons.will_reroll_hit.except_crits))


def place_will_reroll_wounds_rbtn(will_reroll_wounds_variable: StringVar):
    will_reroll_wounds_label = ttk.Label(text="Will reroll\nWOUND ROLLS")
    will_reroll_wounds_label.place(**asdict(positions.labels.will_reroll_wounds_label))

    will_reroll_wounds_1_btn = ttk.Radiobutton(text=WRO.A_E_S.value, value=WRO.A_E_S.value, variable=will_reroll_wounds_variable)
    will_reroll_wounds_1_btn.place(**asdict(positions.buttons.will_reroll_wounds.except_success))

    will_reroll_wounds_2_btn = ttk.Radiobutton(text=WRO.A_E_C.value, value=WRO.A_E_C.value, variable=will_reroll_wounds_variable)
    will_reroll_wounds_2_btn.place(**asdict(positions.buttons.will_reroll_wounds.except_crits))


def setup_app():
    root = Tk()
    root.title(WINDOW_NAME)
    root.geometry(WINDOW_SIZE)

    check = (root.register(is_int), "%P")
    make_int_entry = lambda: ttk.Entry(width=6, validate="key", validatecommand=check)

    targets_amount_label = ttk.Label(text="Targets amount")
    targets_amount_label.place(**asdict(positions.labels.targets_amount_label))
    targets_amount_editor = make_int_entry()
    targets_amount_editor.place(**asdict(positions.editors.targets_amount_editor))

    attacks_amount_label = ttk.Label(text="Attacks amount")
    attacks_amount_label.place(**asdict(positions.labels.attacks_amount_label))
    attacks_amount_editor = make_int_entry()
    attacks_amount_editor.place(**asdict(positions.editors.attacks_amount_editor))
    attacks_rand_label = ttk.Label(text="Attacks random")
    attacks_rand_label.place(**asdict(positions.labels.attacks_rand_label))
    attacks_rand_editor = make_int_entry()
    attacks_rand_editor.place(**asdict(positions.editors.attacks_rand_editor))

    target_W_label = ttk.Label(text="W")
    target_W_label.place(**asdict(positions.labels.target_W_label))
    target_W_editor = make_int_entry()
    target_W_editor.place(**asdict(positions.editors.target_W_editor))
    target_T_label = ttk.Label(text="T")
    target_T_label.place(**asdict(positions.labels.target_T_label))
    target_T_editor = make_int_entry()
    target_T_editor.place(**asdict(positions.editors.target_T_editor))
    target_Sv_label = ttk.Label(text="Sv")
    target_Sv_label.place(**asdict(positions.labels.target_Sv_label))
    target_Sv_editor = make_int_entry()
    target_Sv_editor.place(**asdict(positions.editors.target_Sv_editor))
    target_SvInv_label = ttk.Label(text="InvSv")
    target_SvInv_label.place(**asdict(positions.labels.target_SvInv_label))
    target_SvInv_editor = make_int_entry()
    target_SvInv_editor.place(**asdict(positions.editors.target_SvInv_editor))
    target_FNP_label = ttk.Label(text="FNP")
    target_FNP_label.place(**asdict(positions.labels.target_FNP_label))
    target_FNP_editor = make_int_entry()
    target_FNP_editor.place(**asdict(positions.editors.target_FNP_editor))

    attack_WS_label = ttk.Label(text="WS")
    attack_WS_label.place(**asdict(positions.labels.attack_WS_label))
    attack_WS_editor = make_int_entry()
    attack_WS_editor.place(**asdict(positions.editors.attack_WS_editor))
    attack_S_label = ttk.Label(text="S")
    attack_S_label.place(**asdict(positions.labels.attack_S_label))
    attack_S_editor = make_int_entry()
    attack_S_editor.place(**asdict(positions.editors.attack_S_editor))
    attack_D_label = ttk.Label(text="D")
    attack_D_label.place(**asdict(positions.labels.attack_D_label))
    attack_D_editor = make_int_entry()
    attack_D_editor.place(**asdict(positions.editors.attack_D_editor))
    attack_AP_label = ttk.Label(text="AP")
    attack_AP_label.place(**asdict(positions.labels.attack_AP_label))
    attack_AP_editor = make_int_entry()
    attack_AP_editor.place(**asdict(positions.editors.attack_AP_editor))
    attack_crit_hit_on_label = ttk.Label(text="CRITICAL HIT on")
    attack_crit_hit_on_label.place(**asdict(positions.labels.attack_crit_hit_on_label))
    attack_crit_hit_on_editor = make_int_entry()
    attack_crit_hit_on_editor.place(**asdict(positions.editors.attack_crit_hit_on_editor))
    attack_crit_wound_on_label = ttk.Label(text="CRITICAL WOUND on")
    attack_crit_wound_on_label.place(**asdict(positions.labels.attack_crit_wound_on_label))
    attack_crit_wound_on_editor = make_int_entry()
    attack_crit_wound_on_editor.place(**asdict(positions.editors.attack_crit_wound_on_editor))

    lethal_hits_label = ttk.Label(text="LETHAL HITS")
    lethal_hits_label.place(**asdict(positions.labels.lethal_hits_label))
    lethal_hits_enabled = IntVar()
    lethal_hits_button = ttk.Checkbutton(text="", variable=lethal_hits_enabled)
    lethal_hits_button.place(**asdict(positions.buttons.lethal_hits_button))
    sustained_hits_label = ttk.Label(text="SUSTAINED HITS")
    sustained_hits_label.place(**asdict(positions.labels.sustained_hits_label))
    sustained_hits_editor = make_int_entry()
    sustained_hits_editor.place(**asdict(positions.editors.sustained_hits_editor))
    sustained_hits_enabled = IntVar()
    sustained_hits_button = ttk.Checkbutton(text="", variable=sustained_hits_enabled)
    sustained_hits_button.place(**asdict(positions.buttons.sustained_hits_button))

    devastating_wounds_label = ttk.Label(text="DEVASTATING WOUNDS")
    devastating_wounds_label.place(**asdict(positions.labels.devastating_wounds_label))
    devastating_wounds_enabled = IntVar()
    devastating_wounds_button = ttk.Checkbutton(text="", variable=devastating_wounds_enabled)
    devastating_wounds_button.place(**asdict(positions.buttons.devastating_wounds_button))


    plus_to_hit_label = ttk.Label(text="Plus to HR")
    plus_to_hit_label.place(**asdict(positions.labels.plus_to_hit_label))
    plus_to_hit_editor = make_int_entry()
    plus_to_hit_editor.place(**asdict(positions.editors.plus_to_hit_editor))
    plus_to_wound_label = ttk.Label(text="Plus to WR")
    plus_to_wound_label.place(**asdict(positions.labels.plus_to_wound_label))
    plus_to_wound_editor = make_int_entry()
    plus_to_wound_editor.place(**asdict(positions.editors.plus_to_wound_editor))


    tries_label = ttk.Label(text="Amount of tries")
    tries_label.place(**asdict(positions.labels.tries_label))
    tries_editor = make_int_entry()
    tries_editor.place(**asdict(positions.editors.tries_editor))

    can_reroll_hits_var = StringVar(value=CRO.NOT.value)
    can_reroll_wounds_var = StringVar(value=CRO.NOT.value)
    will_reroll_hits_var = StringVar(value=WRO.A_E_S.value)
    will_reroll_wounds_var = StringVar(value=WRO.A_E_S.value)

    place_can_reroll_hits_rbtn(can_reroll_hits_var)
    place_can_reroll_wounds_rbtn(can_reroll_wounds_var)
    place_will_reroll_hits_rbtn(will_reroll_hits_var)
    place_will_reroll_wounds_rbtn(will_reroll_wounds_var)
    calculator = Calculator(
        attacks_amount_editor=attacks_amount_editor,
        attacks_rand_editor=attacks_rand_editor,
        targets_amount_editor=targets_amount_editor,
        attacks_D_editor=attack_D_editor,
        attacks_S_editor=attack_S_editor,
        attacks_WS_editor=attack_WS_editor,
        crit_hit_on_editor=attack_crit_hit_on_editor,
        crit_wound_on_editor=attack_crit_wound_on_editor,
        attacks_AP_editor=attack_AP_editor,
        target_Sv_editor=target_Sv_editor,
        target_SvInv_editor=target_SvInv_editor,
        target_T_editor=target_T_editor,
        target_W_editor=target_W_editor,
        target_FNP_editor=target_FNP_editor,
        sustained_hits_enabled=sustained_hits_enabled,
        sustained_hits_editor=sustained_hits_editor,
        lethal_hits_enabled=lethal_hits_enabled,
        devastating_wounds_enabled=devastating_wounds_enabled,
        plus_to_hit_editor=plus_to_hit_editor,
        plus_to_wound_editor=plus_to_wound_editor,
        can_reroll_hits_var=can_reroll_hits_var,
        can_reroll_wounds_var=can_reroll_wounds_var,
        will_reroll_hits_var=will_reroll_hits_var,
        will_reroll_wounds_var=will_reroll_wounds_var,
        tries_editor=tries_editor
    )

    info_button = ttk.Button(text="Info (not working)", command=info)
    info_button.place(**asdict(positions.buttons.info))
    info_button = ttk.Button(text="Calculate", command=calculator.calculate)
    info_button.place(**asdict(positions.buttons.calculate))

    # fill entries
    attacks_rand_editor.insert(0, '1')
    attack_crit_hit_on_editor.insert(0, '6')
    attack_crit_wound_on_editor.insert(0, '6')
    plus_to_hit_editor.insert(0, '0')
    plus_to_wound_editor.insert(0, '0')
    target_FNP_editor.insert(0, '7')
    tries_editor.insert(0, '10000')

    return root
