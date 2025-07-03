import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = length_var.get()
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digit_var.get()
    use_special = special_var.get()

    if length < 4:
        messagebox.showwarning("Too Short", "Password must be at least 4 characters.")
        return

    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("No Options", "Select at least one character set.")
        return

    # Ensure at least one character from each selected type
    password = []
    if use_upper: password.append(random.choice(string.ascii_uppercase))
    if use_lower: password.append(random.choice(string.ascii_lowercase))
    if use_digits: password.append(random.choice(string.digits))
    if use_special: password.append(random.choice(string.punctuation))

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
    password_str = ''.join(password)
    password_var.set(password_str)

# Function to copy to clipboard
def copy_to_clipboard():
    result = password_var.get()
    if result:
        root.clipboard_clear()
        root.clipboard_append(result)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Generate a password first.")

# GUI setup
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x400")
root.resizable(False, False)

tk.Label(root, text="Password Length:", font=("Arial", 12)).pack(pady=5)
length_var = tk.IntVar(value=12)
tk.Spinbox(root, from_=4, to=64, textvariable=length_var, font=("Arial", 12)).pack()

tk.Label(root, text="Include in Password:", font=("Arial", 12, "bold")).pack(pady=10)

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Uppercase Letters (A-Z)", variable=upper_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Lowercase Letters (a-z)", variable=lower_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Digits (0-9)", variable=digit_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Special Characters (!@#...)", variable=special_var).pack(anchor="w", padx=20)

tk.Button(root, text="Generate Password", command=generate_password, bg="#007ACC", fg="white", font=("Arial", 12)).pack(pady=15)

password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, font=("Arial", 12), width=30, justify="center").pack(pady=10)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack()

root.mainloop()