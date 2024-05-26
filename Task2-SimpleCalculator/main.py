# Design a simple calculator with basic arithmetic operations.
# Prompt the user to input two numbers and an operation choice.
# Perform the calculation and display the result.

import tkinter as tk

def add():
    result.set(float(num1.get()) + float(num2.get()))

def subtract():
    result.set(float(num1.get()) - float(num2.get()))

def multiply():
    result.set(float(num1.get()) * float(num2.get()))

def divide():
    try:
        result.set(float(num1.get()) / float(num2.get()))
    except ZeroDivisionError:
        result.set("Error! Division by zero.")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create input fields
num1_label = tk.Label(window, text="Enter first number:")
num1_label.grid(row=0, column=0)
num1 = tk.Entry(window)
num1.grid(row=0, column=1)

num2_label = tk.Label(window, text="Enter second number:")
num2_label.grid(row=1, column=0)
num2 = tk.Entry(window)
num2.grid(row=1, column=1)

# Create buttons for arithmetic operations
add_button = tk.Button(window, text="+", command=add)
add_button.grid(row=2, column=0)

subtract_button = tk.Button(window, text="-", command=subtract)
subtract_button.grid(row=2, column=1)

multiply_button = tk.Button(window, text="*", command=multiply)
multiply_button.grid(row=3, column=0)

divide_button = tk.Button(window, text="/", command=divide)
divide_button.grid(row=3, column=1)

# Create a label to display the result
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result)
result_label.grid(row=4, columnspan=2)

# Run the main event loop
window.mainloop()
