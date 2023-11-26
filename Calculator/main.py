import tkinter as tk

def calculate():
    a = float(a_entry.get())
    b = float(b_entry.get())
    if operation.get() == "+":
        result = a + b
    elif operation.get() == "-":
        result = a - b
    elif operation.get() == "*":
        result = a * b
    else:
        result = a / b

    if b == 0 and operation.get() == "/":
        result = "Деление на ноль!"

    result_label.config(text=f"Результат: {result}")

root = tk.Tk()
root.title("Калькулятор")

a_label = tk.Label(root, text="Введите первое число:")
a_label.pack()
a_entry = tk.Entry()
a_entry.pack()

b_label = tk.Label(root, text="Введите второе число:")
b_label.pack()
b_entry = tk.Entry()
b_entry.pack()

operation_label = tk.Label(root, text="Выберите операцию:")
operation_label.pack()
operation = tk.StringVar()
operation.set("+")
operation_entry = tk.Entry(state='readonly', textvariable=operation)
operation_entry.pack()

calculate_button = tk.Button(root, text="Рассчитать", command=calculate)
calculate_button.pack()

result_label = tk.Label(root, text="Результат:")
result_label.pack()

root.mainloop()
