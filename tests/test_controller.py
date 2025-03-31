import pytest
from unittest.mock import patch, MagicMock
from lpfx.controller import LaunchpadController

@patch('lpfx.controller.mido.open_output')
@patch('lpfx.controller.mido.open_input')
def test_controller_initialization(mock_input, mock_output):
    mock_output.return_value = MagicMock()
    mock_input.return_value = MagicMock(poll=lambda: None)

    controller = LaunchpadController()
    assert controller.running is True
    mock_output.assert_called_once_with("Launchpad MIDI 1")
    mock_input.assert_called_once_with("Launchpad MIDI 1")
