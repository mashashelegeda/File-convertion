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


def json_load(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def json_save(result, file_path):
    with open(file_path, 'w')as file:
        return json.dump(result, file)
        
def yaml_load(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

      
if __name__ == "__main__":
    main()
