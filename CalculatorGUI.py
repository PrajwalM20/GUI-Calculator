import tkinter as tk

def click(event):
    button_text = event.widget["text"]
    if button_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")

# Entry field
entry = tk.Entry(window, font=("Arial", 20), borderwidth=5, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, padx=10, pady=10, ipady=10)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', 'C', '+'],
    ['=']
]

for row in buttons:
    frame = tk.Frame(window)
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font=("Arial", 18), relief=tk.GROOVE)
        btn.pack(side="left", expand=True, fill="both")
        btn.bind("<Button-1>", click)

# Run the application
window.mainloop()
