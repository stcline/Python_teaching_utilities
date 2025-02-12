import os
import difflib
import csv
import tokenize
import io

def tokenize_file(filename):
    """Tokenize a Python file and return a list of tokens."""
    with open(filename, 'r') as f:
        source_code = f.read()
    tokens = []
    g = tokenize.tokenize(io.BytesIO(source_code.encode('utf-8')).readline)
    for toknum, tokval, _, _, _ in g:
        if toknum not in (tokenize.COMMENT, tokenize.NL, tokenize.INDENT, tokenize.DEDENT, tokenize.NEWLINE):
            tokens.append(tokval)
    return tokens

def compare_token_lists(tokens1, tokens2):
    """Compare two lists of tokens and calculate their similarity percentage."""
    similarity = difflib.SequenceMatcher(None, tokens1, tokens2).ratio()
    return round(similarity * 100, 2)

def compare_files(file1, file2):
    """Tokenize and compare two files, returning a similarity percentage."""
    tokens1 = tokenize_file(file1)
    tokens2 = tokenize_file(file2)
    return compare_token_lists(tokens1, tokens2)

def compare_multiple_files(directory, output_csv):
    """Compare all Python files in a directory using tokenization and write the results to a CSV file."""
    python_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.py')]

    results = []
    for i in range(len(python_files)):
        for j in range(i + 1, len(python_files)):
            file1 = python_files[i]
            file2 = python_files[j]
            similarity = compare_files(file1, file2)
            results.append([os.path.basename(file1), os.path.basename(file2), similarity])

    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['File 1', 'File 2', 'Similarity (%)'])
        writer.writerows(results)

if __name__ == "__main__":
    directory = "D:\Documents\Python Scripts\Python_teaching_utilities\Comparing_Scripts\compares"
    output_csv = "similarities_tokenized.csv"
    compare_multiple_files(directory, output_csv)
    print(f"Comparison completed. Results saved to {output_csv}.")
