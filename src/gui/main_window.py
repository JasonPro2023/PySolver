from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, 
    QHBoxLayout, QTextEdit, QLineEdit, 
    QPushButton, QLabel, QTabWidget
)
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pysolver - Resolución de Problemas Matemáticos")
        self.setGeometry(100, 100, 900, 700)
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Panel de entrada
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Ingresa tu problema matemático...")
        self.input_field.returnPressed.connect(self.solve_problem)
        
        self.solve_button = QPushButton("Resolver")
        self.solve_button.clicked.connect(self.solve_problem)
        
        input_layout.addWidget(QLabel("Problema:"))
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.solve_button)
        layout.addLayout(input_layout)
        
        # Pestañas para resultados
        self.tabs = QTabWidget()
        self.result_tab = QTextEdit()
        self.result_tab.setReadOnly(True)
        self.steps_tab = QTextEdit()
        self.steps_tab.setReadOnly(True)
        
        self.tabs.addTab(self.result_tab, "Resultado")
        self.tabs.addTab(self.steps_tab, "Procedimiento")
        layout.addWidget(self.tabs)
        
    def solve_problem(self):
        """Método que se llamará al resolver"""
        problem = self.input_field.text()
        if not problem:
            return
            
        # Por ahora solo mostraremos el texto
        self.result_tab.setText(f"Problema ingresado: {problem}\n\n(Próximamente: solución detallada)")
        self.steps_tab.setText("Los pasos de resolución aparecerán aquí...")