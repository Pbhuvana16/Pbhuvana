from flask import Flask, request, jsonify
from database_opr import get_employees, get_employee, add_employee, update_employee, delete_employee

app = Flask(__name__)

@app.route('/api/employees', methods=['GET'])
def get_all_employees():
    employees = get_employees()
    return jsonify(employees), 200

@app.route('/api/employees/<int:employee_id>', methods=['GET'])
def get_single_employee(employee_id):
    employee = get_employee(employee_id)
    if employee:
        return jsonify(employee), 200
    else:
        return 'Employee not found', 404

@app.route('/api/employees', methods=['POST'])
def create_employee():
    data = request.get_json()
    employee_name = data.get('employee_name')
    employee_department = data.get('employee_department')
    if employee_name and employee_department:
        add_employee(employee_name, employee_department)
        return 'Employee added successfully', 201
    else:
        return 'Invalid JSON data format or missing fields', 400

@app.route('/api/employees/<int:employee_id>', methods=['PUT'])
def update_single_employee(employee_id):
    data = request.get_json()
    employee_name = data.get('emploayee_name')
    employee_department = data.get('employee_department')
    if employee_name and employee_department:
        update_employee(employee_id,employee_name, employee_department)
        return 'Employee updated successfully', 200
    else:
        return 'Invalid JSON data format or missing fields', 400

@app.route('/api/employees/<int:employee_id>', methods=['DELETE'])
def delete_single_employee(employee_id):
    delete_employee(employee_id)
    return 'Employee deleted successfully', 200


if __name__ == '__main__':
    app.run(debug=True)
