import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


def do_cmd(cmd: str, value: str, data: list[str]) -> list[str]:
    """ Обрабатывает запрос с командами """
    if cmd == 'filter':
        result = filter(lambda line: value in line, data)
        return list(result)
    elif cmd == 'map':
        result = map(lambda line: line.split()[int(value)], data)
        return list(result)
    elif cmd == 'unique':
        result = set(data)
        return list(result)
    elif cmd == 'sort':
        reverse = (value == 'desc')
        result = sorted(data, reverse=reverse)
        return result
    elif cmd == 'limit':
        result = data[:int(value)]
        return result
    elif cmd == 'regex':
        regex = re.compile(value)
        return list(filter(lambda v: regex.search(v), data))


def do_query(params: dict) -> list[str]:
    """ Считывает файл и возвращает обработанный результат """
    with open(os.path.join(DATA_DIR, params['file_name'])) as f:
        file_data = f.readlines()  # f.read().split('\n')
    result = file_data
    if "cmd1" in params.keys():
        result = do_cmd(params['cmd1'], params['value1'], result)
    if "cmd2" in params.keys():
        result = do_cmd(params['cmd2'], params['value2'], result)
    return result
