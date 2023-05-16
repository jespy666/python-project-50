import pytest
from gendiff.gendiff import generate_diff
from tests import FIXTURES_PATH


def get_fixture_path(file_name: str) -> str:
    """
    Function Takes file name and return path to file.
    """
    return f'{FIXTURES_PATH}{file_name}'


def get_result(file_path: str) -> str:
    """
    Reads content and return it to str format.
    """
    with open(file_path) as result:
        return result.read().strip()


file1_json = get_fixture_path('file1.json')
file2_json = get_fixture_path('file2.json')
file1_yaml = get_fixture_path('file1.yaml')
file2_yaml = get_fixture_path('file2.yaml')
nested1_json = get_fixture_path('nested_file1.json')
nested2_json = get_fixture_path('nested_file2.json')
nested1_yaml = get_fixture_path('nested_file1.yaml')
nested2_yaml = get_fixture_path('nested_file2.yaml')
stylish = get_fixture_path('flat_stylish.txt')
nested_stylish = get_fixture_path('nested.txt')
nested_plain = get_fixture_path('plain.txt')
nested_json = get_fixture_path('json_view.json')


@pytest.mark.parametrize('file1, file2, output, formatter', [
    (file1_json, file2_json, stylish, 'stylish'),
    (file1_yaml, file2_yaml, stylish, 'stylish'),
    (nested1_json, nested2_json, nested_stylish, 'stylish'),
    (nested1_yaml, nested2_yaml, nested_stylish, 'stylish'),
    (nested1_json, nested2_json, nested_plain, 'plain'),
    (nested1_yaml, nested2_yaml, nested_plain, 'plain'),
    (nested1_json, nested2_json, nested_json, 'json'),
    (nested1_yaml, nested2_yaml, nested_json, 'json')
])
def test_generate_diff(file1, file2, output, formatter):
    assert generate_diff(file1, file2, formatter) ==\
           get_result(output)
