# Launchpad FX 🎛️

**Interactive, scriptable, audio-reactive Novation Launchpad (MK1) -FX Engine.**

## Features

- 🌊 **Smooth Animations** (waves, sweeps, sparkles)
- 🎵 **Audio FFT Visualizer**
- 📊 **Real-time System Load Metrics** (CPU, Memory, Network)
- 🎭 **Built-in Gimmicks** (Pac-Man, Ghost, Smiley)
- 📝 **FX Scripting Engine**
- 🎛️ **Live Interactive Shell**

## Quickstart

### Installation
```bash
git clone https://github.com/ematkkona/lpfx.git
cd lpfx
pip install mido numpy sounddevice psutil
```

### Running

#### Interactive shell:
```bash
python main.py --live
```
#### Run an FX script:
```bash
python main.py --script example.fx
```
### Testing
Run tests using pytest:

```bash
pip install pytest
pytest tests/
```

## License
MIT © 2025 Eetu Mäkinen
