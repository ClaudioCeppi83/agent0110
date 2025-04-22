from unittest.mock import patch  # Añadir esta importación
import pytest
from PyQt6.QtCore import QTimer, Qt  # Corregir importación de QtCore

# Eliminar importaciones no utilizadas (subprocess, time)

@pytest.mark.skip(reason="Requires actual Ollama installation")
def test_full_app_flow(qtbot, qapp):
    """End-to-end test of the application flow"""
    from src.main import main

    # Start the application
    timer = QTimer()
    timer.setSingleShot(True)
    timer.timeout.connect(qapp.quit)
    timer.start(5000)  # Auto-close after 5 seconds

    with patch('sys.exit'):
        main()

    # Verify application starts without errors
    # (This would be expanded with actual UI interaction tests)