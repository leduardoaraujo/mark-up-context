from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import sys
import os

class HTMLRenderer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Editor')
        self.setGeometry(100, 100, 1024, 768)
        self.setStyleSheet("""
            QMainWindow, QWidget {
                background-color: #1a1a1a;
                color: #f0f0f0;
            }
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)

        # Open app.html by default
        default_file = os.path.join(os.path.dirname(__file__), 'app.html')
        if os.path.exists(default_file):
            local_url = QUrl.fromLocalFile(default_file)
            self.web_view.setUrl(local_url)

def main():
    app = QApplication(sys.argv)
    window = HTMLRenderer()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
