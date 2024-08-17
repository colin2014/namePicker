import os
import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # Get the list of classes (text files) in the 'data' directory
    class_files = [f for f in os.listdir('data') if f.endswith('.txt')]
    
    # Debug print to show the files found
    print("Files found in 'data' directory:", class_files)
    
    class_names = [os.path.splitext(f)[0] for f in class_files]
    return render_template('index.html', classes=class_names)

@app.route('/get_random_name', methods=['POST'])
def get_random_name():
    class_name = request.form['class_name']
    file_name = os.path.join('data', f"{class_name}.txt")
    
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            names = [name.strip() for name in f.readlines() if name.strip()]
            if names:
                selected_name = random.choice(names)
                return jsonify({'name': selected_name})
    
    return jsonify({'error': 'Class not found or file is empty'}), 404

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/get_random_name', methods=['POST'])
def get_random_name():
    class_name = request.form['class_name']
    file_name = os.path.join('data', f"{class_name}.txt")
    
    # Debug print to verify the file path
    print("Looking for file:", file_name)
    
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            names = [name.strip() for name in f.readlines() if name.strip()]
            if names:
                selected_name = random.choice(names)
                return jsonify({'name': selected_name})
    
    return jsonify({'error': 'Class not found or file is empty'}), 404
