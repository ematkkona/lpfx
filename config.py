import json
from pathlib import Path

CONFIG_FILE = Path.home() / ".lpfx_config.json"

def load_config():
    if CONFIG_FILE.exists():
        try:
            return json.loads(CONFIG_FILE.read_text())
        except:
            return {}
    return {}

def save_config(config):
    CONFIG_FILE.write_text(json.dumps(config, indent=2))
