INDENT = '    '
ADD = '  + '
REMOVE = '  - '
OPEN_BRACER = '{\n'
CLOSE_BRACER = '}\n'


def to_stylish_str(item) -> str:
    """
    Convert data to str format.
    """
    if isinstance(item, dict):
        return str(item)
    if item is None:
        return 'null'
    if isinstance(item, bool):
        return str(item).lower()
    return item


def make_stylish(tree: dict) -> str:
    """
    Function takes a tree(dict) and return str view in 'stylish' format.
    """
    def walk(node, depth):
        if not isinstance(node, dict):
            return to_stylish_str(node)
        result = OPEN_BRACER
        for key, value in node.items():
            if not isinstance(value, dict):
                result += f'{INDENT * depth}{INDENT}{key}: ' \
                          f'{to_stylish_str(value)}\n'
            else:
                if 'action' not in value:
                    result += f'{INDENT * depth}{INDENT}{key}: ' \
                              f'{walk(value, depth + 1)}\n'
                else:
                    action = value.get('action')
                    children = value.get('children')
                    new_value = value.get('value')
                    old_value = value.get('old_value')
                    actions = {
                        'nested': f'{INDENT * depth}{INDENT}{key}:'
                                  f' {walk(children, depth+1)}\n',
                        'update': f'{INDENT * depth}{REMOVE}{key}:'
                                  f' {walk(old_value, depth+1)}\n'
                                  f'{INDENT * depth}{ADD}{key}:'
                                  f' {walk(new_value, depth+1)}\n',
                        'added': f'{INDENT * depth}{ADD}{key}: '
                                 f'{walk(new_value, depth+1)}\n',
                        'removed': f'{INDENT * depth}{REMOVE}{key}:'
                                   f' {walk(new_value, depth+1)}\n',
                        'unstaged': f'{INDENT * depth}{INDENT}{key}:'
                                    f' {walk(new_value, depth+1)}\n'
                    }
                    result += actions[action]
        result += f'{INDENT * depth}{CLOSE_BRACER}'
        return result.strip()

    return walk(tree, 0)
