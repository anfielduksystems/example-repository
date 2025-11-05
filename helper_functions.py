import os
def list_files(directory, extension=".txt"):
    """
    Lists all files with a given extension in the specified directory.
    """
    try:
        return [f for f in os.listdir(directory) if f.endswith(extension)]
    except FileNotFoundError:
        print(f"Directory not found: {directory}")
        return []

def upload_text_file(filepath):
    """
    Reads and returns the contents of a text file.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None