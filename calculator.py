import tkinter as tk
import math

#  Functions  #

def update_display(value):
    current = display_var.get()

    if current == "0":
        display_var.set(value)
    else:
        display_var.set(current + value)

def clear_display():
    display_var.set("0")

def backspace():
    current = display_var.get()

    if len(current) > 1:
        display_var.set(current[:-1])
    else:
        display_var.set("0")

def square_root():
    try:
        result = math.sqrt(float(display_var.get()))
        display_var.set(str(result))
    except:
        display_var.set("Error")

def percentage():
    try:
        result = float(display_var.get()) / 100
        display_var.set(str(result))
    except:
        display_var.set("Error")

def calculate_result():
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
    except:
        display_var.set("Error")

# ---------------- Window ---------------- #

parent = tk.Tk()
parent.title("Calculator")
parent.geometry("420x650")
parent.configure(bg="#1E1E1E")
parent.resizable(False, False)

# ---------------- Title ---------------- #

title = tk.Label(
    parent,
    text="CALCULATOR",
    font=("Segoe UI", 18, "bold"),
    bg="#1E1E1E",
    fg="#00D4FF"
)

title.pack(pady=15)

# ---------------- Display ---------------- #

display_var = tk.StringVar()
display_var.set("0")

display = tk.Label(
    parent,
    textvariable=display_var,
    font=("Segoe UI", 28, "bold"),
    anchor="e",
    bg="#252526",
    fg="white",
    padx=20,
    pady=20,
    width=18
)

display.pack(pady=10)

# ---------------- Button Frame ---------------- #

frame = tk.Frame(parent, bg="#1E1E1E")
frame.pack()

buttons = [
    ["C", "⌫", "√", "%"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

for row in buttons:
    row_frame = tk.Frame(frame, bg="#1E1E1E")
    row_frame.pack()

    for btn in row:

        if btn == "C":
            command = clear_display
        elif btn == "⌫":
            command = backspace
        elif btn == "√":
            command = square_root
        elif btn == "%":
            command = percentage
        elif btn == "=":
            command = calculate_result
        else:
            command = lambda x=btn: update_display(x)

        button = tk.Button(
            row_frame,
            text=btn,
            command=command,
            font=("Segoe UI", 18, "bold"),
            bg="#3A3A3A",
            fg="white",
            activebackground="#00D4FF",
            activeforeground="black",
            relief="flat",
            width=5,
            height=2
        )

        button.pack(side=tk.LEFT, padx=5, pady=5)

# ---------------- Footer ---------------- #

footer = tk.Label(
    parent,
    text="Made by Sakina",
    font=("Segoe UI", 10),
    bg="#1E1E1E",
    fg="gray"
)

footer.pack(pady=15)

# ---------------- Run ---------------- #

parent.mainloop()