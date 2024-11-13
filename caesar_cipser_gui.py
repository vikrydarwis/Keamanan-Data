import tkinter as tk
from tkinter import ttk, messagebox
from caesar_cipher_logic import enkripsi, dekripsi  # Import logika dari file caesar_cipher_logic.py

def process_text():
    try:
        shift = int(shift_value.get())
        text = input_text.get("1.0", "end-1c")
        if mode.get() == "encrypt":
            result = enkripsi(text, shift)
        else:
            result = dekripsi(text, shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
    except ValueError:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter a valid shift value.")

# GUI setup
root = tk.Tk()
root.title("Cipher Encryption Machine")
root.geometry("500x400")
root.config(bg="#f39c12")  # Bright yellow-orange background

# Styling
title_font = ("Arial", 16, "bold")
label_font = ("Arial", 12, "bold")
button_font = ("Arial", 12, "bold")

# Title Label
title_label = tk.Label(root, text="Caesar Cipher Encryption/Decryption", font=title_font, bg="#e67e22", fg="white")
title_label.pack(pady=10, fill="x")

# Shift Value Frame
shift_frame = tk.Frame(root, bg="#f39c12")
shift_frame.pack(pady=10)
tk.Label(shift_frame, text="Set Shift Value:", font=label_font, bg="#f39c12", fg="white").grid(row=0, column=0, padx=10, pady=5)
shift_value = tk.Entry(shift_frame, width=5, font=label_font, bg="#f7dc6f", fg="#2c3e50")
shift_value.grid(row=0, column=1, padx=5, pady=5)

# Input Text Frame
input_frame = tk.Frame(root, bg="#f39c12")
input_frame.pack(pady=10)
tk.Label(input_frame, text="Input Text to Encrypt/Decrypt:", font=label_font, bg="#f39c12", fg="white").grid(row=0, column=0, padx=10, pady=5)
input_text = tk.Text(input_frame, height=5, width=40, font=("Arial", 10), bg="#f7dc6f", fg="#2c3e50")
input_text.grid(row=1, column=0, padx=10, pady=5)

# Mode selection
mode_frame = tk.Frame(root, bg="#f39c12")
mode_frame.pack(pady=10)
mode = tk.StringVar(value="encrypt")
ttk.Style().configure("TRadiobutton", background="#f39c12", foreground="white", font=label_font)
ttk.Radiobutton(mode_frame, text="Encrypt", variable=mode, value="encrypt", style="TRadiobutton").grid(row=0, column=0, padx=20)
ttk.Radiobutton(mode_frame, text="Decrypt", variable=mode, value="decrypt", style="TRadiobutton").grid(row=0, column=1, padx=20)

# Process Button
process_button = tk.Button(root, text="Process Text", command=process_text, font=button_font, bg="#27ae60", fg="white", activebackground="#2ecc71", activeforeground="white", relief="raised")
process_button.pack(pady=10)

# Output Text Frame
output_frame = tk.Frame(root, bg="#f39c12")
output_frame.pack(pady=10)
tk.Label(output_frame, text="Output:", font=label_font, bg="#f39c12", fg="white").grid(row=0, column=0, padx=10, pady=5)
output_text = tk.Text(output_frame, height=5, width=40, font=("Arial", 10), bg="#f7dc6f", fg="#2c3e50")
output_text.grid(row=1, column=0, padx=10, pady=5)

root.mainloop()
