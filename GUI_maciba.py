import tkinter as tk
from math import *

def calculate():
    try:
        expression = calculator_entry.get()
        result = eval(expression)
        if "/" in expression and result == float('inf'):
            result_label.config(text="Error: Division by zero")
        else:
            result_label.config(text=f"Result: {result}")
    except Exception as e:
        result_label.config(text="Error")

def clear_result():
    calculator_entry.delete(0, tk.END)
    result_label.config(text="Result: ")


root = tk.Tk()
root.title("Mini Calculator GUI")


root.geometry("640x450")


clear_button = tk.Button(root, text="X", command=clear_result, fg="red")
clear_button.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=5)

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

calculator_entry = tk.Entry(root)
calculator_entry.pack(side=tk.TOP, anchor=tk.CENTER, pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(side=tk.TOP, anchor=tk.CENTER, pady=10)

root.mainloop()

