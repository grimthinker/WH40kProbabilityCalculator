from app.classes import Offsets, Positions, LabelsPositions, Position, EditorsPositions, ButtonsPositions, \
    CanRerollRBtnPositions, WillRerollRBtnPositions

WINDOW_NAME = "WH40k Probability Calculator"
WINDOW_SIZE = "1100x600"

offsets = Offsets(
    target_x=20,
    target_y=0
)

positions = Positions(
    LabelsPositions(
        targets_amount_label=Position(20, 100),
        attacks_amount_label=Position(20, 150),
        can_reroll_hits_label=Position(20, 200),
        can_reroll_wounds_label=Position(20, 280),
        will_reroll_hits_label=Position(230, 200),
        will_reroll_wounds_label=Position(230, 280),

        target_T_label=Position(520, 100),
        target_W_label=Position(520, 150),
        target_Sv_label=Position(520, 200),
        target_SvInv_label=Position(520, 250),
        target_FNP_label=Position(520, 300),

        attack_S_label=Position(280-50, 150),
        attack_WS_label=Position(270-50, 100),
        attack_D_label=Position(360, 100),

        plus_to_wound_label=Position(20, 370),

        tries_label=Position(650, 70)
    ),
    EditorsPositions(
        targets_amount_editor=Position(110, 100),
        attacks_amount_editor=Position(110, 150),

        target_T_editor=Position(540, 100),
        target_W_editor=Position(540, 150),
        target_Sv_editor=Position(540, 200),
        target_SvInv_editor=Position(560, 250),
        target_FNP_editor=Position(560, 300),

        attack_S_editor=Position(250, 150),
        attack_WS_editor=Position(250, 100),
        attack_D_editor=Position(380, 100),

        plus_to_wound_editor=Position(90, 370),

        tries_editor=Position(740, 70)
    ),
    ButtonsPositions(
        can_reroll_hits=CanRerollRBtnPositions(
            none=Position(110, 200),
            all=Position(110, 240),
            ones_only=Position(110, 220),
        ),
        can_reroll_wounds=CanRerollRBtnPositions(
            none=Position(110, 280),
            all=Position(110, 320),
            ones_only=Position(110, 300),
        ),
        will_reroll_hit=WillRerollRBtnPositions(
            except_success=Position(310, 200),
            except_crits=Position(310, 220),
        ),
        will_reroll_wounds=WillRerollRBtnPositions(
            except_success=Position(320, 280),
            except_crits=Position(320, 300),
        ),
        info=Position(20, 20),
        calculate=Position(800, 70)
    ),
)




