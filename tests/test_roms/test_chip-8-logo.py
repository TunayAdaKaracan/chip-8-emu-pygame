import pygame
import math
from board.cpu import Chip

pygame.init()

w, h = 64, 32
scale = 16

SCREEN = pygame.display.set_mode((w * scale, h * scale))


def render_display(chip, screen: pygame.Surface):
    for i in range(chip.screen.cols * chip.screen.rows):
        x = (i % chip.screen.cols) * chip.screen.scale
        y = math.floor(i / chip.screen.cols) * chip.screen.scale

        if chip.screen.display[i]:
            pygame.draw.rect(screen, (0, 255, 0), (x, y, chip.screen.scale, chip.screen.scale))


# Emu loop
def main():
    chip = Chip(scale, False, 40, False)
    chip.load_sprites_to_mem()
    chip.load_rom("1-chip8-logo.ch8", "../../rom/tests/")
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        chip.update_timers()
        chip.tick()
        SCREEN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if chip.paused:
                        chip.resume()
                    else:
                        chip.pause()
                chip.keyboard.key_down(event.key)
            if event.type == pygame.KEYUP:
                chip.keyboard.key_up(event.key)
        render_display(chip, SCREEN)
        pygame.display.update()


if __name__ == "__main__":
    main()
