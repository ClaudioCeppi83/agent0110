from PyQt6.QtWidgets import QWidget, QTextEdit, QVBoxLayout
from pyte import Screen, Stream

class PyteTerminal(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.screen = Screen(80, 24)  # Adjust size as needed
        self.stream = Stream(self.screen)

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        self.text_edit.setFontFamily("monospace")  # Use a monospace font

        layout = QVBoxLayout(self)
        layout.addWidget(self.text_edit)
        self.setLayout(layout)
        self.update_display()
    
    def update_display(self):
        """Updates the QTextEdit with the content of the pyte.Screen."""
        self.text_edit.clear()
        for row in self.screen.display:        
            line = ""
            for cell in row:
                if isinstance(cell, str):
                    line += cell
                elif hasattr(cell, 'data') and isinstance(cell.data, str):
                    line += cell.data
                else:
                    line += str(cell)  # Fallback: convert to string
            self.text_edit.append(line)

    def send_input(self, text):
        """Sends input to the pyte.Stream."""
        self.stream.feed(text)
        self.update_display()
        
    def write(self, data): #testing method
        self.send_input(data)