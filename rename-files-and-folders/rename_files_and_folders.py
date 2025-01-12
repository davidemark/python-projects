import os
import re
import sys

def to_snake_case(name):
    """Convert a string to snake_case and lowercase."""
    name = re.sub(r'[^a-zA-Z0-9]', '_', name)  # Replace non-alphanumeric chars with _
    name = re.sub(r'_+', '_', name)  # Replace multiple underscores with a single one
    return name.lower()  # Convert to lowercase

def to_kebab_case(name):
    """Convert a string to kebab-case and lowercase."""
    name = re.sub(r'[^a-zA-Z0-9]', '-', name)  # Replace non-alphanumeric chars with -
    name = re.sub(r'-+', '-', name)  # Replace multiple hyphens with a single one
    return name.lower()  # Convert to lowercase

def transform_file_name(name):
    """Transform a string specifically for PDF and ZIP files."""
      
    # Step 1: Replace two or more consecutive spaces with `+-+`
    name = re.sub(r'\s{2,}', '+-+', name)
    
    # Step 2: Replace remaining single spaces with `+`
    name = re.sub(r'\s+', '+', name)
    
    # Step 3: Replace non-alphanumeric characters (except `+`) with `+`
    name = re.sub(r'[^a-zA-Z0-9+]', '+', name)
    
    # Step 4: Replace hyphens with plus signs
    name = name.replace('-', '+')  # Replace hyphens with plus signs

    # Step 5: Replace occurrences of `+++` with `+-+`
    name = name.replace('+++', '+-+')  # Replace `+++` with `+-+`
    
    # Step 6: Replace multiple consecutive `+` symbols with a single `+`
    name = re.sub(r'\++', '+', name)
    
    return name.lower()  # Convert to lowercase

def rename_files_and_folders(root_folder):
    programming_and_markup_extensions = {
        '.py', '.java', '.c', '.cpp', '.js', '.ts', '.html', '.css', 
        '.xml', '.json', '.yml', '.yaml', '.md', '.php', '.rb', '.sh',
        '.bat', '.pl', '.swift', '.cs', '.sql'
    }

    special_files_extensions = {
        '.pdf', '.zip', '.rtf', '.txt'
    }

    for root, dirs, files in os.walk(root_folder, topdown=False):
        # Rename files
        for file in files:
            old_path = os.path.join(root, file)
            file_name, file_ext = os.path.splitext(file)
            
            if file_ext.lower() in programming_and_markup_extensions:
                # Use snake_case for programming and markup language files
                new_name = to_snake_case(file_name) + file_ext.lower()
            elif file_ext.lower() in special_files_extensions:
                # Use special name convention for specific files
                new_name = transform_file_name(file_name) + file_ext.lower()
            else:
                # General transformation for files
                new_name = transform_file_name(file_name) + file_ext.lower()
            
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed file: {old_path} -> {new_path}")

        # Rename folders
        for folder in dirs:
            old_path = os.path.join(root, folder)
            new_name = to_kebab_case(folder)
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed folder: {old_path} -> {new_path}")

if __name__ == "__main__":
    # Check if a path was provided via CLI, else use default path
    if len(sys.argv) < 2:
        print("No path specified. Using default path: '/Users/davidemark/vault/to-rename'")
        folder_path = "/Users/davidemark/vault/to-rename"  # Set the default folder path
    else:
        folder_path = sys.argv[1]  # Use the path provided by the user via CLI
    
    # Check if the folder path is valid
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        rename_files_and_folders(folder_path)
    else:
        print(f"Invalid folder path: {folder_path}. Please provide a valid directory.")
