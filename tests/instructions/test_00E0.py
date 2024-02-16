from board.cpu import Chip

program = [
    0x61, 0x0A,  # SET R1 = 10
    0x62, 0x0A,  # SET R2 = 10
    0x63, 0x01,  # SET R3 = 1
    0xF3, 0x29,  # ADDR = R3 * 5
    0xD1, 0x25,  # DRAW AT R1, R2 SPRITE LENGTH = 5
    0x00, 0xE0   # CLEAR SCREEN
]

chip = Chip(1, False, 1)
chip.load_sprites_to_mem()
chip.load_program_to_mem(program)

for _ in range(len(program) // 2):
    chip.tick()

assert all([val == 0 for val in chip.screen.display]), "Needs to be all 0"
