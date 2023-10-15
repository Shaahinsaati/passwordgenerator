import tkinter as tk
from tkinter import Label, Entry, Button, Checkbutton
import pyperclip
from main import password_generator
from tkinter import CENTER

def generate_password(event=None):
    length = int(length_entry.get())
    use_digits = use_digits_var.get()
    use_special_chars = use_special_chars_var.get()
    password = password_generator(length,has_digit=use_digits,has_specials=use_special_chars)
    password_label.config(text="Generated Password: " + password)
    generated_password.set(password)


def copy_password():
    passworde = generated_password.get()
    if passworde:
        pyperclip.copy(passworde)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Calculate window size and position for center of the screen
window_width = 600
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
root.resizable(0,0,)
# Create GUI components
Label(root, text="Password Length:", font=("Helvetica", 12)).place(x=30, y=30)
length_entry = Entry(root)
length_entry.place(x=200, y=30)
length_entry.insert(0, "8")
length_entry.bind("<Return>", generate_password)  # Bind the Enter key event

use_digits_var = tk.BooleanVar()
use_special_chars_var = tk.BooleanVar()

Checkbutton(root, text="Include Digits", variable=use_digits_var, font=("Helvetica", 10)).place(x=30, y=70)
Checkbutton(root, text="Include Special Characters", variable=use_special_chars_var, font=("Helvetica", 10)).place(x=30, y=100)

generate_button = Button(root, text="Generate Password", command=generate_password, bg="black", fg="yellow", font=("Helvetica", 12))
generate_button.place(x=30, y=140)

copy_button = Button(root, text="Copy Password", command=copy_password, bg="yellow", fg="black", font=("Helvetica", 12))
copy_button.place(x=200, y=140)

password_label = Label(root, text="", bg="lightgray", font=("Helvetica", 14))
password_label.place(x=30, y=180)

# Create a StringVar to store the generated password
generated_password = tk.StringVar()

# Start the GUI main loop
root.mainloop()
