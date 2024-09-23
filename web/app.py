from flask import Flask, render_template, jsonify, url_for
import json
import os

app = Flask(__name__)

# Path to your English questions JSON file
QUESTIONS_PATH = r"C:\Users\aarus\OneDrive\Desktop\SAT\sat app\question_setup\questions\english"

@app.route('/')
def index():
    # Load the questions from the JSON file
    with open(os.path.join(QUESTIONS_PATH, 'questions.json'), 'r') as file:
        questions = json.load(file)
    
    return render_template('index.html', questions=questions)

if __name__ == "__main__":
    app.run(debug=True)
