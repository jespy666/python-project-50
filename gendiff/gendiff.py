from gendiff.parser import parse_data


def generate_diff(file_path1: str, file_path2: str) -> str:
    """
    Function takes paths of both files and return diff between it in str format.
    """
    file1, file2 = parse_data(file_path1, file_path2)
    keys1 = set(file1.keys())
    keys2 = set(file2.keys())
    added_keys = keys2 - keys1
    removed_keys = keys1 - keys2
    common_keys = keys1 & keys2
    changed_keys = {k for k in common_keys if file1[k] != file2[k]}
    unchanged_key = {k for k in common_keys if file1[k] == file2[k]}
    diff = '{\n'
    for k in sorted(added_keys | removed_keys | changed_keys | unchanged_key):
        if k in added_keys:
            diff += f'  + {k}: {str(file2[k]).lower()}\n'
        elif k in removed_keys:
            diff += f'  - {k}: {str(file1[k]).lower()}\n'
        elif k in changed_keys:
            diff += f'  - {k}: {str(file1[k]).lower()}\n'
            diff += f'  + {k}: {str(file2[k]).lower()}\n'
        elif k in unchanged_key:
            diff += f'    {k}: {str(file1[k]).lower()}\n'
    diff += '}'
    return diff.strip()
