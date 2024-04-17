import random
from dataclasses import dataclass, field
from enum import StrEnum
from tkinter import StringVar, IntVar
from tkinter.ttk import Entry

from app.utils import D3, D6, D1, def_wound_on, DICE_NAMES


@dataclass
class Position:
    x: int
    y: int


@dataclass
class LabelsPositions:
    targets_amount_label: Position
    attacks_amount_label: Position
    attacks_rand_label: Position
    can_reroll_hits_label: Position
    can_reroll_wounds_label: Position
    will_reroll_hits_label: Position
    will_reroll_wounds_label: Position
    target_W_label: Position
    target_T_label: Position
    target_Sv_label: Position
    target_SvInv_label: Position
    target_FNP_label: Position
    attack_S_label: Position
    attack_WS_label: Position
    attack_D_label: Position
    attack_AP_label: Position
    attack_crit_hit_on_label: Position
    attack_crit_wound_on_label: Position

    sustained_hits_label: Position
    lethal_hits_label: Position
    devastating_wounds_label: Position

    plus_to_hit_label: Position
    plus_to_wound_label: Position

    tries_label: Position


@dataclass
class EditorsPositions:
    targets_amount_editor: Position
    attacks_amount_editor: Position
    attacks_rand_editor: Position
    target_W_editor: Position
    target_T_editor: Position
    target_Sv_editor: Position
    target_SvInv_editor: Position
    target_FNP_editor: Position
    attack_S_editor: Position
    attack_WS_editor: Position
    attack_D_editor: Position
    attack_AP_editor: Position
    attack_crit_hit_on_editor: Position
    attack_crit_wound_on_editor: Position

    sustained_hits_editor: Position

    plus_to_hit_editor: Position
    plus_to_wound_editor: Position

    tries_editor: Position


@dataclass
class CanRerollRBtnPositions:
    none: Position
    all: Position
    ones_only: Position


@dataclass
class WillRerollRBtnPositions:
    except_success: Position
    except_crits: Position


@dataclass
class ButtonsPositions:
    can_reroll_hits: CanRerollRBtnPositions
    can_reroll_wounds: CanRerollRBtnPositions
    will_reroll_hit: WillRerollRBtnPositions
    will_reroll_wounds: WillRerollRBtnPositions
    sustained_hits_button: Position
    lethal_hits_button: Position
    devastating_wounds_button: Position
    info: Position
    calculate: Position


@dataclass
class Positions:
    labels: LabelsPositions
    editors: EditorsPositions
    buttons: ButtonsPositions



@dataclass
class Offsets:
    target_x: int
    target_y: int


@dataclass
class ResultData:
    success_hits_list: list[int] = field(default_factory=list)
    success_wounds_list: list[int] = field(default_factory=list)
    failed_saves_list: list[int] = field(default_factory=list)
    failed_fnp_list: list[int] = field(default_factory=list)
    wounds_lost_list: list[int] = field(default_factory=list)
    targets_killed_list: list[int] = field(default_factory=list)


@dataclass
class BaseData:
    base_attacks: int
    rand_attack: str
    targets: int
    WS: int
    S: int
    AP: int
    D: str
    T: int
    Sv: int
    SvInv: int
    FNP: int
    W: int
    sustained_hits: bool
    sustained_hits_val: int
    lethal_hits: bool
    devastating_wounds: bool
    wound_on: int
    CH: int   # critical hit
    CW: int   # critical wound
    PTH: int  # plus to hit roll
    PTW: int  # plus to wound roll
    CRH: str  # can reroll hits
    CRW: str  # can reroll wounds
    WRH: str  # will reroll hits
    WRW: str  # will reroll wounds
    tries: int

    def prepare_try(self):
        match self.rand_attack:
            case DICE_NAMES.D3_NAME:
                dice = D3
            case DICE_NAMES.D6_NAME:
                dice = D6
            case _:
                dice = D1
        data = OneTryData(
            attacks=sum([random.choice(dice) for _ in range(self.base_attacks)]),
            targets=[self.W for _ in range(self.targets)],
        )
        return data


@dataclass
class OneTryData:
    attacks: int = 1
    targets: list[int] = field(default_factory=list)
    success_hits: int = 0
    success_wounds: int = 0
    failed_saves: int = 0
    failed_fnp: int = 0
    wounds_lost: int = 0
    targets_killed: int = 0



