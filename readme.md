# Launchpad FX 🎛️

**Interactive, scriptable, audio-reactive FX engine for Novation Launchpad (MK1)**

## Features

- 🌊 **Text scroller**
- 🎵 **Audio FFT Visualizer**
- 📊 **Real-time System Load Metrics** (CPU, Memory, Network)
- 🎭 **Built-in Gimmicks** (Pac-Man, Ghost, Smiley)
- 🎛️ **Smooth animations, automatic & manual switching modes**
- 📝 **FX Scripting Engine with live console**
- 
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
