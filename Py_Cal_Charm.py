from tkinter import*
import math


root = Tk()
root.title("PyCharm Calculator")
root.geometry("416x550+500+40")

calc = Frame(root, bd=20, pady=5, bg='gainsboro', relief = RIDGE)
calc.grid()

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""