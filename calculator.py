import tkinter as tk
from tkinter import ttk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")

        self.result = 0
        self.operation = ""

        self.x=10
        self.y=5
        self.ix=5
        self.iy=5
        self.height=1
        self.width=3
        self.font=("Arial", 20)
        
        self.output = ttk.Label(self, text="0", font=self.font)
        self.output.grid(row=0, column=0, columnspan=4, padx=self.x, pady=self.y, ipadx=self.ix, ipady=self.iy)

        self.entry = ttk.Entry(self, justify="right", font=self.font)
        self.entry.grid(row=1, column=0, columnspan=4, padx=5, pady=5, ipadx=20, ipady=20)

        self.clear_button = tk.Button(self, text="C",height=self.height, width=self.width,font=self.font, command = self.clear)
        self.clear_button.grid(row=2, column=2,padx=self.x, pady=self.y, ipadx=self.ix, ipady=self.iy)

        self.add_button = tk.Button(self, text="+",height=self.height, width=self.width,font=self.font, command = lambda: self.set_operator("+"))
        self.add_button.grid(row=3, column=3, padx=self.x, pady=self.y, ipadx=self.ix, ipady=self.iy)
        
        self.sub_button = tk.Button(self, text="-",height=self.height, width=self.width,font=self.font, command =lambda: self.set_operator("-"))
        self.sub_button.grid(row=4, column=3, padx=self.x, pady=self.y, ipadx=self.ix, ipady=self.iy)
        
        self.multi_button = tk.Button(self, text="X",height=self.height, width=self.width,font=self.font, command = lambda: self.set_operator("*"))
        self.multi_button.grid(row=5, column=3, padx=self.x, pady=self.y, ipadx=self.ix, ipady=self.iy)

        self.div_button = tk.Button(self, text="/",height=self.height, width=self.width,font=self.font, command = lambda: self.set_operator("/"))
        self.div_button.grid(row=6, column=3, padx=self.x, pady=self.y, ipadx=self.ix, ipady=self.iy)

        self.neg_button = tk.Button(self, text="+/-",height=self.height, width=self.width,font=self.font, command = lambda: self.set_operator("+/-"))
        self.neg_button.grid(row=6, column=2, padx=self.x, pady=self.y, ipadx=self.ix, ipady=self.iy)

        self.sum_button = tk.Button(self, text="=",height=self.height, width=self.width,font=self.font, command=self.operator)
        self.sum_button.grid(row=2, column=3, padx=self.x, pady=self.y, ipadx=self.ix, ipady=self.iy)

        self.create_number_buttons()
    def create_number_buttons(self):
        numbers = [[7, 8, 9],[4, 5, 6],[1, 2, 3],['.', 0],]
        for i, row in enumerate(numbers):
            for j, number in enumerate(row):
                button = tk.Button(self, text=number,height=self.height, width=self.width,font=self.font, command=lambda n=number: self.insert_from_buttons(n))
                button.grid(row=i+3, column=j, padx=self.x, pady=self.y, ipadx=self.ix, ipady=self.iy)

    def insert_from_buttons(self, number):
        self.insert_number = str(self.entry.get()) + str(number)
        self.entry.delete(0, "end")
        self.entry.insert(0, self.insert_number)


    def operator(self):
        self.old_result = self.result
        self.number = float(self.entry.get())

        if self.operation == "+":
            self.result += self.number
            
        elif self.operation == "-":
            self.result -= self.number

        elif self.operation == "*":
            self.result *= self.number

        elif self.operation == "/":
            self.result /= self.number
        
        self.output.config(text=f"{self.old_result} {self.operation} {self.number} = {self.result}")
        self.operation = ""
        self.entry.delete(0, "end")
        self.entry.insert(0, str(self.result))

    def set_operator(self, operation):
        if self.operation != "" or self.operation == "+/-":
            self.operator()

        if operation == "+/-":
            self.number = -float(self.entry.get())
            self.entry.delete(0, "end")
            self.entry.insert(0, str(self.number))

        else:
            self.operation= operation
            self.number = self.entry.get()
            self.result = float(self.number)
            self.output.config(text=f"Result:  {self.number} {operation}")
            self.entry.delete(0, "end")

    def clear(self):
        self.entry.delete(0, "end")
        self.operation = ""
        self.result = 0
        self.output.config(text=f"Result: {self.result}")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
