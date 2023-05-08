def build_diff(dict1: dict, dict2: dict) -> dict:
    """
    Function takes two dictionary and return
    dictionary(tree) for further formatting.
    """
    added = dict2.keys() - dict1.keys()
    removed = dict1.keys() - dict2.keys()
    common = dict1.keys() | dict2.keys()
    node = {}
    for key in sorted(common):
        if key in added:
            node[key] = {'action': 'added',
                         'value': dict2[key]}
        elif key in removed:
            node[key] = {'action': 'removed',
                         'value': dict1[key]}
        elif dict1[key] == dict2[key]:
            node[key] = {'action': 'unstaged',
                         'value': dict1[key]}
        elif isinstance(dict1[key], dict) and\
                isinstance(dict2[key], dict):
            children = build_diff(dict1[key], dict2[key])
            node[key] = {'action': 'nested',
                         'children': children}
        else:
            node[key] = {'action': 'update',
                         'value': dict2[key],
                         'old_value': dict1[key]}
    return node
