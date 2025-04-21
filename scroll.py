import time
from charset import CHARSET

def scroll_text(controller, text="LAUNCHPAD!", color=127, speed=0.1):
    display = [0] * 8
    data = []

    for char in f"   {text}   ":
        glyph = CHARSET.get(char.upper(), ["        "] * 8)
        for row in glyph:
            bits = 0
            for i, c in enumerate(row[:8]):
                bits |= (1 << (7 - i)) if c != " " else 0
            data.append(bits)
        data.append(0)  # spacing

    for shift in range(len(data)):
        for row in range(8):
            display[row] = ((display[row] << 1) & 0xFF) | ((data[shift] >> (7 - row)) & 1)
        for row in range(8):
            for col in range(8):
                bit = (display[row] >> (7 - col)) & 1
                note = row * 16 + col
                controller.send_note(note, color if bit else 0)
        time.sleep(speed)
    controller.clear_grid()
