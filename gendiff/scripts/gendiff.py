import argparse
from gendiff.scripts.parser import parse
from gendiff.scripts.get_diff import get_diff
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
    first_file = parse(file_path_1)
    second_file = parse(file_path_2)
    diff = get_diff(first_file, second_file)
    diff = formaters[format_name](diff)
    return diff


if __name__ == "__main__":
    main()
