from flask import Flask, request, jsonify
import json

# Create a Flask web application instance
app = Flask(__name__)

# Read the config.json file
with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)

# Define a route that responds to HTTP GET requests at '/'
@app.route('/subjects', methods=['GET'])
def get():
    # Return a JSON format of subjects
    return jsonify(config_data['subjects'])

# Define a route that responds to HTTP GET requests at '/<marks>'
@app.route('/<marks>', methods=['GET'])
def get_subjects(marks):
    subjects_in_same_marks = []

    # Iterate through the subjects list
    for item in config_data['subjects']:
        if item['marks'] == marks:
            subjects_in_same_marks.append(item)

    # Return a JSON representation of the filtered subjects list
    return jsonify(subjects_in_same_marks)

if __name__ == '__main__':
    app.run(debug=True)
