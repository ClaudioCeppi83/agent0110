import sys
from PyQt6.QtWidgets import QApplication
from src.gui.main_window import MainWindow

def main():
    try:
        app = QApplication(sys.argv)
        main_window = MainWindow()
        main_window.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Error starting application: {e}")
        return 1  # Indicate an error occurred

if __name__ == "__main__":
    main()