@dataclass
class DataAccessor:
    targets_amount_editor: Entry
    attacks_amount_editor: Entry
    attacks_rand_editor: Entry
    target_W_editor: Entry
    target_T_editor: Entry
    target_Sv_editor: Entry
    target_SvInv_editor: Entry
    target_FNP_editor: Entry
    attacks_WS_editor: Entry
    attacks_S_editor: Entry
    attacks_D_editor: Entry
    attacks_AP_editor: Entry
    crit_hit_on_editor: Entry
    crit_wound_on_editor: Entry
    sustained_hits_enabled: IntVar
    sustained_hits_editor: Entry
    lethal_hits_enabled: IntVar
    devastating_wounds_enabled: IntVar
    plus_to_hit_editor: Entry
    plus_to_wound_editor: Entry
    can_reroll_hits_var: StringVar
    can_reroll_wounds_var: StringVar
    will_reroll_hits_var: StringVar
    will_reroll_wounds_var: StringVar
    tries_editor: Entry


    def get_data(self):
        wound_on = def_wound_on(self.S, self.T, plus_to_wound=self.PTW)
        data = BaseData(
            base_attacks=self.attacks_amount,
            rand_attack=self.attacks_random,
            targets=self.targets_amount,
            WS=self.WS,
            S=self.S,
            AP=self.AP,
            D=self.D,
            T=self.T,
            Sv=self.Sv,
            SvInv=self.SvInv,
            FNP=self.FNP,
            W=self.W,
            sustained_hits=self.sustained_hits,
            sustained_hits_val=self.sustained_hits_val,
            lethal_hits=self.sustained_hits,
            devastating_wounds=self.devastating_wounds,
            wound_on=wound_on,
            CRH=self.can_reroll_hits,
            CRW=self.can_reroll_wounds,
            WRH=self.will_reroll_hits,
            WRW=self.will_reroll_wounds,
            PTH=self.PTH,
            PTW=self.PTW,
            tries=self.tries,
            CH=self.crit_hit_on,
            CW=self.crit_wound_on
        )
        return data


    @staticmethod
    def _return_val_int(editor: IntVar | Entry) -> int:
        try:
            return int(editor.get())
        except:
            return 1

    @staticmethod
    def _return_val_str(editor: StringVar | Entry) -> str:
        try:
            return str(editor.get())
        except:
            return ''

    @property
    def tries(self) -> int:
        return self._return_val_int(self.tries_editor)

    @property
    def targets_amount(self) -> int:
        return self._return_val_int(self.targets_amount_editor)

    @property
    def attacks_amount(self) -> int:
        return self._return_val_int(self.attacks_amount_editor)

    @property
    def attacks_random(self) -> str:
        return self._return_val_str(self.attacks_rand_editor)

    @property
    def W(self) -> int:
        return self._return_val_int(self.target_W_editor)
    @property

    def T(self) -> int:
        return self._return_val_int(self.target_T_editor)

    @property
    def Sv(self) -> int:
        return self._return_val_int(self.target_Sv_editor)

    @property
    def SvInv(self) -> int:
        return self._return_val_int(self.target_SvInv_editor)

    @property
    def FNP(self) -> int:
        return self._return_val_int(self.target_FNP_editor)

    @property
    def WS(self) -> int:
        return self._return_val_int(self.attacks_WS_editor)

    @property
    def S(self) -> int:
        return self._return_val_int(self.attacks_S_editor)

    @property
    def D(self) -> str:
        return self._return_val_str(self.attacks_D_editor)

    @property
    def AP(self) -> int:
        return self._return_val_int(self.attacks_AP_editor)

    @property
    def crit_hit_on(self) -> int:
        return self._return_val_int(self.crit_hit_on_editor)

    @property
    def crit_wound_on(self) -> int:
        return self._return_val_int(self.crit_wound_on_editor)

    @property
    def PTW(self) -> int:
        """
        plus to wound
        """
        return self._return_val_int(self.plus_to_wound_editor)

    @property
    def PTH(self) -> int:
        """
        plus to hit
        """
        return self._return_val_int(self.plus_to_hit_editor)

    @property
    def can_reroll_hits(self) -> str:
        return self._return_val_str(self.can_reroll_hits_var)

    @property
    def can_reroll_wounds(self) -> str:
        return self._return_val_str(self.can_reroll_wounds_var)

    @property
    def will_reroll_hits(self) -> str:
        return self._return_val_str(self.will_reroll_hits_var)

    @property
    def will_reroll_wounds(self) -> str:
        return self._return_val_str(self.will_reroll_wounds_var)

    @property
    def sustained_hits(self) -> bool:
        return bool(self._return_val_int(self.sustained_hits_enabled))

    @property
    def sustained_hits_val(self) -> int:
        return self._return_val_int(self.sustained_hits_editor)

    @property
    def lethal_hits(self) -> bool:
        return bool(self._return_val_int(self.lethal_hits_enabled))

    @property
    def devastating_wounds(self) -> bool:
        return bool(self._return_val_int(self.devastating_wounds_enabled))

