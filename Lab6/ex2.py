import os
import sys

def rename_files_with_prefix(directory):
    try:

        if not os.path.isdir(directory):
            raise ValueError(f"Error: {directory} is not a valid directory path.")


        files = os.listdir(directory)


        for index, filename in enumerate(files, start=1):
            old_path = os.path.join(directory, filename)
            new_filename = f"file{index}{os.path.splitext(filename)[1]}"
            new_path = os.path.join(directory, new_filename)

            try:
                os.rename(old_path, new_path)
                print(f"Renamed {filename} to {new_filename}")

            except Exception as e:
                print(f"Error renaming {filename}: {e}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    rename_files_with_prefix(directory_path)
