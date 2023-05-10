def to_plain_str(item) -> str:
    """
    Convert data to str format.
    """
    if isinstance(item, dict):
        return '[complex value]'
    if item is None:
        return 'null'
    if isinstance(item, bool):
        return str(item).lower()
    else:
        return f"'{item}'"


def make_plain(tree: dict) -> str:
    """
    Function takes a tree(dict) and return str view in 'plain' format.
    """
    def walk(node, path):
        result = []
        for key, value in node.items():
            current_path = f"{path}.{key}" if path else key
            action = value.get('action')
            if action == 'nested':
                children = value.get('children')
                result.append(walk(children, current_path))
            else:
                actions = {'update': f"Property '{current_path}'"
                                     f" was updated. From "
                                     f"{to_plain_str(value.get('old_value'))}"
                                     f" to {to_plain_str(value.get('value'))}",
                           'added': f"Property '{current_path}'"
                                    f" was added with value:"
                                    f" {to_plain_str(value.get('value'))}",
                           'removed': f"Property '{current_path}' was removed"}
                if action == 'unstaged':
                    continue
                result.append(actions[action])
        return '\n'.join(result)

    return walk(tree, '')
