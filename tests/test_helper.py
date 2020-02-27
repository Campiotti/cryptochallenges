from typing import IO
import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def get_str(file: IO) -> str:
    content_arr = file.readlines()
    content_str = ''.join(content_arr)
    file.close()
    return content_str


def get_file_as_str(path: str) -> str:
    return get_str(open(path, 'r'))
