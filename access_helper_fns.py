from helper_functions import list_files, upload_text_file
import os

# Example usage
directory = "C:/Users/User/Documents/DevRepos"
files = list_files(directory)
print("Text files found:", files)

for filename in files:
    filepath = os.path.join(directory, filename)
    content = upload_text_file(filepath)
    
    if content:
        print(f"\n Contents of {filename}:\n{content}")
    else:
        print(f"\n Could not read {filename}")
