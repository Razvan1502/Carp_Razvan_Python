import os
import sys

def count_files_by_extension(directory):
    try:

        if not os.path.isdir(directory):
            raise ValueError(f"Error: {directory} is not a valid directory path.")

        files = os.listdir(directory)

        # Check if directory is empty
        if not files:
            raise ValueError(f"Error: {directory} is an empty directory.")

        # dictionary to store counts for each file extension
        extension_counts = {}

        #count files by extension
        for filename in files:
            _, file_extension = os.path.splitext(filename)
            file_extension = file_extension.lower()  # Convert to lowercase for case-insensitivity


            extension_counts[file_extension] = extension_counts.get(file_extension, 0) + 1

        # Print the counts
        print("File counts by extension:")
        for extension, count in extension_counts.items():
            print(f"{extension}: {count} files")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    count_files_by_extension(directory_path)
