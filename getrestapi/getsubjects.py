from flask import Flask, request, jsonify

# Create a Flask web application instance
app = Flask(__name__)

# Sample data 
subjects = [
    {"subject_number": "1", "subject_name": "Maths", "marks": "95"},
    {"subject_number": "2", "subject_name": "Physics", "marks": "98"},
    {"subject_number": "3", "subject_name": "Chemistry", "marks": "90"},
    {"subject_number": "4", "subject_name": "English", "marks": "90"},
    {"subject_number": "5", "subject_name": "Telugu", "marks": "95"},
]

# Define a route that responds to HTTP GET requests at '/'
@app.route('/', methods=['GET'])
def get():
    # Return a JSON format of subjects
    return jsonify(subjects)

# Define a route that responds to HTTP GET requests at '/<marks>'
@app.route('/<marks>', methods=['GET'])
def get_subjects(marks):
    subjects_in_same_marks = []

    # Iterate through the subjects list
    for item in subjects:
        if item['marks'] == marks:
            subjects_in_same_marks.append(item)

    # Return a JSON representation of the filtered subjects list
    return jsonify(subjects_in_same_marks)

if __name__ == '__main__':
    app.run(debug=True)
