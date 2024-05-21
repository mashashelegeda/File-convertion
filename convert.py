import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Data convertion')
    parser.add_argument('input_file', type=str)
    parser.add_argument('output_file', type=str)
    return parser.parse_args()

def main():
    args = parse_arguments()

    result = ""
    files_format = args.input_file.split('.')[-1].lower()
    if files_format == 'json':
        result = json_load(args.input_file)
    elif files_format == 'yaml' or files_format == 'yml':
        result = yaml_load(args.input_file)
    elif files_format == 'xml':
        result = xml_load(args.input_file)
    else:
        print("Available formats: json, yml(yaml), xml")
        return

    output_format = args.output_file.split(".")[-1].lower()
    if output_format == 'json':
        json_save(result, args.output_file)
    elif output_format in ['yml', 'yaml']:
        yaml_save(result, args.output_file)
    elif output_format == 'xml':
        xml_save(result, args.output_file)
    else:
        print('Available formats: json, yml(yaml), xml')


def json_load(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def json_save(result, file_path):
    with open(file_path, 'w')as file:
        return json.dump(result, file)
        
def yaml_load(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
        
def yaml_save(result, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(result, file)
        
def xml_load(file_path):
    with open(file_path, 'r') as file:
        return xmltodict.parse(file.read())
        
def xml_save(result, file_path):
    with open(file_path, "w") as file:
        xmltodict.unparse(result, output=file, pretty=True)


      
if __name__ == "__main__":
    main()
