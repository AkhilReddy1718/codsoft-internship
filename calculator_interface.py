import tkinter as tk
def button_click(symbol):
    current = display_var.get()
    if current == 'Error':
        current = ''
    if symbol == 'C':
        current = ''
    elif symbol == '=':
        try:
            current = str(eval(current))
        except:
            current = 'Error'
    elif symbol == '←':  
        current = current[:-1]
    else:
        current += symbol
    display_var.set(current)
root = tk.Tk()
root.title("Calculator")
display_var = tk.StringVar()
display_entry = tk.Entry(root, textvariable=display_var, justify='right', font=('Arial', 20))
display_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='ew')
buttons = [
    'C', '%', '←', '/',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '00', '0', '.', '='
]
row = 1
col = 0
for button in buttons:
    tk.Button(root, text=button, padx=20, pady=10, font=('Arial', 14), command=lambda b=button: button_click(b)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1
root.mainloop()
