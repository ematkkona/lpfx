import threading
import queue
import mido
import time
from lpfx.input.buttons import listen_buttons

class LaunchpadController:
    def __init__(self):
        self.device_name = "Launchpad MIDI 1"
        self.outport = None
        self.inport = None
        self.midi_queue = queue.Queue()
        self.running = True
        self.current_effect = "scroll"

        try:
            self.outport = mido.open_output(self.device_name)
            self.inport = mido.open_input(self.device_name)
        except IOError:
            print(f"⚠️ Could not open MIDI device '{self.device_name}'. Running in demo mode.")
            return  # Don't start threads

        threading.Thread(target=self.midi_sender, daemon=True).start()
        time.sleep(0.5)
        while self.inport.poll():
            self.inport.receive()
        threading.Thread(target=listen_buttons, args=(self,), daemon=True).start()

    @property
    def is_ready(self):
        return self.outport is not None and self.inport is not None

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
        if self.outport:
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

