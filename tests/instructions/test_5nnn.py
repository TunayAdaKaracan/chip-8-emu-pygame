from board.cpu import Chip

program = [
    0x61, 0x0A,  # SET R1 = 10
    0x62, 0x0A,  # SET R2 = 10
    0x51, 0x20,  # COMP R1 == R2
    0x63, 0x0B,  # SET R3 = 11
    0x64, 0x0C   # SET R4 = 12
]

chip = Chip(1, False, 1)
chip.load_sprites_to_mem()
chip.load_program_to_mem(program)

for _ in range(len(program) // 2):
    chip.tick()

# Tests
assert chip.registers[1].get() == 10
assert chip.registers[2].get() == 10
assert chip.registers[3].get() == 0
assert chip.registers[4].get() == 12
assert chip.pc == 0x20c