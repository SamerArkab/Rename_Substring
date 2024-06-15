import os

def rename_files_in_directory(directory, old_substring, new_substring):
    try:
        for filename in os.listdir(directory):
            old_file_path = os.path.join(directory, filename)
            
            # Check if it's a file (not a directory)
            if os.path.isfile(old_file_path):
                new_filename = filename.replace(old_substring, new_substring)
                new_file_path = os.path.join(directory, new_filename)
                
                os.rename(old_file_path, new_file_path)
                print(f'Renamed: {old_file_path} -> {new_file_path}')
    except Exception as e:
        print(f'An error occurred: {e}')

def main():
    directory = input("Enter the absolute path of the directory: ").strip()

    old_substring = ''
    while old_substring == '':
        old_substring = input("Enter the substring to replace: ").strip()
        if old_substring == '':
            print('Substring to replace can not be empty.')

    new_substring = input("Enter the new substring: ").strip()

    rename_files_in_directory(directory, old_substring, new_substring)

if __name__ == "__main__":
    main()
