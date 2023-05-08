import pytest
from gendiff.gendiff import generate_diff
from tests import FIXTURES_PATH


def get_fixture_path(file_name: str) -> str:
    """
    Function Takes file name and return path to file.
    """
    return f'{FIXTURES_PATH}{file_name}'


def get_result(file_name: str) -> str:
    """
    Reads content and return it to str format
    """
    with open(file_name) as result:
        return result.read()


@pytest.mark.parametrize('file1, file2, output', [
    ('file1.json', 'file2.json', 'flat_expected.txt'),
    ('file1.yaml', 'file2.yaml', 'flat_expected.txt'),
    ('nested_file1.json', 'nested_file2.json', 'nested.txt'),
    ('nested_file1.yaml', 'nested_file2.yaml', 'nested.txt')
])
def test_generate_diff(file1, file2, output):
    file1_path = get_fixture_path(file1)
    file2_path = get_fixture_path(file2)
    expected_path = get_fixture_path(output)
    assert generate_diff(file1_path, file2_path) ==\
           get_result(expected_path)
