# example.fx – Sample FX Script for Launchpad FX 🎛️

fx("scroll", text="HELLO WORLD", color=95, speed=0.15)
wait(1)

loop(2): fx("wave", direction="horizontal", duration=3); fx("sweep", direction="right", duration=3)

fx("gimmick")
wait(1)

fx("system")
wait(5)

fx("audio")
wait(5)
