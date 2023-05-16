import json
import yaml


def parse(data, extension):
    if extension == 'json':
        return json.loads(data)
    elif extension == 'yaml' or extension == 'yml':
        return yaml.safe_load(data)
    else:
        raise Exception('Unsupported file format!')
