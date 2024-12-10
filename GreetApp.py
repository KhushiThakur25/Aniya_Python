import tkinter as tk

def greet():
    name = entry.get()
    if name:
        label.config(text=f"Hello, {name}!")
    else:
        label.config(text="Hello, world!")

root = tk.Tk()
root.title("Greet App")

label = tk.Label(root,text="Enter your name:",font=("Arial",14))
label.pack(pady=10)

entry = tk.Entry(root,font=("Arial",14))
entry.pack(pady=10)

button = tk.Button(root,text="Greet",font=("Arial",14),command=greet)
button.pack(pady=10)

label = tk.Label(root,text="",font=("Arial",14))
label.pack(pady=10)

root.mainloop()