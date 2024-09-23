import tkinter as tk
from tkinter import ttk
from file_manager import create_json_file, ensure_directory

# Categories for math questions
categories = {
    "Algebra": [
        "Linear equations in one variable",
        "Linear functions",
        "Linear equations in two variables",
        "Systems of two linear equations in two variables",
        "Linear inequalities in one or two variables"
    ],
    "Advanced Math": [
        "Nonlinear functions",
        "Nonlinear equations in one variable and systems of equations in two variables",
        "Equivalent expressions"
    ],
    "Problem-Solving and Data Analysis": [
        "Ratios, rates, proportional relationships, and units",
        "Percentages",
        "One-variable data: Distributions and measures of center and spread",
        "Two-variable data: Models and scatterplots",
        "Probability and conditional probability",
        "Inference from sample statistics and margin of error",
        "Evaluating statistical claims: Observational studies and experiments"
    ],
    "Geometry and Trigonometry": [
        "Area and volume",
        "Lines, angles, and triangles",
        "Right triangles and trigonometry",
        "Circles"
    ]
}

difficulty_levels = ["Easy", "Medium", "Hard"]

def save_question():
    # Get form data
    question_data = {
        "category": category_var.get(),
        "difficulty": difficulty_var.get(),
        "question": question_text.get("1.0", tk.END).strip(),
        "type": type_var.get(),
    }

    if type_var.get() == "MCQ":
        # Collect the options and mark the correct ones
        question_data["options"] = [
            {"option": mcq_var1.get(), "correct": mcq_check1.get()},
            {"option": mcq_var2.get(), "correct": mcq_check2.get()},
            {"option": mcq_var3.get(), "correct": mcq_check3.get()},
            {"option": mcq_var4.get(), "correct": mcq_check4.get()}
        ]
    else:
        question_data["correct_answers"] = answer_text.get().split(',')

    # Ensure math directory exists and save the question data in a JSON file
    directory = ensure_directory('math')
    create_json_file(directory, question_data)

    # Clear the form for a new entry
    clear_form()

def update_options():
    """Updates the form based on the selected question type."""
    if type_var.get() == "MCQ":
        mcq_frame.pack(fill="both", expand=True)
        answer_frame.pack_forget()
    else:
        answer_frame.pack(fill="both", expand=True)
        mcq_frame.pack_forget()

def clear_form():
    """Clears the form fields after saving the question."""
    category_var.set("")
    difficulty_var.set("")
    question_text.delete("1.0", tk.END)
    type_var.set("")
    mcq_var1.set("")
    mcq_var2.set("")
    mcq_var3.set("")
    mcq_var4.set("")
    answer_text.delete(0, tk.END)
    mcq_check1.set(False)
    mcq_check2.set(False)
    mcq_check3.set(False)
    mcq_check4.set(False)

# Main application window
app = tk.Tk()
app.title("Math Question Entry")

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

# Question Text Box
question_label = ttk.Label(app, text="Question:")
question_label.pack()
question_text = tk.Text(app, height=4, width=50)
question_text.pack()

# Type Dropdown (MCQ or User Input)
type_var = tk.StringVar()
type_label = ttk.Label(app, text="Type:")
type_label.pack()
type_menu = ttk.Combobox(app, textvariable=type_var, values=["MCQ", "User Input"])
type_menu.pack()
type_menu.bind("<<ComboboxSelected>>", lambda e: update_options())

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

# User Input Answer Frame
answer_frame = tk.Frame(app)
answer_label = ttk.Label(answer_frame, text="Enter all acceptable answers (separated by commas):")
answer_label.pack()
answer_text = ttk.Entry(answer_frame)
answer_text.pack()

# Save Button
save_button = ttk.Button(app, text="Save Question", command=save_question)
save_button.pack()

# Start the application
app.mainloop()
