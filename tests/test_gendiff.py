import pytest
from gendiff.scripts.gendiff import generate_diff


@pytest.mark.parametrize("file_1, file_2, expected", [
    ("tests/fixtures/filepath1.json", "tests/fixtures/filepath2.json",
    "tests/fixtures/expected_1.txt"),
    ("tests/fixtures/filepath1.yaml", "tests/fixtures/filepath2.yaml",
    "tests/fixtures/expected_1.txt"),
    ("tests/fixtures/filepath3.json", "tests/fixtures/filepath4.json",
    "tests/fixtures/expected_2.txt"),
    ("tests/fixtures/filepath3.yaml", "tests/fixtures/filepath4.yaml",
    "tests/fixtures/expected_2.txt")
    ])
def test_generate_diff(file_1, file_2, expected):
    diff = generate_diff(file_1, file_2)
    expected_result = read_file(expected)
    assert diff == expected_result

def read_file(file_name):
    with open(file_name) as file:
        return file.read()
