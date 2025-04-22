from src.gui.pyte_terminal import PyteTerminal
from PyQt6.QtTest import QTest

def test_terminal_initialization(qtbot):
    """Test that terminal initializes correctly"""
    terminal = PyteTerminal()
    qtbot.addWidget(terminal)

    # Modificamos la aserción para esperar espacios en blanco
    assert terminal.text_edit.toPlainText().strip() == ""

def test_terminal_write_operations(qtbot):
    """Test writing and displaying text in terminal"""
    terminal = PyteTerminal()
    qtbot.addWidget(terminal)

    test_text = "Hello, terminal!"
    terminal.write(test_text)

    assert test_text in terminal.text_edit.toPlainText()

    # Test multiple writes
    terminal.write("\nSecond line")
    content = terminal.text_edit.toPlainText()
    assert "Hello, terminal!" in content
    assert "Second line" in content