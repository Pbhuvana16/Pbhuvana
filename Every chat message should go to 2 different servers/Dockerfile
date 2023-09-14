#Use an official Python runtime as a parent image
FROM python:3.8-slim

#Set the working directory in the container
WORKDIR /one-many_pro

#Copy the current directory contents into the container at /app
COPY swiggy.py /one-many_pro
COPY zomato.py /one-many_pro
COPY config.json /one-many_pro

#Install any needed packages specified in requirements.txt
# If you have a requirements.txt file for dependencies


#Expose the ports for both servers
EXPOSE 5000
EXPOSE 5001
