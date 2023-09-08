#Use an official Python runtime as a parent image
FROM python:3.8-slim
RUN pip install xmltodict
#RUN apt-get update && apt-get install -y libxml2-dev


#Set the working directory in the container
WORKDIR /testwork

#COPY my_xml.xml /testwork/
#Copy the Python script to the container
COPY xml_json.py /testwork/

#Run the Python script when the container launches
ENTRYPOINT ["python", "/testwork/xml_json.py"]
