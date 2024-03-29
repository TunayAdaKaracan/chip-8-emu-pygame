from board.cpu import Chip

program = [
    0xA0, 0xFB
]

chip = Chip(1, False, 1)
chip.load_sprites_to_mem()
chip.load_program_to_mem(program)

for _ in range(len(program) // 2):
    chip.tick()

assert chip.address.get() == 0xFB