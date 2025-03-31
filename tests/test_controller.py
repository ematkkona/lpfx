import pytest
from controller import LaunchpadController

def test_controller_initialization():
    controller = LaunchpadController()
    assert controller.running is True
