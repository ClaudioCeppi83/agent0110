import pytest
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtTest import QTest
from src.main import main
from src.core.ollama import OllamaClient

@pytest.mark.skipif(True, reason="Requires manual execution with Ollama running")
def test_complete_workflow(qtbot, qapp, mocker):
    """End-to-end test of the complete application workflow"""
    # Mock Ollama responses
    mocker.patch.object(OllamaClient, 'list_models', return_value=['llama2'])
    mocker.patch.object(
        OllamaClient,
        'generate_response',
        return_value="Mocked response from LLM"
    )

    # Start application
    window = main()  # Necesitarás modificar main() para devolver la ventana

    # Test model loading
    assert window.model_selector.count() == 1

    # Enter prompt and send
    QTest.keyClicks(window.prompt_input, "Hello, how are you?")
    QTest.mouseClick(window.send_button, Qt.MouseButton.LeftButton)

    # Verify response
    assert "Mocked response from LLM" in window.output_terminal.text_edit.toPlainText()