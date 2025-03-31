# party.fx – Random fun FX loop

loop(5):
  fx("scroll", text="PARTY TIME!", color=63, speed=0.1)
  fx("wave", direction="vertical", duration=2)
  fx("sweep", direction="left", duration=2)
  fx("gimmick")
  fx("audio")
  wait(1)
