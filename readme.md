
# Launchpad FX

![Launchpad FX Logo](launchpad_fx_logo_transparent.png)

Launchpad FX is an interactive, scriptable, audio-reactive FX engine built for the Novation Launchpad (MK1). It features dynamic LED animations, real-time audio visualization, and system metrics display—bringing your Launchpad to life!

## Key Features

- ✅ **FX Scripting Engine:** Easily create and run custom `.fx` scripts.
- ✅ **Interactive Console:** Live scripting with autocomplete and FX script execution.
- ✅ **Audio-Reactive Visualizations:** Stunning FFT-based audio effects.
- ✅ **System Monitoring:** Real-time CPU, memory, and network visualizations.
- ✅ **Built-in FX:** Wave, Sweep, Scroll text, and fun gimmicks like Pac-Man, Ghost, and Smiley.
- ✅ **Graceful Fallback:** Robust error handling if MIDI hardware isn't connected.

## Installation

Install via pip:
```bash
pip install lpfx
```

Or clone from GitHub:
```bash
git clone https://github.com/ematkkona/lpfx.git
cd lpfx
pip install -e .
```

## Quickstart

Run the interactive shell:
```bash
lpfx --live
```

Run a provided FX script:
```bash
lpfx --script example.fx
```

List available scripts:
```bash
lpfx --list
```

## Included Demo Scripts

- `example.fx` – Demonstrates basic scrolling, wave, sweep, gimmick, audio, and system effects.
- `party.fx` – A fun, looping sequence of animations and gimmicks.
- `metrics.fx` – Displays real-time system metrics visually.

## Writing Your Own FX Scripts

FX scripts are simple to create:

```python
fx("scroll", text="HELLO WORLD", color=95, speed=0.15)
wait(1)

loop(2):
  fx("wave", direction="horizontal", duration=3)
  fx("sweep", direction="right", duration=3)

fx("audio")
wait(5)
```

## Contributing

Contributions welcome! Please open an issue or pull request on GitHub.

## License

MIT © 2025 Eetu Mäkinen
