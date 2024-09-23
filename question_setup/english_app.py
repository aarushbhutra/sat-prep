import tkinter as tk
from tkinter import ttk
import json
import os

# File path for storing questions
QUESTIONS_FILE_PATH = 'questions\english\questions.json'

# Categories for English questions
categories = {
    "Comprehension": [
        "Central Ideas and Details",
        "Inferences",
        "Command of Evidence"
    ],
    "Language and Structure": [
        "Words in Context",
        "Text Structure and Purpose",
        "Cross-Text Connections"
    ],
    "Rhetoric": [
        "Rhetorical Synthesis",
        "Transitions"
    ],
    "Form and Sense": [
        "Boundaries",
        "Form, Structure, and Sense"
    ]
}

difficulty_levels = ["Easy", "Medium", "Hard"]

def ensure_directory():
    """Ensure the directory exists where the JSON file is stored."""
    directory = os.path.dirname(QUESTIONS_FILE_PATH)
    if not os.path.exists(directory):
        os.makedirs(directory)

def load_existing_questions():
    """Load the existing questions from the JSON file, or return an empty dictionary if the file doesn't exist."""
    if os.path.exists(QUESTIONS_FILE_PATH):
        with open(QUESTIONS_FILE_PATH, 'r') as file:
            return json.load(file)
    return {}

def save_question():
    """Save the question data to the questions.json file."""
    # Get form data
    question_data = {
        "category": category_var.get(),
        "difficulty": difficulty_var.get(),
        "text": text_entry.get("1.0", tk.END).strip(),
        "question": question_text.get("1.0", tk.END).strip(),
        "options": [
            {"option": mcq_var1.get(), "correct": mcq_check1.get()},
            {"option": mcq_var2.get(), "correct": mcq_check2.get()},
            {"option": mcq_var3.get(), "correct": mcq_check3.get()},
            {"option": mcq_var4.get(), "correct": mcq_check4.get()}
        ]
    }

    # Ensure the directory exists
    ensure_directory()

    # Load existing questions from the JSON file
    questions = load_existing_questions()

    # Determine the new question ID
    new_id = str(len(questions) + 1)

    # Add the new question to the questions dictionary
    questions[new_id] = question_data

    # Save the updated questions back to the JSON file
    with open(QUESTIONS_FILE_PATH, 'w') as file:
        json.dump(questions, file, indent=4)

    # Clear the form for a new entry
    clear_form()

def clear_form():
    """Clears the form fields after saving the question."""
    category_var.set("")
    difficulty_var.set("")
    text_entry.delete("1.0", tk.END)
    question_text.delete("1.0", tk.END)
    mcq_var1.set("")
    mcq_var2.set("")
    mcq_var3.set("")
    mcq_var4.set("")
    mcq_check1.set(False)
    mcq_check2.set(False)
    mcq_check3.set(False)
    mcq_check4.set(False)

# Main application window
app = tk.Tk()
app.title("English Question Entry")

# Category Dropdown
category_var = tk.StringVar()
category_label = ttk.Label(app, text="Category:")
category_label.pack()
category_menu = ttk.Combobox(app, textvariable=category_var)
category_menu['values'] = [item for sublist in categories.values() for item in sublist]
category_menu.pack()

# Difficulty Dropdown
difficulty_var = tk.StringVar()
difficulty_label = ttk.Label(app, text="Difficulty:")
difficulty_label.pack()
difficulty_menu = ttk.Combobox(app, textvariable=difficulty_var, values=difficulty_levels)
difficulty_menu.pack()

# Text Box for the main text
text_label = ttk.Label(app, text="Text:")
text_label.pack()
text_entry = tk.Text(app, height=6, width=50)
text_entry.pack()

# Question Text Box
question_label = ttk.Label(app, text="Question:")
question_label.pack()
question_text = tk.Text(app, height=4, width=50)
question_text.pack()

# MCQ Options Frame with checkboxes for correct answers
mcq_frame = tk.Frame(app)

mcq_var1 = tk.StringVar()
mcq_var2 = tk.StringVar()
mcq_var3 = tk.StringVar()
mcq_var4 = tk.StringVar()

mcq_check1 = tk.BooleanVar()
mcq_check2 = tk.BooleanVar()
mcq_check3 = tk.BooleanVar()
mcq_check4 = tk.BooleanVar()

mcq_label1 = ttk.Label(mcq_frame, text="Option 1:")
mcq_label1.grid(row=0, column=0)
mcq_entry1 = ttk.Entry(mcq_frame, textvariable=mcq_var1)
mcq_entry1.grid(row=0, column=1)
mcq_checkbox1 = ttk.Checkbutton(mcq_frame, variable=mcq_check1, text="Correct")
mcq_checkbox1.grid(row=0, column=2)

mcq_label2 = ttk.Label(mcq_frame, text="Option 2:")
mcq_label2.grid(row=1, column=0)
mcq_entry2 = ttk.Entry(mcq_frame, textvariable=mcq_var2)
mcq_entry2.grid(row=1, column=1)
mcq_checkbox2 = ttk.Checkbutton(mcq_frame, variable=mcq_check2, text="Correct")
mcq_checkbox2.grid(row=1, column=2)

mcq_label3 = ttk.Label(mcq_frame, text="Option 3:")
mcq_label3.grid(row=2, column=0)
mcq_entry3 = ttk.Entry(mcq_frame, textvariable=mcq_var3)
mcq_entry3.grid(row=2, column=1)
mcq_checkbox3 = ttk.Checkbutton(mcq_frame, variable=mcq_check3, text="Correct")
mcq_checkbox3.grid(row=2, column=2)

mcq_label4 = ttk.Label(mcq_frame, text="Option 4:")
mcq_label4.grid(row=3, column=0)
mcq_entry4 = ttk.Entry(mcq_frame, textvariable=mcq_var4)
mcq_entry4.grid(row=3, column=1)
mcq_checkbox4 = ttk.Checkbutton(mcq_frame, variable=mcq_check4, text="Correct")
mcq_checkbox4.grid(row=3, column=2)

mcq_frame.pack()

# Save Button
save_button = ttk.Button(app, text="Save Question", command=save_question)
save_button.pack()

# Start the application
app.mainloop()
