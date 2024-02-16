from board.cpu import Chip

program = [
    0x12, 0x08,  # JUMP TO 0x208 | ADDR 0x200

    # Function sets R1, R2
    0x61, 0x0A,  # SET R1 = 10 | ADDR 0x202
    0x62, 0x0C,  # SET R2 = 12 | ADDR 0x204
    0x00, 0xEE,  # RET | 206

    0x63, 0x0B,  # SET R3 = 11 | ADDR 0x208
    0x22, 0x02,  # CALL ADDR 202 | ADDR 0x20A

    0xF3, 0x29,  # ADDR = R3 * 5 | ADDR 0x20C
]

chip = Chip(1, False, 1)
chip.load_sprites_to_mem()
chip.load_program_to_mem(program)

for _ in range(len(program) // 2):
    chip.tick()

assert chip.registers[1].get() == 10
assert chip.registers[2].get() == 12
assert chip.registers[3].get() == 11
assert chip.address.get() == 55
assert len(chip.stack) == 0