import os
import json

def get_next_filename(directory):
    """Returns the next numbered filename in the specified directory."""
    existing_files = [f for f in os.listdir(directory) if f.endswith('.json')]
    if not existing_files:
        return '1.json'
    else:
        # Extract numbers from filenames and find the next number
        numbers = [int(f.split('.')[0]) for f in existing_files]
        return f'{max(numbers) + 1}.json'

def create_json_file(directory, question_data):
    """Creates a new JSON file with the next number as the filename and saves question data."""
    filename = get_next_filename(directory)
    filepath = os.path.join(directory, filename)
    
    # Write the question data to the new JSON file
    with open(filepath, 'w') as json_file:
        json.dump(question_data, json_file, indent=4)
    
    print(f'Created file: {filepath}')
    return filepath

def ensure_directory(subject):
    """Ensures the directory for the selected subject exists and returns the path."""
    directory = os.path.join('questions', subject)
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    return directory
