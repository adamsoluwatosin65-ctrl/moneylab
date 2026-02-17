import tkinter as tk
from tkinter import messagebox
import random

def move_button(event):
    """Moves the 'No' button to a random position when hovered."""
    new_x = random.randint(50, 350)
    new_y = random.randint(50, 250)
    no_btn.place(x=new_x, y=new_y)

def show_aza_option():
    """Hides the initial question and shows the 'Send Aza' button."""
    label.config(text="I knew you were a legend! 🫡")
    yes_btn.pack_forget()
    no_btn.place_forget() # Remove the runaway button
    
    aza_btn.pack(pady=20)

def show_account():
    """Shows the final account details."""
    messagebox.showinfo("Account Details", "OPAY\n8026294248\n\nTransfer received in advance! 🤝")
    root.destroy()

# Main Window Setup
root = tk.Tk()
root.title("Quick Question")
root.geometry("500x400")
root.resizable(False, False)

label = tk.Label(root, text="send me  2k? 🥺", font=("Arial", 14, "bold"))
label.pack(pady=50)

# Yes Button
yes_btn = tk.Button(root, text="Yes", font=("Arial", 12), bg="green", fg="white", width=10, command=show_aza_option)
yes_btn.pack(pady=10)

# No Button (The one that runs away)
no_btn = tk.Button(root, text="No", font=("Arial", 12), bg="red", fg="white", width=10)
no_btn.place(x=200, y=200)
no_btn.bind("<Enter>", move_button) # Triggers when mouse enters the button area

# Aza Button (Hidden initially)
aza_btn = tk.Button(root, text="Send Aza", font=("Arial", 12), bg="blue", fg="white", width=15, command=show_account)

root.mainloop()