import mysql.connector
import json

 
# MySQL database configuration
def load_database_config():
    with open('config.json') as config_file:
        config = json.load(config_file)
        database_config = config.get('database_config', {})
    return database_config

 

# Function to establish a database connection
def connect_to_database():
   database_config = load_database_config()
   return mysql.connector.connect(**database_config)

 

 

# Function to get all employees from the database
def get_employees():
    connection = connect_to_database()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employee")
    employees = cursor.fetchall()
    cursor.close()
    connection.close()
    return employees

 

# Function to get a specific employee by ID from the database
def get_employee(employee_id):
    connection = connect_to_database()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employee WHERE employee_id = %s", (employee_id,))
    employee = cursor.fetchone()
    cursor.close()
    connection.close()
    return employee

 

# Function to add an employee to the database
def add_employee(employee_name,employee_department):
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "INSERT INTO employee (employee_name, employee_department) VALUES (%s, %s)"
    values = (employee_name,employee_department)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

 

# Function to update an employee in the database by ID
def update_employee(employee_id, employee_name, employee_department):
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "UPDATE employee SET name = %s, department = %s WHERE id = %s"
    values = (employee_name, employee_department, employee_id)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

 

# Function to delete an employee from the database by ID
def delete_employee(employee_id):
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "DELETE FROM employee WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()
    cursor.close()
    connection.close()
    
    
