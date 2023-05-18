## LEFT
import board
from kmk.modules.split import SplitSide
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.GP2,
                board.GP3,
                board.GP4,
                board.GP5
                )
    row_pins = (board.GP6,
				board.GP7)
    diode_orientation = DiodeOrientation.COL2ROW
    led_key_pos=[
        0,2
        ]
    brightness_limit = 1.0
    num_pixels = 1

