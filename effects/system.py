import psutil
import time
from lpfx.constants import COLOR_CPU, COLOR_MEM, COLOR_NET

def system_effect(controller):
    while controller.running and controller.current_effect == "system":
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        net = psutil.net_io_counters().bytes_recv % (1024 * 1024) / (1024 * 1024) * 100

        def draw(col_base, value, color):
            height = int((value / 100) * 8)
            for row in range(8):
                for c in range(2):
                    note = (7 - row) * 16 + (col_base + c)
                    controller.send_note(note, color if row < height else 0)

        draw(0, cpu, COLOR_CPU)
        draw(3, mem, COLOR_MEM)
        draw(6, net, COLOR_NET)
        time.sleep(0.25)
    controller.clear_grid()
