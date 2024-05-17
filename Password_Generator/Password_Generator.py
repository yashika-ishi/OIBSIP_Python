import random
import string
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

# Function generate password
def generate_password():
    str = string.ascii_letters + string.digits 
    password="".join(random.choice(str) for i in range(var.get()))
    output.config(text= password, font=("Ubuntu",20), justify= "center")

# Function to copy
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output['text'])

# callback event
def my_callback(event):
    copy_btn.config(text='Shushhh!!')
# window  # Appling styling to GUI elements
root=tk.Tk()
style=Style(theme='superhero')
root.title("Password generator")
root.geometry("300x200")

# interger variable to hold number of characters
var = tk.IntVar()
var.set(8)

# Drop down menu
dropdown = ttk.Combobox(root, textvariable= var, values= [8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
dropdown.pack(pady= 5)

# Generate Button
generate_btn= ttk.Button(root, text="Generate Password", command= generate_password)
generate_btn.pack(pady=5)

# copy button
copy_btn = ttk.Button(root, text="Copy", command=copy_to_clipboard)
copy_btn.pack(pady=5)

copy_btn.bind('<Leave>', my_callback)
# output field
output = ttk.Label(root)
output.pack(pady=20)

root.mainloop()#.main loop................................