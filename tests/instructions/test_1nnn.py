from board.cpu import Chip

program = [
    0x61, 0x0A,  # SET R1 = 10 | ADDR 0x200
    0x12, 0x06,  # JUMP TO 0x206 | ADDR 0x202
    0x62, 0x0B,  # SET R2 = 11 | ADDR 0x204
    0x63, 0x0C,  # SET R3 = 12 |ADDR 0x206
]

chip = Chip(1, False, 1)
chip.load_sprites_to_mem()
chip.load_program_to_mem(program)

for _ in range(len(program) // 2):
    chip.tick()

# Tests
assert chip.registers[1].get() == 10
assert chip.registers[2].get() == 0
assert chip.registers[3].get() == 12
assert chip.pc == 0x20a
