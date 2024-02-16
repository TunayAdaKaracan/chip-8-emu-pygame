from board.cpu import Chip

chip = Chip(1, False, 1)
chip.load_sprites_to_mem()
chip.load_program_to_mem([
    0x61, 0x0A,  # LD R1 10
    0x62, 0x0A,  # LD R2 10
    0x63, 0x01,  # LD R3 1
    0xF3, 0x29,  # LD ADDR for sprite 1 from reg 3
    0xD1, 0x25
])
chip.tick()
chip.tick()
chip.tick()
chip.tick()
chip.tick()