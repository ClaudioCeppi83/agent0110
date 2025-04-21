import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QMenuBar,
    QMenu,
    QTabWidget,
    QTextEdit,
    QPushButton,
    QComboBox,
)
from PyQt6.QtCore import Qt
from src.gui.pyte_terminal import PyteTerminal
from src.core.ollama import OllamaClient


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Agente 0110")

        # Instantiate OllamaClient
        self.ollama_client = OllamaClient()

        #Window config
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()

        # Menu Bar
        menu_bar = QMenuBar(self)
        modelos_menu = QMenu("Modelos", self)
        modelos_menu.addAction("Seleccionar Modelo")
        menu_bar.addMenu(modelos_menu)
        mcps_menu = QMenu("MCPs", self)
        mcps_menu.addAction("Gestionar MCPs")
        menu_bar.addMenu(mcps_menu)
        configuracion_menu = QMenu("Configuración", self)
        configuracion_menu.addAction("Opciones")
        menu_bar.addMenu(configuracion_menu)
        self.setMenuBar(menu_bar)
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        self.model_selector = QComboBox()
        
        # Populate model_selector with models
        model_list = self.ollama_client.list_models()
        self.model_selector.addItems(model_list)
        main_layout.addWidget(self.model_selector)
        # Connect model_selector currentIndexChanged to on_model_changed
        self.model_selector.currentIndexChanged.connect(self.on_model_changed)


        

        self.terminal_tabs = QTabWidget()
        self.logs_terminal = PyteTerminal()
        self.output_terminal = PyteTerminal()
        self.terminal_tabs.addTab(self.logs_terminal, "Logs")
        self.terminal_tabs.addTab(self.output_terminal, "Output")
        main_layout.addWidget(self.terminal_tabs)

        self.prompt_input = QTextEdit()
        self.send_button = QPushButton("Send")
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.prompt_input)
        input_layout.addWidget(self.send_button)
        main_layout.addLayout(input_layout)
        # Connect send_button clicked signal to on_send_clicked
        self.send_button.clicked.connect(self.on_send_clicked)


    def on_model_changed(self, index):
        """Slot to handle model selection changes."""
        model_name = self.model_selector.currentText()
        print(f"Selected model changed to: {model_name}")


    def on_send_clicked(self):
        """Slot to handle send button clicks."""
        prompt_text = self.prompt_input.toPlainText()
        selected_model = self.model_selector.currentText()
        print(f"Prompt: {prompt_text}\nModel: {selected_model}")
        response = self.ollama_client.generate_response(prompt_text, selected_model)
        if response:
            self.output_terminal.write(response)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())