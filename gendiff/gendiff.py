from gendiff.parser import parse_data
from gendiff.diff_builder import build_diff
from gendiff.formaters.stylish import make_stylish
from gendiff.formaters.plain import make_plain


def get_formater(format_name):
    formatter = make_stylish
    if format_name == 'plain':
        formatter = make_plain
    return formatter


def generate_diff(file_path1: str, file_path2: str,
                  format_name='stylish') -> str:
    """
    Function generate diff between two files in default format - 'stylish'.
    """
    data1, data2 = parse_data(file_path1, file_path2)
    diff = build_diff(data1, data2)
    formater = get_formater(format_name)
    return formater(diff)
