import random
from charset import CHARSET

def render_sprite(controller, pattern, duration=1.5, color=127):
    import time
    start = time.time()
    while time.time() - start < duration and controller.running:
        for row in range(8):
            for col in range(8):
                pixel = (ord(pattern[row][col]) != ord(" "))
                note = row * 16 + col
                controller.send_note(note, color if pixel else 0)
        time.sleep(0.1)
    controller.clear_grid()

def show_random_gimmick(controller):
    pattern = random.choice([CHARSET["PACMAN"], CHARSET["GHOST"], CHARSET["SMILEY"]])
    render_sprite(controller, pattern)
