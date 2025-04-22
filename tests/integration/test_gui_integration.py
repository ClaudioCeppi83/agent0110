from PyQt6.QtCore import Qt
from unittest.mock import MagicMock
import pytest

from src.gui.main_window import MainWindow
from src.core.ollama import OllamaClient

def test_main_window_integration(qtbot, mocker):
    """Test MainWindow integrates with OllamaClient"""
    # Mock OllamaClient methods
    mocker.patch.object(OllamaClient, 'list_models', return_value=['llama2'])
    mocker.patch.object(OllamaClient, 'generate_response', return_value="Mocked response")

    window = MainWindow()
    qtbot.addWidget(window)

    # Verify model list is populated
    assert window.model_selector.count() > 0
    assert window.model_selector.itemText(0) == 'llama2'

    # Test send button
    window.prompt_input.setPlainText("test prompt")
    qtbot.mouseClick(window.send_button, Qt.MouseButton.LeftButton)

    assert "Mocked response" in window.output_terminal.text_edit.toPlainText()