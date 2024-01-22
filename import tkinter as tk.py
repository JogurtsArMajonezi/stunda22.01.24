import tkinter as tk

def parse_input(expression):
    try:
        return eval(expression)
    except (SyntaxError, ZeroDivisionError):
        return None

def calculate():
    expression = calculator_entry.get()
    result = parse_input(expression)

    if result is not None:
        result_label.config(text=f"Result: {result}")
    else:
        result_label.config(text="Error: Invalid expression or division by zero", fg="red")

def clear_result():
    calculator_entry.delete(0, tk.END)
    result_label.config(text="Result: ")


root = tk.Tk()
root.title("Toms Graudums")


root.geometry("640x450")


clear_button = tk.Button(root, text="X", command=clear_result, fg="red")
clear_button.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=5) 

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

calculator_entry = tk.Entry(root)
calculator_entry.pack(side=tk.TOP, anchor=tk.CENTER, pady=5)  

calculate_button = tk.Button(root, text="Start", command=calculate)
calculate_button.pack(side=tk.TOP, anchor=tk.CENTER, pady=10)  


root.mainloop()
