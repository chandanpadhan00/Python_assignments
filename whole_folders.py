import csv
import io
import chardet
import os
import shutil

def clean_column_name(name):
    return name.strip().replace('\n', '').replace('\r', '')

def remove_bom(text):
    return text.replace('\ufeff', '')

def replace_special_chars(text):
    replacements = {
        '¢': '™',
        'Â': '®',
        # Add more mappings as needed
    }
    
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def process_row(row):
    idmp_class = remove_bom(row.get('IDMP_CLASS', ''))
    physical_name = row.get('PHYSICAL_NAME', '')
    attribute_value = row.get('ATTRIBUTE_VALUE', '')
    product_key = row.get('PRODUCT_KEY', '')
    if row.get('3rd_LEvel_Number') == '1.13.3.1':
        row['2nd_Level_Name'] = 'ATC Code Flag'
        row['2nd_Level_Number'] = ''
        row['3rd_Level_Name'] = ''
        row['3rd_Level_Number'] = ''
    return row

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
    return chardet.detect(raw_data)['encoding']

def process_csv(input_file, output_file):
    input_encoding = detect_encoding(input_file)
    print(f"Processing file: {input_file}")
    print(f"Detected input file encoding: {input_encoding}")
    with open(input_file, 'r', encoding=input_encoding) as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = [clean_column_name(name) for name in reader.fieldnames]
        if 'ATTRIBUTE_SOURCE_VALUE' not in fieldnames:
            fieldnames.append('ATTRIBUTE_SOURCE_VALUE')
        
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        rows_processed = 0
        rows_deleted = 0
        for row in reader:
            cleaned_row = {clean_column_name(k): v for k, v in row.items()}
            new_row = process_row(cleaned_row)
            if new_row is not None:
                writer.writerow(new_row)
                rows_processed += 1
            else:
                rows_deleted += 1
    print(f"Processing complete. Output saved to {output_file}")
    print(f"Rows processed: {rows_processed}")
    print(f"Rows deleted: {rows_deleted}")
    print(f"Output file encoded as: UTF-8")
    print()

def process_directory(input_dir, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Process each CSV file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.csv'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            process_csv(input_path, output_path)

# Usage
input_directory = 'path/to/input/directory'  # Replace with your input directory path
output_directory = 'path/to/output/directory'  # Replace with your output directory path
process_directory(input_directory, output_directory)
