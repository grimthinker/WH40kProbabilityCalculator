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
        targets_amount_label=Position(340, 50),
        attacks_rand_label=Position(170, 50),
        attacks_amount_label=Position(20, 50),
        can_reroll_hits_label=Position(20, 200),
        can_reroll_wounds_label=Position(20, 280),
        will_reroll_hits_label=Position(230, 200),
        will_reroll_wounds_label=Position(230, 280),

        target_T_label=Position(520, 100),
        target_W_label=Position(520, 150),
        target_Sv_label=Position(520, 200),
        target_SvInv_label=Position(520, 250),
        target_FNP_label=Position(520, 300),

        attack_S_label=Position(120, 100),
        attack_WS_label=Position(20, 100),
        attack_D_label=Position(320, 100),
        attack_AP_label=Position(215, 100),
        attack_crit_hit_on_label=Position(20, 150),
        attack_crit_wound_on_label=Position(195, 150),

        sustained_hits_label=Position(20, 420),
        lethal_hits_label=Position(20, 450),
        devastating_wounds_label=Position(20, 480),

        plus_to_hit_label=Position(20, 370),
        plus_to_wound_label=Position(170, 370),

        tries_label=Position(650, 70)
    ),
    EditorsPositions(
        targets_amount_editor=Position(440, 50),
        attacks_amount_editor=Position(110, 50),
        attacks_rand_editor=Position(260, 50),

        target_T_editor=Position(540, 100),
        target_W_editor=Position(540, 150),
        target_Sv_editor=Position(540, 200),
        target_SvInv_editor=Position(560, 250),
        target_FNP_editor=Position(560, 300),

        attack_S_editor=Position(140, 100),
        attack_WS_editor=Position(50, 100),
        attack_D_editor=Position(340, 100),
        attack_AP_editor=Position(240, 100),
        attack_crit_hit_on_editor=Position(120, 150),
        attack_crit_wound_on_editor=Position(320, 150),

        sustained_hits_editor=Position(150, 420),

        plus_to_hit_editor=Position(90, 370),
        plus_to_wound_editor=Position(240, 370),

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

        sustained_hits_button=Position(120, 420),
        lethal_hits_button=Position(100, 450),
        devastating_wounds_button=Position(160, 480),
        info=Position(20, 550),
        calculate=Position(800, 70)
    ),
)




