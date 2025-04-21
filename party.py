import time
import random
from effects.gimmicks import show_random_gimmick
from effects.animations import wave_effect, sweep_effect
from effects.audio import audio_effect
from effects.system import system_effect
from effects.scroll import scroll_text

def party_mode(controller, duration=30):
    effects = [
        lambda c: scroll_text(c, "PARTY MODE!", color=random.randint(30, 127)),
        lambda c: wave_effect(c, direction=random.choice(["horizontal", "vertical"]), duration=5),
        lambda c: sweep_effect(c, direction=random.choice(["left", "right", "up", "down"]), duration=5),
        show_random_gimmick,
        audio_effect,
        system_effect,
    ]
    start = time.time()
    while time.time() - start < duration and controller.running:
        effect = random.choice(effects)
        controller.current_effect = "party"
        try:
            effect(controller)
        except Exception as e:
            print(f"Party mode error: {e}")
        time.sleep(0.5)
    controller.clear_grid()
