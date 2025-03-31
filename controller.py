import threading
import queue
import mido
import time
from lpfx.input.buttons import listen_buttons

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

        # ✅ Correct position here (INSIDE the __init__)
        threading.Thread(target=listen_buttons, args=(self,), daemon=True).start()

    def midi_sender(self):
        while self.running:
            try:
                msg = self.midi_queue.get(timeout=0.01)
                self.outport.send(msg)
            except queue.Empty:
                time.sleep(0.001)

    def clear_grid(self):
        for note in range(128):
            self.send_note(note, 0)

    def send_note(self, note, velocity):
        self.outport.send(mido.Message("note_on", note=note, velocity=velocity))

    def run_loop(self):
        print("Running main loop. Press Ctrl+C to stop.")
        try:
            while self.running:
                # Your loop logic here (simplified)
                time.sleep(0.5)
        except KeyboardInterrupt:
            self.running = False
            self.clear_grid()
            print("Stopped.")

