# Launchpad FX 🎛️

**Interactive, scriptable, audio-reactive FX engine for Novation Launchpad (MK1, MK2, and others)**

## Features

- 🌊 **Text scroller**
- 🎵 **Audio FFT Visualizer**
- 📊 **Real-time System Load Metrics** (CPU, Memory, Network)
- 🎭 **Built-in Gimmicks** (Pac-Man, Ghost, Smiley)
- 🎛️ **Smooth animations, automatic & manual mode switching**
- 📝 **FX Scripting Engine with live console**
- ✅ **Multi-device support** (MK1/MK2/other MIDI devices) with auto-detect and profiles

## Quickstart

### Installation (Editable Mode for Development)
```bash
git clone https://github.com/ematkkona/lpfx.git
cd lpfx
pip install -e .
```

### Run the Interactive Shell
```bash
python lpfx/main.py --live
```

### Run an FX Script
```bash
python lpfx/main.py --script example.fx
```

### Select or List Devices
```bash
python lpfx/main.py --select-device
```

### Run Tests
```bash
pip install pytest
pytest tests/
```

For more on setting up Launchpad MK2 and device management, see [docs/devices.md](docs/devices.md).

## License
MIT © 2025 Eetu Mäkinen