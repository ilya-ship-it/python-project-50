import argparse
from gendiff.scripts.parser import parse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    file_path_1 = args.first_file
    file_path_2 = args.second_file
    diff = generate_diff(file_path_1, file_path_2)
    return diff


def generate_diff(file_path_1, file_path_2):
    fisrt_file = parse(file_path_1)
    second_file = parse(file_path_2)
    fisrt_file = dict(sorted(fisrt_file.items()))
    new_line_keys = list(filter(lambda key: key not in fisrt_file, second_file))
    result = '{'
    for key, value in fisrt_file.items():
        if key not in second_file:
            result += f"\n    - {key}: {value}"
        elif value != second_file[key]:
            result += f"\n    - {key}: {value}"
            result += f"\n    + {key}: {second_file[key]}"
        else:
            result += f"\n      {key}: {value}"
    for key in new_line_keys:
        result += f"\n    + {key}: {second_file[key]}"
    result += '\n}'
    return result


if __name__ == "__main__":
    main()
