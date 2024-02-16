DEFAULT_KEYBINDINGS = {
    49: 0x1,  # 1
    50: 0x2,  # 2
    51: 0x3,  # 3
    52: 0xc,  # 4
    113: 0x4,  # Q
    119: 0x5,  # W
    101: 0x6,  # E
    114: 0xD,  # R
    97: 0x7,  # A
    115: 0x8,  # S
    100: 0x9,  # D
    102: 0xE,  # F
    122: 0xA,  # Z
    120: 0x0,  # X
    99: 0xB,  # C
    118: 0xF  # V
}

PACMAN = DEFAULT_KEYBINDINGS.copy()
PACMAN[119] = 0x3
PACMAN[115] = 0x6
PACMAN[100] = 0x8


class VirtualKeyboard:
    def __init__(self, key_bindings=None):
        self.KEYMAP = key_bindings or PACMAN

        self.keys_pressed = []

        self.key_press_event = None

    def is_key_pressed(self, key):
        return key in self.keys_pressed

    def key_down(self, key):
        if key not in self.KEYMAP:
            return
        self.keys_pressed.append(self.KEYMAP[key])
        if self.key_press_event:
            self.key_press_event(self.KEYMAP[key])
            self.key_press_event = None

    def key_up(self, key):
        if key not in self.KEYMAP:
            return
        self.keys_pressed.remove(self.KEYMAP[key])
