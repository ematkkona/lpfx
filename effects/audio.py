import numpy as np
import sounddevice as sd
import time
from lpfx.constants import COLOR_RAINBOW

def audio_effect(controller):
    def callback(indata, frames, time_info, status):
        if not controller.running or controller.current_effect != "audio":
            raise sd.CallbackStop()

        samples = indata[:, 0]
        fft = np.abs(np.fft.rfft(samples))
        bins = np.array_split(fft, 8)
        levels = [min(int(np.mean(b) * 10), 8) for b in bins]

        for col in range(8):
            for row in range(8):
                note = (7 - row) * 16 + col
                val = COLOR_RAINBOW[col % len(COLOR_RAINBOW)] if row < levels[col] else 0
                controller.send_note(note, val)

    with sd.InputStream(callback=callback):
        while controller.running and controller.current_effect == "audio":
            time.sleep(0.05)
    controller.clear_grid()
