from board.cpu import Chip

program = [
    0x61, 0x0A,  # SET R1 = 10
    0x71, 0x01,  # ADD 1 TO R1
]

chip = Chip(1, False, 1)
chip.load_sprites_to_mem()
chip.load_program_to_mem(program)

for _ in range(len(program) // 2):
    chip.tick()

assert chip.registers[1].get() == 0x0B