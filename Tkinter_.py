import tkinter as tk
from PIL import Image,ImageTk
root = tk.Tk()
# label = tk.Label(root,text="Welcome to Tkinter!")
# label.pack()

# button = tk.Button(root, text="click me")
# button.pack()

# label1 = tk.Label(root, text = "Name:")
# label1.grid(row=0,column=0)

# entry1 = tk.Entry(root)

# entry1.grid(row=0,column=1)

# button = tk.Button(root, text="Click me")
# button.place(x = 100, y = 100)

img = tk.PhotoImage(file = "giphy.gif")
label = tk.Label(root,image=img)
label.pack()

# image = Image.open('panda.jpg')

# photo = ImageTk.PhotoImage(image)
# label = tk.Label(root,image=photo)
# label.pack()

root.mainloop()