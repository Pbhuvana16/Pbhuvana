
# Exercise1 : Write a GET Rest API using Python.

from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for demonstration
subjects = [
{"subject_number":"1", "subject_name":"Maths", "marks":"95"},
{"subject_number":"2", "subject_name":"Pysics", "marks":"98"},
{"subject_number":"3", "subject_name":"Chemistry", "marks":"90"},
{"subject_number":"4", "subject_name":"English", "marks":"90"},
{"subject_number":"5", "subject_name":"Telugu", "marks":"95"},
]

@app.route('/', methods=['GET'])
def get():
    return jsonify(subjects)

@app.route('/<marks>', methods=['GET'])
def get_subjects(marks):
    subjects_in_same_marks=[]
    for item in subjects:
        if item['marks'] == marks:
            subjects_in_same_marks.append(item)
    return subjects_in_same_marks

if __name__ == '__main__':
    app.run(debug=True)
