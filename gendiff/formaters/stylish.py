INDENT = '    '
ADD = '  + '
REMOVE = '  - '
OPEN_BRACKET = '{\n'
CLOSE_BRACKET = '}\n'


def to_str(item, depth: int) -> str:
    """
    Tree item handler for stylish formatter
    """
    if isinstance(item, dict):
        result = OPEN_BRACKET
        for key, value in item.items():
            if isinstance(value, dict):
                upd_value = to_str(value, depth+1)
                result += f'{INDENT * depth}{INDENT}{key}:' \
                          f' {upd_value}\n'
            else:
                result += f'{INDENT * depth}{INDENT}{key}:' \
                          f' {value}\n'
        result += f'{INDENT * depth}{CLOSE_BRACKET}'
        return result.strip()
    if isinstance(item, bool):
        return str(item).lower()
    if item is None:
        return 'null'
    return item


def make_stylish(tree: dict) -> str:
    """
    Function takes a tree(dict) and return str view in 'stylish' format.
    """
    def walk(node, depth):
        result = OPEN_BRACKET
        for key, value in node.items():
            action = value.get('action')
            cur_depth = depth + 1
            if action == 'nested':
                children = value.get('children')
                result += f'{INDENT * cur_depth}{key}:' \
                          f' {walk(children, cur_depth)}\n'
            else:
                new_value = value.get('value')
                old_value = value.get('old_value')
                actions = {
                    'update': f'{INDENT * depth}'
                              f'{REMOVE}{key}: '
                              f'{to_str(old_value, cur_depth)}\n'
                              f'{INDENT * depth}'
                              f'{ADD}{key}: '
                              f'{to_str(new_value, cur_depth)}\n',
                    'added': f'{INDENT * depth}'
                             f'{ADD}{key}: '
                             f'{to_str(new_value, cur_depth)}\n',
                    'removed': f'{INDENT * depth}'
                               f'{REMOVE}{key}: '
                               f'{to_str(new_value, cur_depth)}\n',
                    'unstaged': f'{INDENT * depth}'
                                f'{INDENT}{key}: '
                                f'{to_str(new_value, cur_depth)}\n'
                }
                result += actions[action]
        result += f'{INDENT * depth}{CLOSE_BRACKET}'
        return result.strip()
    return walk(tree, 0)
