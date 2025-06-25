def file_read(filepath : str) -> str:
    with open(filepath, 'r') as f:
        return f.read()
    
def file_write(filepath : str, data : str):
    with open(filepath, 'w') as f:
        f.write(data)
    
def file_create(filepath : str, data : str):
    with open(filepath, 'x') as f:
        f.write(data)

# file_read / file_write related
def json_read(filepath : str) -> dict | list:
    return json.load(file_read(filepath))
    
def json_write(filepath : str, data : dict | list):
    file_write(filepath,json.dumps(data))

# Standalone

def json_read(filepath : str) -> dict | list:
    with open(filepath, 'r') as f:
        return json.loads(f)
    
def json_write(filepath : str, data : dict | list):
    with open(filepath, 'w') as f:
        f.write(json.dumps(data))