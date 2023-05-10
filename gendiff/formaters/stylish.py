INDENT = '    '
ADD = '  + '
REMOVE = '  - '
OPEN_BRACER = '{\n'
CLOSE_BRACER = '}\n'
ACTIONS = {
           'added': ADD,
           'removed': REMOVE,
           'unstaged': INDENT,
           }


def to_stylish_str(item) -> str:
    """
    Convert data to str format.
    """
    if item is None:
        return 'null'
    if isinstance(item, bool):
        return str(item).lower()
    return str(item)


def make_stylish(tree: dict) -> str:  # noqa C901
    """
    Function takes a tree(dict) and return str view in 'stylish' format.
    """
    def walk(node, depth):
        if not isinstance(node, dict):
            return to_stylish_str(node)
        result = OPEN_BRACER
        for key, value in node.items():
            if not isinstance(value, dict):
                result += f'{INDENT * depth}{INDENT}{key}:' \
                          f' {to_stylish_str(value)}\n'
            elif value.get('action') == 'nested':
                result += f'{INDENT * depth}{INDENT}{key}:' \
                          f' {walk(value.get("children"), depth + 1)}\n'
            elif value.get('action') == 'update':
                result += f'{INDENT * depth}{REMOVE}{key}:' \
                          f' {walk(value.get("old_value"), depth + 1)}\n'
                result += f'{INDENT * depth}{ADD}{key}:' \
                          f' {walk(value.get("value"), depth + 1)}\n'
            elif value.get('action') in ACTIONS:
                result += f'{INDENT * depth}{ACTIONS[value.get("action")]}' \
                          f'{key}:' \
                          f' {walk(value.get("value"), depth + 1)}\n'
            else:
                result += f'{INDENT * depth}{INDENT}{key}:' \
                          f' {walk(value, depth + 1)}\n'
        result += f'{INDENT * depth}{CLOSE_BRACER}'
        return result.strip()
    return walk(tree, 0)
