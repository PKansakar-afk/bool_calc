import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLCDNumber

from project.components.lexica import MyLexer
from project.components.parsers import ASTParser
from project.components.memory import Memory
from project.components.ui import Ui_MainWindow

class MainWindow(QMainWindow):
    true_btn: QPushButton
    false_btn: QPushButton
    and_btn: QPushButton
    or_btn: QPushButton
    eql_btn: QPushButton
    input_text: QLineEdit
    prefix_text: QLineEdit
    output_text: QLineEdit

    def __init__(self): # MainWindow Constructor
        super(MainWindow, self).__init__() # Call parent class constructor
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.true_btn.clicked.connect(lambda: self.append_text("t"))
        self.ui.false_btn.clicked.connect(lambda: self.append_text("f"))
        self.ui.and_btn.clicked.connect(lambda: self.append_text("∧"))
        self.ui.or_btn.clicked.connect(lambda: self.append_text("∨"))

        self.ui.eql_btn.clicked.connect(self.push_equal)

    def append_text(self, char: str):
        """Appends the clicked character to the input text box with a space."""
        current_text = self.ui.input_text.text()
        # visual spacing for users (t ∨ f instead of t∨f)
        if current_text == "":
            self.ui.input_text.setText(char)
        else:
            self.ui.input_text.setText(f"{current_text} {char}")

    def push_equal(self):
        print("Evaluating Boolean Logic...")
        lexer = MyLexer()
        parser = ASTParser()
        memory = Memory()

        input_text = self.ui.input_text.text()
        
        # Guard clause: Do nothing if the input is empty
        if not input_text.strip():
            print("Input is empty.")
            return

        try:
            # The parser returns a tuple: (bool_result, prefix_string)
            bool_result, prefix_string = parser.parse(lexer.tokenize(input_text))
            
            # Set text to 't' or 'f'
            self.ui.output_text.setText("t" if bool_result else "f")

            # Update the Prefix Notation Text Box
            self.ui.prefix_text.setText(prefix_string)
            
            # Print the outputs
            print(f"Input: {input_text}")
            print(f"Evaluated Truth Value: {'t' if bool_result else 'f'}")
            print(f"Prefix Notation: {prefix_string}")
            print("-" * 20)

            # Print Memory state to console
            print("\n--- Current Memory State ---")
            print(memory)
            
        except AssertionError as e:
            print(f"Memory Error: {e}")
        except Exception as e:
            print(f"Evaluation Error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())