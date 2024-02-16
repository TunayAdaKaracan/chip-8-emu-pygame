from board.cpu import Chip

program = [
    0x60, 0x06,  # SET R0 = 6
    0xB2, 0x00,  # PC = R0 + 0x200
    0x61, 0x0B,  # SET R1 = 11
    0x62, 0x0C   # SET R2 = 12
]

chip = Chip(1, False, 1)
chip.load_sprites_to_mem()
chip.load_program_to_mem(program)

for _ in range(len(program) // 2):
    chip.tick()

assert chip.registers[0].get() == 6
assert chip.registers[1].get() == 0
assert chip.registers[2].get() == 12
assert chip.pc == 0x20a