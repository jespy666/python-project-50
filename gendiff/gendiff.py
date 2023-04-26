import json
import difflib


def generate_diff(file_path1, file_path2):
    first_data = json.load(open(file_path1))
    second_data = json.load(open(file_path2))
    diff = difflib.unified_diff(
        json.dumps(first_data, sort_keys=True, indent=4).splitlines(),
        json.dumps(second_data, sort_keys=True, indent=4).splitlines(),
        fromfile='first',
        tofile='second',
        lineterm=''
    )
    result = '\n'.join(diff)
    begin = result.find('{')
    return result[begin:]
