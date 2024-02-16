from board.cpu import Chip

program = [
    0x61, 0x0A,  # SET R1 = 10
    0x41, 0x0B,  # COMP NEQ R1 = 11
    0x62, 0x0C,  # SET R2 = 12
    0x63, 0x0F   # SET R3 = 15
]

chip = Chip(1, False, 1)
chip.load_sprites_to_mem()
chip.load_program_to_mem(program)

for _ in range(len(program) // 2):
    chip.tick()

# Tests
assert chip.registers[1].get() == 10
assert chip.registers[2].get() == 0
assert chip.registers[3].get() == 15
assert chip.pc == 0x20a