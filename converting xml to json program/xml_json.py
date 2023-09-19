import xmltodict  
import json  

#user to enter the XML file name
my_xml = input("Enter the file name:")

# Open the XML file and read its contents
def read_xml_file(file_name):
    with open(file_name) as xml_file:
        return xml_file.read()

# Parse the XML content into a Python dictionary
def parse_xml_to_dict(xml_content):
    return xmltodict.parse(xml_content)

# Convert the Python dictionary to JSON
def convert_dict_to_json(my_dict):
    return json.dumps(my_dict)

# Print the JSON data
def print_json_data(json_data):
    print(json_data)

# Main function
def main():
    xml_content = read_xml_file(my_xml)
    my_dict = parse_xml_to_dict(xml_content)
    json_data = convert_dict_to_json(my_dict)
    print_json_data(json_data)

if __name__ == "__main__":
    main()  # Call the main function
