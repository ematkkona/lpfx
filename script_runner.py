import time
import random
from effects.animations import wave_effect, sweep_effect
from effects.scroll import scroll_text
from effects.gimmicks import show_random_gimmick
from effects.audio import audio_effect
from effects.system import system_effect

class ScriptRunner:
    def __init__(self, controller):
        self.controller = controller

    def fx(self, name, **kwargs):
        effects = {
            "wave": wave_effect,
            "sweep": sweep_effect,
            "scroll": scroll_text,
            "gimmick": lambda c, type=None: show_random_gimmick(c),
            "audio": audio_effect,
            "system": system_effect,
        }
        effect_func = effects.get(name)
        if effect_func:
            effect_func(self.controller, **kwargs)
        else:
            print(f"Effect '{name}' not found.")

    def wait(self, seconds):
        time.sleep(seconds)

    def loop(self, count, sequence):
        for _ in range(count):
            self.run_script(sequence)

    def run_script(self, script_lines):
        for line in script_lines:
            line = line.strip()
            if line.startswith("fx"):
                exec(f"self.{line}")
            elif line.startswith("wait"):
                exec(f"self.{line}")
            elif line.startswith("loop"):
                parts = line.split(":", 1)
                count = int(parts[0].split("(")[1].split(")")[0])
                nested_script = parts[1].strip().split(";")
                self.loop(count, nested_script)

    def load_and_run(self, filepath):
        with open(filepath, "r") as script_file:
            lines = [line.strip() for line in script_file if line.strip() and not line.strip().startswith("#")]
        self.run_script(lines)
