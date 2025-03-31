import mido
import time
import queue
import threading
from charset import CHARSET
from effects.gimmicks import show_random_gimmick
from effects.animations import wave_effect, sweep_effect

class LaunchpadController:
    def __init__(self):
        self.device_name = "Launchpad MIDI 1"
        self.outport = mido.open_output(self.device_name)
        self.inport = mido.open_input(self.device_name)
        self.midi_queue = queue.Queue()
        self.running = True
        self.current_effect = "scroll"
        threading.Thread(target=self.midi_sender, daemon=True).start()
        time.sleep(0.5)
        timeout = time.time() + 1
        while time.time() < timeout and self.inport.poll():
            self.inport.receive()
        threading.Thread(target=self.listen_buttons, daemon=True).start()

    def send_note(self, note, velocity):
        self.outport.send(mido.Message("note_on", note=note, velocity=velocity))

    def midi_sender(self):
        while self.running:
            effect = self.current_effect or "gimmick"
            if effect == "gimmick":
                show_random_gimmick(self)
            elif effect == "wave":
                wave_effect(self, direction="horizontal")
            elif effect == "sweep":
                sweep_effect(self, direction="left")
            else:
                show_random_gimmick(self)

            try:
                msg = self.midi_queue.get(timeout=0.01)
                self.outport.send(msg)
            except queue.Empty:
                time.sleep(0.001)

    def clear_grid(self):
        for note in range(128):
            self.send_note(note, 0)

    from input.buttons import listen_buttons
    threading.Thread(target=listen_buttons, args=(self,), daemon=True).start()  # to be implemented in input/buttons.py

    def run_loop(self):
        print("Running main loop. Press Ctrl+C to stop.")
        try:
            while self.running:
            effect = self.current_effect or "gimmick"
            if effect == "gimmick":
                show_random_gimmick(self)
            elif effect == "wave":
                wave_effect(self, direction="horizontal")
            elif effect == "sweep":
                sweep_effect(self, direction="left")
            else:
                show_random_gimmick(self)

                show_random_gimmick(self)
                time.sleep(3)
        except KeyboardInterrupt:
            self.running = False
            self.clear_grid()
            print("Stopped.")
