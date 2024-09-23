import tkinter as tk
import subprocess
import os

# Define paths to the applications
ENGLISH_APP_PATH = r"english_app.py"
MATH_APP_PATH = r"math_app.py"

def open_english_app():
    """Open the English question app."""
    if os.path.exists(ENGLISH_APP_PATH):
        subprocess.run(["python", ENGLISH_APP_PATH], check=True)
    else:
        print("English app not found at", ENGLISH_APP_PATH)

def open_math_app():
    """Open the Math question app."""
    if os.path.exists(MATH_APP_PATH):
        subprocess.run(["python", MATH_APP_PATH], check=True)
    else:
        print("Math app not found at", MATH_APP_PATH)

# Create the main application window
app = tk.Tk()
app.title("SAT Question Manager")

# Add a label to the GUI
label = tk.Label(app, text="Choose an application to open:")
label.pack(pady=20)

# Button to open the English app
english_button = tk.Button(app, text="Open English App", command=open_english_app, width=30)
english_button.pack(pady=10)

# Button to open the Math app
math_button = tk.Button(app, text="Open Math App", command=open_math_app, width=30)
math_button.pack(pady=10)

# Start the application
app.mainloop()
