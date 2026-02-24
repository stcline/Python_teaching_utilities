# This script scans a specified directory and compares the sizes of files within it. It prints out the files that are the within 1% of another file's size.
import os
def compare_file_sizes(directory):
    file_sizes = {}
    
    # Walk through the directory and get file sizes
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path)
            file_sizes[file_path] = size
    
    # Compare file sizes
    for file1, size1 in file_sizes.items():
        for file2, size2 in file_sizes.items():
            if file1 != file2:
                if abs(size1 - size2) / max(size1, size2) < 0.01:  # Check if sizes are within 1%
                    print(f"{file1} and {file2} are within 1% of each other's size.")
# Example usage
directory_to_scan = "H:\My Drive\Classroom\PLTW-DigElectHB - Cline - 6 6\3.2.1 - Asynchronous Counters"
compare_file_sizes(directory_to_scan)