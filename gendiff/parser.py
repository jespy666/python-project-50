import json
import yaml


def get_files_format(file1_path: str, file2_path: str) -> str:
    """
    Function takes two file paths as inputs and returns the format of the files.
    """
    file1_name = file1_path.split('/')[-1]
    file2_name = file2_path.split('/')[-1]
    file1_extension = file1_name.split('.')[-1]
    file2_extension = file2_name.split('.')[-1]
    if file1_extension == file2_extension:
        return file1_extension
    else:
        raise Exception('File formats do not match!')


def get_files_data(file1_path: str, file2_path: str) -> tuple:
    """
    Function takes two file paths and returns the tuple of both files data.
    """
    with open(file1_path, 'r') as f1:
        data1 = f1.read()
    with open(file2_path, 'r') as f2:
        data2 = f2.read()
    return data1, data2


def parse_data(file1_path: str, file2_path: str) -> tuple:
    """
    Reads content of two files and return their data as a tuple of dict.
    """
    data1, data2 = get_files_data(file1_path, file2_path)
    file_format = get_files_format(file1_path, file2_path)
    if file_format == 'json':
        return json.loads(data1), json.loads(data2)
    elif file_format == 'yaml' or file_format == 'yml':
        return yaml.safe_load(data1), yaml.safe_load(data2)
    else:
        raise Exception('Unsupported file format!')
