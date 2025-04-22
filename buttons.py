import threading
import time

def listen_buttons(controller):
    mode_buttons = {108: 'audio', 109: 'system', 110: 'scroll', 111: 'party', 104: 'wave', 105: 'sweep'}
    color_buttons = {106: -1, 107: 1}
    debounce_time = 0.2
    last_pressed = {}

    while controller.running:
        msg = controller.inport.poll()
        if msg and msg.type == 'control_change':
            ctrl, val = msg.control, msg.value
            now = time.time()

            if val > 0 and (ctrl not in last_pressed or now - last_pressed[ctrl] > debounce_time):
                last_pressed[ctrl] = now

                if ctrl in mode_buttons:
                    controller.current_effect = mode_buttons[ctrl]
                    threading.Thread(target=controller.run_loop, daemon=True).start()
                    print(f"Mode changed to {controller.current_effect}")

                elif ctrl in color_buttons:
                    colors = controller.color_profile.get('grid_colors', [15, 31, 47, 63, 79, 95, 111, 127])
                    current = controller.color_profile['grid']
                    idx = colors.index(current)
                    controller.color_profile['grid'] = colors[(idx + color_buttons[ctrl]) % len(colors)]
                    print(f"Color profile changed to {controller.color_profile['grid']}")

        time.sleep(0.01)
