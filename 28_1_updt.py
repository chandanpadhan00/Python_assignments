import csv
import io
import os
import chardet

def replace_special_chars(text):
    replacements = {
        '¢': '™',
        'Â': '®',
        # Add more mappings as needed
    }
    
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
    return chardet.detect(raw_data)['encoding']

def process_csv(input_file, output_file):
    input_encoding = detect_encoding(input_file)
    
    with open(input_file, 'r', encoding=input_encoding) as infile, \
         open(output_file, 'w', newline='', encoding=input_encoding) as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            new_row = [replace_special_chars(cell) for cell in row]
            writer.writerow(new_row)

# Usage
input_file = 'input.csv'  # Replace with your input file name
output_file = os.path.splitext(input_file)[0] + '_processed' + os.path.splitext(input_file)[1]

process_csv(input_file, output_file)
print(f"Processing complete. Output saved to {output_file}")
