import csv
import io
import chardet

def replace_special_chars(text):
    # Define your replacement mappings here
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
    print(f"Detected input file encoding: {input_encoding}")

    with open(input_file, 'r', encoding=input_encoding) as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            new_row = [replace_special_chars(cell) for cell in row]
            writer.writerow(new_row)

    print(f"Output file encoded as: UTF-8")

# Usage
input_file = 'input.csv'  # Replace with your input file name
output_file = 'output.csv'  # Replace with your desired output file name

process_csv(input_file, output_file)
print(f"Processing complete. Output saved to {output_file}")
