import time
import math
from random import choice
from lpfx.constants import COLOR_RAINBOW

def wave_effect(controller, direction="horizontal", speed=0.1, duration=5):
    start = time.time()
    while time.time() - start < duration and controller.running:
        for phase in range(8):
            for row in range(8):
                for col in range(8):
                    if direction == "horizontal":
                        val = int(4.5 + 3.5 * math.sin((col + phase) * math.pi / 4))
                        lit = (7 - row) == val
                    else:
                        val = int(4.5 + 3.5 * math.sin((row + phase) * math.pi / 4))
                        lit = (7 - col) == val
                    note = row * 16 + col
                    controller.send_note(note, choice(COLOR_RAINBOW) if lit else 0)
            time.sleep(speed)
    controller.clear_grid()

def sweep_effect(controller, direction="left", speed=0.05, duration=5):
    steps = 8
    if direction == "left":
        cols = range(8)
    elif direction == "right":
        cols = reversed(range(8))
    elif direction == "up":
        rows = reversed(range(8))
    else:
        rows = range(8)

    start = time.time()
    while time.time() - start < duration and controller.running:
        for step in range(steps):
            for row in range(8):
                for col in range(8):
                    note = row * 16 + col
                    if direction in ["left", "right"]:
                        lit = col == step
                    else:
                        lit = row == step
                    controller.send_note(note, choice(COLOR_RAINBOW) if lit else 0)
            time.sleep(speed)
    controller.clear_grid()
