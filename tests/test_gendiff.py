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
nested_file1_json = get_fixture_path('nested_file1.json')
nested_file2_json = get_fixture_path('nested_file2.json')
nested_file1_yaml = get_fixture_path('nested_file1.yaml')
nested_file2_yaml = get_fixture_path('nested_file2.yaml')
stylish_result = get_fixture_path('flat_stylish.txt')
stylish_nested_result = get_fixture_path('nested.txt')
plain_nested_result = get_fixture_path('plain.txt')
json_nested_result = get_fixture_path('json_view.json')


@pytest.mark.parametrize('file1, file2, stylish_output', [
    (file1_json, file2_json, stylish_result),
    (file1_yaml, file2_yaml, stylish_result),
    (nested_file1_json, nested_file2_json, stylish_nested_result),
    (nested_file1_yaml, nested_file2_yaml, stylish_nested_result),
])
def test_stylish(file1, file2, stylish_output):
    format_name = 'stylish'
    assert generate_diff(file1, file2, format_name) ==\
           get_result(stylish_output)


@pytest.mark.parametrize('file1, file2, plain_output', [
    (nested_file1_json, nested_file2_json, plain_nested_result),
    (nested_file1_yaml, nested_file2_yaml, plain_nested_result),
])
def test_plain(file1, file2, plain_output):
    format_name = 'plain'
    assert generate_diff(file1, file2, format_name) ==\
           get_result(plain_output)


@pytest.mark.parametrize('file1, file2, json_view', [
    (nested_file1_json, nested_file2_json, json_nested_result),
    (nested_file1_yaml, nested_file2_yaml, json_nested_result),
])
def test_json_view(file1, file2, json_view):
    format_name = 'json'
    assert generate_diff(file1, file2, format_name) ==\
           get_result(json_view)
