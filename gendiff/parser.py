import json
import yaml


def parse(data, data_format):
    parser = {
        'json': json.loads,
        'yaml': yaml.safe_load,
        'yml': yaml.safe_load
    }
    data_format = data_format.lower()
    if data_format not in parser:
        raise ValueError(f"Unsupported file format: {data_format}")
    return parser[data_format](data)
