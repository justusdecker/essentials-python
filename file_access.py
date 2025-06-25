def file_read(filepath : str) -> str:
    """
    Opens a file, read & return the content.
    Raises `FileNotFoundError` if file not exist.
    """
    with open(filepath, 'r') as f:
        return f.read()
    
def file_write(filepath : str, data : str) -> str:
    """
    Opens a file, writes the given data into it.
    Creates a new file if not exist.
    """
    with open(filepath, 'w') as f:
        return f.write(data)
    
def file_create(filepath : str, data : str) -> str:
    """
    Opens a file, writes the given data into it.
    Raises `FileExistsError` if file exist.
    """
    with open(filepath, 'x') as f:
        return f.write(data)
