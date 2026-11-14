import tkinter as tk
from tkinter import messagebox


def calculate_bmi():
    weight_text = weight_entry.get().strip()
    height_text = height_entry.get().strip()

    if not weight_text or not height_text:
        messagebox.showerror(
            "Missing Input",
            "Please enter both weight and height."
        )
        return

    try:
        weight = float(weight_text)
        height_cm = float(height_text)

        if weight <= 0 or height_cm <= 0:
            messagebox.showerror(
                "Invalid Input",
                "Weight and height must be greater than zero."
            )
            return

        if not (weight < float("inf") and height_cm < float("inf")):
            raise ValueError

        height_m = height_cm / 100
        bmi = weight / (height_m * height_m)

        if bmi < 18.5:
            category = "Underweight"
            category_color = "#D97706"
        elif bmi < 25:
            category = "Normal Weight"
            category_color = "#16A34A"
        elif bmi < 30:
            category = "Overweight"
            category_color = "#EA8A24"
        else:
            category = "Obesity"
            category_color = "#DC4444"

        result_label.config(text=f"BMI: {bmi:.2f}")
        category_label.config(
            text=f"Category: {category}",
            fg=category_color
        )

    except (ValueError, OverflowError):
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numeric values."
        )


def reset_calculator():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="BMI: --")
    category_label.config(text="Category: --", fg="#52657D")
    weight_entry.focus_set()


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("460x510")
root.resizable(False, False)
root.configure(bg="#F1F6FC")

tk.Label(
    root,
    text="BMI Calculator",
    font=("Helvetica Neue", 25, "bold"),
    bg="#F1F6FC",
    fg="#183153"
).pack(pady=(28, 8))

tk.Label(
    root,
    text="Calculate your Body Mass Index",
    font=("Helvetica Neue", 12),
    bg="#F1F6FC",
    fg="#657B95"
).pack(pady=(0, 22))

tk.Label(
    root,
    text="Weight (kg)",
    font=("Helvetica Neue", 12, "bold"),
    bg="#F1F6FC",
    fg="#183153"
).pack(pady=5)

weight_entry = tk.Entry(
    root,
    font=("Helvetica Neue", 14),
    width=25,
    justify="center",
    bg="white",
    fg="#183153",
    relief="flat",
    highlightthickness=1,
    highlightbackground="#CAD8E8"
)
weight_entry.pack(pady=8, ipady=8)

tk.Label(
    root,
    text="Height (cm)",
    font=("Helvetica Neue", 12, "bold"),
    bg="#F1F6FC",
    fg="#183153"
).pack(pady=5)

height_entry = tk.Entry(
    root,
    font=("Helvetica Neue", 14),
    width=25,
    justify="center",
    bg="white",
    fg="#183153",
    relief="flat",
    highlightthickness=1,
    highlightbackground="#CAD8E8"
)
height_entry.pack(pady=8, ipady=8)

button_frame = tk.Frame(root, bg="#F1F6FC")
button_frame.pack(pady=20)

tk.Button(
    button_frame,
    text="Calculate BMI",
    command=calculate_bmi,
    font=("Helvetica Neue", 11, "bold"),
    bg="#CFE3FA",
    fg="#183153",
    activebackground="#B8D3F0",
    relief="flat",
    cursor="hand2",
    width=15,
    pady=10
).pack(side="left", padx=6)

tk.Button(
    button_frame,
    text="Reset",
    command=reset_calculator,
    font=("Helvetica Neue", 11, "bold"),
    bg="#DFE7F0",
    fg="#183153",
    activebackground="#CAD8E8",
    relief="flat",
    cursor="hand2",
    width=10,
    pady=10
).pack(side="left", padx=6)

result_label = tk.Label(
    root,
    text="BMI: --",
    font=("Helvetica Neue", 23, "bold"),
    bg="#F1F6FC",
    fg="#183153"
)
result_label.pack(pady=(12, 5))

category_label = tk.Label(
    root,
    text="Category: --",
    font=("Helvetica Neue", 14, "bold"),
    bg="#F1F6FC",
    fg="#52657D"
)
category_label.pack(pady=5)

tk.Label(
    root,
    text="BMI is a screening measure, not a medical diagnosis.",
    font=("Helvetica Neue", 9),
    bg="#F1F6FC",
    fg="#657B95",
    wraplength=410
).pack(side="bottom", pady=18)

weight_entry.focus_set()
root.mainloop()
