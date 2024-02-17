# Kutup's Super-Chip8 Emu
This project is an emulator for Chip 8 from 1970s. Quirks are matched to modern one. 
Special thanks to "Gulrak" and "Janitor Raus" -from [r/EmuDev Discord Server](https://discord.gg/PnFAUWUFKa)- for helping me out in this project and pointing out the mistakes i did.

Sources used while doing this project:
https://tobiasvl.github.io/blog/write-a-chip-8-emulator
https://github.com/mattmikolay/chip-8/wiki/CHIP%E2%80%908-Technical-Reference
https://github.com/mattmikolay/chip-8/wiki/CHIP%E2%80%908-Instruction-Set

For test roms check out: https://github.com/Timendus/chip8-test-suite

## Integration
The `Chip` class contains everything needed for emulator to work. The chip doesn't directly use any pygame functions which makes it usable on any kind of project, not even a display is needed. To integrate this Chip to your projects, copy `board` folder which contains all the stuff needed for emulator.

### Create Chip Instance
Create a new chip instance with
```py
chip = Chip()
```
Chip class takes 4 (1 kwarg) args.
```py
scale = 16 # This is just a variable stored in chip.screen for easier access later on

# Whatever if chip should pause itself after creation.
# Ticking while in paused state doesn't do anything
start_paused = False 

# Instruction count that will be executed per tick call. 60 fps = 10 * 60 = 600 Instructions per second
speed = 10

# To limit stack size for bad roms that might cause stackoverflow
stack_size = 32 

chip = Chip(scale, start_paused, speed, stack_size=stack_size)
```

### Load Font Sprites and ROM
Before execution load font sprites to memory and load a rom file from a directory (default to `./rom/`).
```py
chip.load_sprites_to_mem()
chip.load_rom("slipperyslope.ch8")
```

### Call Update Functions
We need to call some functions in order to chip to work properly.
These are: `Chip.tick`, `Chip.update_timers`, `Chip.keyboard.key_down`, `Chip.keyboard.key_up`
`Chip.update_timers` must be called once every frame at 60 FPS (60Hz) before `Chip.tick`
`Chip.tick` can be called at a custom rate
`Chip.keyboard.key_down` and `Chip.keyboard.key_up` needs to be managed by developer as it might change depending on what framework/library you are using

### Render Display
This will vary depending on your framework/library. I will give an example for pygame and official rendering function used in this project:

```py
def render_display(chip, screen: pygame.Surface):
    for i in range(chip.screen.cols * chip.screen.rows):
        x = (i % chip.screen.cols) * chip.screen.scale
        y = math.floor(i / chip.screen.cols) * chip.screen.scale

        if chip.screen.display[i]:
            pygame.draw.rect(screen, (0, 255, 0), (x, y, chip.screen.scale, chip.screen.scale))
```

### Keybindings
As this can also change depending on the framework/library you are using you might need to change your KEYBINDINGS in `VirtualKeyboard` class.

Keybindings are just a dict of Computer Key -> Chip-8 Key.
