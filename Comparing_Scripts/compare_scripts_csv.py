import os
import difflib
import csv

def compare_files(file1, file2):
    """
    Compare two files and calculate their similarity percentage.
    """
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        content1 = f1.read()
        content2 = f2.read()
    
    # Use difflib to calculate similarity
    similarity = difflib.SequenceMatcher(None, content1, content2).ratio()
    return round(similarity * 100, 2)

def compare_multiple_files(directory, output_csv):
    """
    Compare all Python files in a directory and write the results to a CSV file.
    """
    # Get all Python files in the directory
    python_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.py')]
    
    # Prepare results for CSV
    results = []
    for i in range(len(python_files)):
        for j in range(i + 1, len(python_files)):
            file1 = python_files[i]
            file2 = python_files[j]
            similarity = compare_files(file1, file2)
            results.append([os.path.basename(file1), os.path.basename(file2), similarity])
    
    # Write results to CSV
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['File 1', 'File 2', 'Similarity (%)'])
        writer.writerows(results)

if __name__ == "__main__":
    # Specify the directory containing Python files and the output CSV file
    directory = "D:\Documents\Python Scripts\Python_teaching_utilities\Comparing_Scripts\compares"  # Files to be compared
    output_csv = "similarities.csv"
    
    # Run the comparison
    compare_multiple_files(directory, output_csv)
    print(f"Comparison completed. Results saved to {output_csv}.")
