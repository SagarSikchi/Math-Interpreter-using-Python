from tkinter import *
from tokens import Token
from lexer import Lexer
from _parser_ import Parser
from interpreter import Interpreter

# Create a Math_Interpreter class
class Math_Interpreter:

    def __init__(self, master):
        self.master = master
        master.title("MATH INTERPRETER")

        # Create a line where we display the equation
        self.equation = Entry(master, width=40, borderwidth=5)

        # Assign a position for the equation line in the grey application window
        self.equation.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Execute the .creteButton() method
        self.createButton()

    def createButton(self):
        # We first create each button one by one with the value we want
        # Using addButton() method
        b0 = self.addButton(0)
        b1 = self.addButton(1)
        b2 = self.addButton(2)
        b3 = self.addButton(3)
        b4 = self.addButton(4)
        b5 = self.addButton(5)
        b6 = self.addButton(6)
        b7 = self.addButton(7)
        b8 = self.addButton(8)
        b9 = self.addButton(9)
        b_add = self.addButton('+')
        b_sub = self.addButton('-')
        b_mult = self.addButton('*')
        b_div = self.addButton('/')
        b_modulo = self.addButton('%')
        b_exp = self.addButton('^')
        b_lp = self.addButton('(')
        b_rp = self.addButton(')')
        b_clear = self.addButton('CLEAR')
        b_value = self.addButton('VALUE')

        row1 = [b7, b8, b9]
        row2 = [b4, b5, b6]
        row3 = [b1, b2, b3]
        row4 = [b0, b_lp, b_rp]
        row5 = [b_add, b_sub, b_exp, b_clear]
        row6 = [b_mult, b_div, b_modulo, b_value]

        # Assign each button to a particular location on the GUI
        r = 1
        for row in [row1, row2, row3, row4, row5, row6]:
            c = 1
            for buttn in row:
                buttn.grid(row=r, column=c, columnspan=1)
                c += 1
            r += 1

    def addButton(self, value):
        text = ""
        return Button(self.master, text=value, width=10, command=lambda: self.clickButton(str(value), text))

    def clickButton(self, value, text):

        # Get the equation that's entered by the user
        current_equation = str(self.equation.get())
        text = current_equation

        # If user clicked "CLEAR", then clear the screen
        if value == 'CLEAR':
            text = ""
            self.equation.delete(-1, END)

        # If user clicked "VALUE", then compute the answer and display it
        elif value == 'VALUE':
            current_equation = text
            lexer = Lexer(current_equation)
            tokens = lexer.generate_tokens()

            parser = Parser(tokens)
            tree = parser.parse()

            if not tree:
                self.equation.insert(0, "Error")
            interpreter = Interpreter()
            answer = interpreter.visit(tree)
            self.equation.delete(-1, END)
            self.equation.insert(0, answer)

        # If user clicked any other button, then add it to the equation line
        else:
            self.equation.delete(0, END)
            self.equation.insert(-1, current_equation + value)

if __name__ == '__main__':

    # Create the main window of an application
    root = Tk()

    root.geometry("360x230")
    root.minsize(360, 230)

    # Tell our Math_Interprete class to use this window
    my_gui = Math_Interpreter(root)

    # Executable loop on the application, waits for user input
    root.mainloop()
