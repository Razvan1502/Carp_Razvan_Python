import os
import sys

def function(directory):
    try:
        if not os.path.isdir(directory):
            raise ValueError(f"Error: {directory} is not a valid directory path.")

        for dirpath, _, filenames in os.walk(directory):
            for filename in filenames:
                longest = max(filename, key=lambda file: (len(file), file))
                shortest = min(filename, key=lambda file: (len(file), file))
                    if filename[1] == "c":
                        print(f"File: {filename} has a name that starts with c.")

             file_count_by_extension = {}
            _, extension = os.path.splitext(filename)

             if extension in file_count_by_extension:
                file_count_by_extension[extension] += 1
             else:
                file_count_by_extension[extension] = 1

             return file_count_by_extensio


    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("write: python script.py <directory_path> ")
        sys.exit(1)

    directory_path = sys.argv[1]
    function(directory_path)

