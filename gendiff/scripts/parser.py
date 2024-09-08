import json
import yaml


def parse(file_path):
    splited_file_path = file_path.split('.')
    extension = splited_file_path[-1].lower()
    parser = {
        'json': json.load,
        'yaml': yaml.safe_load,
        'yml': yaml.safe_load
    }
    if extension not in parser:
        raise ValueError(f"Unsupported file format: {extension}")
    with open(file_path) as file:
        return parser[extension](file)
    

