from board.cpu import Chip
import random

random.seed(1234)  # 0xE1 is the first rand

program = [
    0xC1, 0xFF # RAND
]

chip = Chip(1, False, 1)
chip.load_sprites_to_mem()
chip.load_program_to_mem(program)

for _ in range(len(program) // 2):
    chip.tick()

assert chip.registers[1].get() == 0xE1
