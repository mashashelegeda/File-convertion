
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

if __name__ == "__main__":
    main()