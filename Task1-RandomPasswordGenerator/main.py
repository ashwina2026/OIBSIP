
import tkinter as tk
from tkinter import messagebox
import random
import string


# Generate password
def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4 or length > 64:
            messagebox.showerror(
                "Invalid Length",
                "Please select a length between 4 and 64."
            )
            return

        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        numbers = string.digits
        special = string.punctuation

        all_characters = uppercase + lowercase + numbers + special

        password_list = [
            random.choice(uppercase),
            random.choice(lowercase),
            random.choice(numbers),
            random.choice(special)
        ]

        for _ in range(length - 4):
            password_list.append(random.choice(all_characters))

        random.shuffle(password_list)

        password = "".join(password_list)

        password_entry.config(state="normal")
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state="readonly")

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid number."
        )


# Copy password
def copy_password():
    password = password_entry.get()

    if not password:
        messagebox.showwarning(
            "No Password",
            "Generate a password first."
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

    messagebox.showinfo(
        "Success",
        "Password copied successfully!"
    )


# Main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("460x410")
root.resizable(False, False)
root.configure(bg="#F4F0FF")

# Fonts
heading_font = ("Helvetica Neue", 23, "bold")
normal_font = ("Helvetica Neue", 12)
button_font = ("Helvetica Neue", 12, "bold")

# Heading
heading = tk.Label(
    root,
    text="Password Generator",
    font=heading_font,
    bg="#F4F0FF",
    fg="#493477"
)
heading.pack(pady=(25, 5))

subtitle = tk.Label(
    root,
    text="Create a random password in seconds",
    font=normal_font,
    bg="#F4F0FF",
    fg="#666666"
)
subtitle.pack(pady=(0, 25))

# Length label
length_label = tk.Label(
    root,
    text="Password Length (4–64)",
    font=("Helvetica Neue", 12, "bold"),
    bg="#F4F0FF",
    fg="#493477"
)
length_label.pack(pady=5)

# Length selector
length_entry = tk.Spinbox(
    root,
    from_=4,
    to=64,
    width=10,
    font=("Helvetica Neue", 13),
    justify="center",
    bg="white",
    fg="#493477",
    buttonbackground="#DCD1F5",
    relief="flat",
    bd=0,
    highlightthickness=1,
    highlightbackground="#C8B8EB",
    highlightcolor="#7053B5"
)
length_entry.delete(0, tk.END)
length_entry.insert(0, "12")
length_entry.pack(pady=10, ipady=5)

# Password display
password_entry = tk.Entry(
    root,
    width=35,
    font=("Helvetica Neue", 13),
    justify="center",
    state="readonly",
    readonlybackground="white",
    fg="#493477",
    disabledforeground="#493477",
    relief="flat",
    bd=0,
    highlightthickness=1,
    highlightbackground="#C8B8EB",
    highlightcolor="#7053B5"
)
password_entry.pack(pady=20, ipady=10)

# Generate button
generate_button = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    font=button_font,
    bg="#DCD1F5",
    fg="#493477",
    activebackground="#C8B8EB",
    activeforeground="#493477",
    relief="flat",
    bd=0,
    highlightthickness=0,
    cursor="hand2",
    width=23,
    pady=10
)
generate_button.pack(pady=7)

# Copy button
copy_button = tk.Button(
    root,
    text="Copy Password",
    command=copy_password,
    font=button_font,
    bg="#7053B5",
    fg="#493477",
    activebackground="#594092",
    activeforeground="#493477",
    relief="flat",
    bd=0,
    highlightthickness=0,
    cursor="hand2",
    width=23,
    pady=10
)
copy_button.pack(pady=7)

# Footer
footer = tk.Label(
    root,
    text="Made with Python and Tkinter",
    font=("Helvetica Neue", 9),
    bg="#F4F0FF",
    fg="#888888"
)
footer.pack(side="bottom", pady=12)

# Run application
root.mainloop()

