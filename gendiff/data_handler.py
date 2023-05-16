
def get_extension(file_path: str) -> str:
    """
    Function takes file path as input and return extension of file.
    """
    name = file_path.split('/')[-1]
    return name.split('.')[-1]


def get_data(file_path: str) -> str:
    """
    Function takes file path and return file content.
    """
    with open(file_path, 'r') as f1:
        data = f1.read()
    return data
