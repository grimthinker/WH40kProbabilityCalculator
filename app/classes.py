from dataclasses import dataclass, field
from enum import StrEnum
from tkinter import StringVar
from tkinter.ttk import Entry


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


@dataclass
class Position:
    x: int
    y: int


@dataclass
class LabelsPositions:
    targets_amount_label: Position
    attacks_amount_label: Position
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

    plus_to_wound_label: Position

    tries_label: Position


@dataclass
class EditorsPositions:
    targets_amount_editor: Position
    attacks_amount_editor: Position
    target_W_editor: Position
    target_T_editor: Position
    target_Sv_editor: Position
    target_SvInv_editor: Position
    target_FNP_editor: Position
    attack_S_editor: Position
    attack_WS_editor: Position
    attack_D_editor: Position

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
    success_wounds_on_list: list[int] = field(default_factory=list)
    success_hits_list: list[int] = field(default_factory=list)
    success_wounds_list: list[int] = field(default_factory=list)
    failed_saves_list: list[int] = field(default_factory=list)
    failed_fnp_list: list[int] = field(default_factory=list)
    wounds_lost_list: list[int] = field(default_factory=list)
    targets_killed_list: list[int] = field(default_factory=list)


@dataclass
class Data:
    targets_amount_editor: Entry
    attacks_amount_editor: Entry
    target_W_editor: Entry
    target_T_editor: Entry
    target_Sv_editor: Entry
    target_SvInv_editor: Entry
    target_FNP_editor: Entry
    attacks_WS_editor: Entry
    attacks_S_editor: Entry
    attacks_D_editor: Entry
    plus_to_wound_editor: Entry
    can_reroll_hits_var: StringVar
    can_reroll_wounds_var: StringVar
    will_reroll_hits_var: StringVar
    will_reroll_wounds_var: StringVar
    tries_editor: Entry


    @staticmethod
    def _return_val_int(editor: Entry) -> int:
        try:
            return int(editor.get())
        except:
            return 1

    @staticmethod
    def _return_val_str(editor: StringVar) -> str:
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
    def D(self) -> int:
        return self._return_val_int(self.attacks_D_editor)

    @property
    def PTW(self) -> int:
        """
        plus to wound
        """
        return self._return_val_int(self.plus_to_wound_editor)

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




