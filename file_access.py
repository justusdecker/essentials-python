def file_read(filepath : str) -> str:
    """
    Opens a file, read & return the content.
    Raises `FileNotFoundError` if file not exist.
    """
    with open(filepath, 'r') as f:
        return f.read()
    
def file_write(filepath : str, data : str):
    """
    Opens a file, writes the given data into it.
    Creates a new file if not exist.
    """
    with open(filepath, 'w') as f:
        f.write(data)
    
def file_create(filepath : str, data : str):
    """
    Opens a file, writes the given data into it.
    Raises `FileExistsError` if file exist.
    """
    with open(filepath, 'x') as f:
        f.write(data)

# file_read / file_write related
def json_read(filepath : str) -> dict | list:
    """
    It uses `file_read` to read the file.
    Returns a dict or list.
    Raises `FileNotFoundError` if file not exist.
    Raises `JSONDecodeError` if content is corrupted
    """
    return json.load(file_read(filepath))
    
def json_write(filepath : str, data : dict | list):
    """
    It uses `file_write` to write to the file.
    Raises an Exeption if unsupported types are given. Classes, Functions etc.
    """
    file_write(filepath,json.dumps(data))

# Standalone

def json_read(filepath : str) -> dict | list:
    """
    Opens a json file, read & return the content as dict or list
    Raises `FileNotFoundError` if file not exist.
    Raises `JSONDecodeError` if content is corrupted
    """
    with open(filepath, 'r') as f:
        return json.loads(f)
    
def json_write(filepath : str, data : dict | list):
    """
    Opens a json file, writes the given data into it.
    Creates a new json file if not exist.
    Raises an Exeption if unsupported types are given. Classes, Functions etc.
    """
    with open(filepath, 'w') as f:
        f.write(json.dumps(data))