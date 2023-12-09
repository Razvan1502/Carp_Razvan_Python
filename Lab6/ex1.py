import os
import sys

def read_and_print_files(directory, file_extension):
    try:

        if not os.path.isdir(directory):
            raise ValueError(f"Error: {directory} is not a valid directory path.")


        for filename in os.listdir(directory):
            if filename.endswith(file_extension):
                file_path = os.path.join(directory, filename)

                try:

                    with open(file_path, 'r') as file:
                        print(f"Contents of {filename}:")
                        print(file.read())
                        print("=" * 40)

                except Exception as e:
                    print(f"Error reading file {filename}: {e}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_path> <file_extension>")
        sys.exit(1)

    directory_path = sys.argv[1]
    file_extension = sys.argv[2]

    read_and_print_files(directory_path, file_extension)
