import argparse
from gendiff.scripts.parser import parse
from gendiff.scripts.get_diff import get_diff
from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain


formaters = {
    'stylish': stylish,
    'plain': plain,
    }



def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    file_path_1 = args.first_file
    file_path_2 = args.second_file
    formater = args.format
    diff = generate_diff(file_path_1, file_path_2, formater)
    return diff


def generate_diff(file_path_1, file_path_2, format_name='stylish'):
    fisrt_file = parse(file_path_1)
    second_file = parse(file_path_2)
    diff = get_diff(fisrt_file, second_file)
    diff = formaters[format_name](diff)
    return diff


if __name__ == "__main__":
    main()
