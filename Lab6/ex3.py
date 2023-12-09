import os
import sys


def calculate_total_size(directory):
    try:

        if not os.path.isdir(directory):
            raise ValueError(f"Error: {directory} is not a valid directory path.")

        total_size = 0


        for dirpath, _, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)

                try:

                    total_size += os.path.getsize(file_path)

                except Exception as e:
                    print(f"Error accessing file {file_path}: {e}")

        print(f"Total size of all files in {directory}: {total_size} bytes")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    calculate_total_size(directory_path)
