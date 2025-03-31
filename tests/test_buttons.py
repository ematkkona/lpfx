import pytest
from lpfx.input.buttons import listen_buttons

def test_listen_buttons_callable():
    assert callable(listen_buttons)

