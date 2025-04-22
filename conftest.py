import pytest
from PyQt6.QtWidgets import QApplication

# Fixture para la aplicación Qt (necesaria para pruebas GUI)
@pytest.fixture(scope="session")
def qapp():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    yield app