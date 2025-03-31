import pytest
from effects.animations import wave_effect

def test_wave_effect_callable():
    assert callable(wave_effect)
