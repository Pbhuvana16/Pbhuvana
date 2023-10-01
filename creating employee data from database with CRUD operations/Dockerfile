# Use an official Python runtime as a parent image
FROM python:3.8-slim
#FROM mysql:latest
# Install necessary packages
RUN apt-get update && apt-get install -y default-libmysqlclient-dev
# Install Flask and any other dependencies
RUN apt-get update && apt-get install -y mariadb-server default-libmysqlclient-dev

 

# Install Flask and mysql-connector-python
RUN pip install flask mysql-connector-python
# Set the working directory in the container
WORKDIR /crudopr

 

# Copy your Flask application code into the container
COPY restapi.py /crudopr/
COPY database_opr.py /crudopr/
COPY config.json /crudopr/
# Expose the port your Flask app will run on
EXPOSE 5000
EXPOSE 3306
 

# Run your Flask application
CMD ["python", "restapi.py"]
