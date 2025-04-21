from PyQt6.QtWidgets import QWidget, QTextEdit, QVBoxLayout
from pyte import Screen, Stream
import logging


class PyteTerminal(QWidget):
    # Constants for screen size
    SCREEN_WIDTH = 80
    SCREEN_HEIGHT = 24

    # Initialize pyte.Screen and pyte.Stream to manage terminal state.
    def __init__(self, parent=None):
        super().__init__(parent)

        # pyte.Screen to represent the terminal screen.
        self.screen = Screen(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        # pyte.Stream to feed characters into the screen.
        self.stream = Stream(self.screen)


        # QTextEdit to display the terminal content.
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        self.text_edit.setFontFamily("monospace")  # Use a monospace font

        layout = QVBoxLayout(self)
        layout.addWidget(self.text_edit)
        self.setLayout(layout)
        self.update_display()

    def update_display(self):
        """Updates the QTextEdit with the content of the pyte.Screen.
        
        Iterates over the screen rows and cells, adding the content to the QTextEdit.
        """
        self.text_edit.clear()
        for row in self.screen.display:
            line = ""
            for cell in row:
                # Check if cell is a string.
                if isinstance(cell, str):
                    line += cell
                # Check if cell has a data attribute and it is a string.
                elif hasattr(cell, 'data') and isinstance(cell.data, str):
                    line += cell.data
                # Fallback: convert cell to string.
                else:
                    line += str(cell)
            self.text_edit.append(line)

        logging.info("Terminal display updated.")

    def send_input(self, text):
        """Sends input to the pyte.Stream.

        This method feeds text into the pyte.Stream, effectively simulating typing in the terminal.
        Then updates the display to reflect any changes.
        """
        logging.info(f"Sending input to terminal: {text!r}")
        self.stream.feed(text)
        self.update_display()

    def write(self, data):  # testing method
        self.send_input(data)