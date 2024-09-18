import argparse
from gendiff.parser import parse
from gendiff.get_diff import get_diff
from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain
from gendiff.formaters.json import json_format

formaters = {
    'stylish': stylish,
    'plain': plain,
    'json': json_format,
}


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output',
                        default='stylish'
                        )
    args = parser.parse_args()

    file_path_1 = args.first_file
    file_path_2 = args.second_file
    formater = args.format

    diff = generate_diff(file_path_1, file_path_2, formater)
    print(diff)


def generate_diff(file_path_1, file_path_2, format_name='stylish'):
    data_1, data_format_1 = read_data(file_path_1)
    data_2, data_format_2 = read_data(file_path_2)
    first_file = parse(data_1, data_format_1)
    second_file = parse(data_2, data_format_2)
    diff = get_diff(first_file, second_file)
    diff = formaters[format_name](diff)
    return diff


def read_data(file_path):
    file_format = file_path.split('.')[-1]
    with open(file_path) as file:
        return file.read(), file_format


if __name__ == "__main__":
    main()
