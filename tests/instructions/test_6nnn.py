from board.cpu import Chip

program = [
    0x60, 0x00,  # SET R0 0
    0x61, 0x01,  # SET R1 1
    0x62, 0x02,  # SET R2 2
    0x63, 0x03,  # SET R3 3
    0x64, 0x04,  # SET R4 4
    0x65, 0x05,  # SET R5 5
    0x66, 0x06,  # SET R6 6
    0x67, 0x07,  # SET R7 7
    0x68, 0x08,  # SET R8 8
    0x69, 0x09,  # SET R9 9
    0x6A, 0x0A,  # SET R10 10
    0x6B, 0x0B,  # SET R11 11
    0x6C, 0x0C,  # SET R12 12
    0x6D, 0x0D,  # SET R13 13
    0x6E, 0x0E,  # SET R14 14
    0x6F, 0x0F,  # SET R15 15
]

chip = Chip(1, False, 1)
chip.load_sprites_to_mem()
chip.load_program_to_mem(program)

for _ in range(len(program) // 2):
    chip.tick()

# Tests
for i, register in enumerate(chip.registers):
    assert register.get() == i