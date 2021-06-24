from re import compile, IGNORECASE
from os.path import isfile
from sys import version_info
if not version_info < (3, 4):
    from pathlib import Path
else:
    Path = None

URL_REGEX = compile(
    r'^(?:http|ftp)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
    r'localhost|' #localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', IGNORECASE
)

def is_url(url: str):
    url = str(url)
    return URL_REGEX.match(url) is not None

def is_file(filepath):
    if Path is not None:
        return isinstance(filepath, (bytes, str, Path)) and isfile(filepath)
    else:
        return isinstance(filepath, (bytes, str)) and isfile(filepath)