print("Starting")
from kb import KMKKeyboard
from kmk.keys import KC
from kmK.handlers.sequences import send_string, simple_key_sequence
from kmk.modules.layers import Layers
from kmk.modules.oneshot import OneShot
keyboard = KMKKeyboard()

print("Media keys")
from kmk.extensions.media_keys import MediaKeys
keyboard.extensions.append(MediaKeys())

print("Layers")
keyboard.modules.append(Layers())

TAP_A = KC.LT(1, KC.A)
TAP_E = KC.LT(3, KC.E)
TAP_S = KC.LT(2, KC.S)
TAP_O = KC.LT(4, KC.O)
DF_NAV  = KC.DF(5)
DF_BASE = KC.DF(0)

print("Keymap")
keyboard.keymap = [
   [ # 0 - Default
     TAP_A  , KC.R    , KC.T    , TAP_S,
     TAP_E  , KC.Y    , KC.I    , TAP_O ],
   [ # 
     KC.NONE  , send_string("(") , send_string(")") , KC.LSFT(KC.RBRC) ,
     KC.NONE  , KC.RBRC          , KC.BSLS          , KC.LSFT(KC.BSLS) ],
   [ # 
     KC.N1  , KC.N2  , KC.N3  , KC.NONE ,
     KC.N4  , KC.N5  , KC.N6  , KC.NONE  ],
   [ # 
     send_string("!")  , KC.NUBS          , KC.SLSH          , send_string("`") ,
     KC.NONE           , KC.LSFT(KC.INT1) , send_string("-") , send_string("=") ],
   [ # 
     KC.MUTE  , KC.INS  , KC.VOLU  , KC.NONE ,
     KC.RSFT  , KC.PSCR , KC.VOLD  , KC.NONE  ],

   [ # 5 - NAV Layer
     KC.HOME, KC.UP,   KC.END,  KC.PGUP,
     KC.LEFT, KC.DOWN, KC.RGHT, KC.PGDN],
]

print("OneShot")
oneshot = OneShot()
#oneshot.tap_time = 1500
keyboard.modules.append(oneshot)

OS_LSFT = KC.OS(KC.LSFT, tap_time=None)
OS_LCTL = KC.OS(KC.LCTL, tap_time=None)
OS_LALT = KC.OS(KC.LALT, tap_time=None)

print("Combos")
from kmk.modules.combos import Combos, Chord, Sequence
combos = Combos()
keyboard.modules.append(combos)
combos.combos = [
    # A
    Chord((TAP_E, TAP_O),              KC.B),
    Chord((TAP_E, KC.Y),               KC.C),
    Chord((TAP_A, KC.R, KC.T),         KC.D),
    # E
    Chord((TAP_A, KC.R),               KC.F),
    Chord((KC.R, KC.T),                KC.G),
    Chord((TAP_E, KC.I),               KC.H),
    # I
    Chord((KC.T, TAP_S),               KC.J),
    Chord((KC.Y, TAP_O),               KC.K),
    Chord((TAP_E, KC.Y, KC.I),         KC.L),
    Chord((KC.Y, KC.I, TAP_O),         KC.M),
    Chord((KC.I, TAP_O),               KC.N),
    # O
    Chord((TAP_E, KC.I, TAP_O),        KC.P),
    Chord((TAP_A, KC.T, TAP_S),        KC.Q),
    # R
    # S
    # T
    Chord((KC.Y, KC.I),                KC.U),
    Chord((KC.R, TAP_S),               KC.V),
    Chord((TAP_A, TAP_S),              KC.W),
    Chord((KC.R, KC.T, TAP_S),         KC.X),
    # Y
    Chord((TAP_A, KC.R, KC.T, TAP_S),  KC.Z),
    #
    Chord((TAP_A, TAP_E),              KC.ENTER),
    Chord((TAP_A, KC.Y, KC.I),         KC.GRV),
    Chord((TAP_A, KC.Y),               KC.DOT),
    Chord((TAP_A, KC.I),               KC.COMM),
    Chord((TAP_A, TAP_O),              KC.INT1),
    Chord((KC.T, KC.I),                send_string("!")),
    Chord((TAP_E, KC.Y, KC.I, TAP_O),  KC.SPC),
    Chord((TAP_E, KC.R), KC.BSPC),
    Chord((KC.R, KC.I), KC.DEL),
    #
    Chord((TAP_A, KC.R, TAP_O),        KC.ESC),
    Chord((TAP_A, KC.R, KC.T, TAP_O),  KC.TAB),
    Chord((TAP_A, KC.Y, KC.I, TAP_O),  KC.CAPS),
    Chord((KC.Y, TAP_S),               KC.LGUI),
    Chord((KC.R, KC.Y),                KC.LSFT),
    #
    Chord((TAP_E, TAP_S),              OS_LCTL),
    Chord((KC.I, TAP_S),               OS_LALT),
    Chord((TAP_E, KC.R, KC.T, TAP_S),  OS_LSFT),
    #
    Chord((KC.N1, KC.N2),              KC.N7),
    Chord((KC.N2, KC.N3),              KC.N8),
    Chord((KC.N4, KC.N5),              KC.N9),
    Chord((KC.N5, KC.N6),              KC.N0),
    # LAYER Trigger Chords ####
    Chord((KC.R, TAP_E, KC.I),         DF_NAV),
    Chord((KC.UP, KC.LEFT, KC.RGHT),   DF_BASE),
    # Brasil
    Chord((TAP_S, TAP_O),              KC.SCLN),  # Ç
    Chord((KC.Y,  KC.T ),              KC.LBRC),  # Agudo
    Chord((KC.T,  TAP_O),              KC.LSFT(KC.LBRC)),  # Crase
    Chord((KC.T,  TAP_E),              KC.QUOT),  # Til
    Chord((KC.T,  TAP_A),              KC.LSFT(KC.QUOT)),  # Circunflexo
]

print("Ok")
if __name__ == '__main__':
    keyboard.go()
