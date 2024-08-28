import csv
import io
from datetime import datetime

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

def process_row(row):
    idmp_class = row.get('idmp_class', '')
    physical_name = row.get('physcial_name', '')  # Note: 'physcial_name' typo is preserved as per your query
    attribute_value = row.get('attribute_value', '')

    # Apply transformations based on SQL queries
    if idmp_class in ['Marketing Authorisation', 'Marketing Authorisation Procedure'] and 'DT' in physical_name and attribute_value == 'N/A':
        row['attribute_value'] = '1900-01-01'

    # Replace single quotes with double single quotes
    if "'" in attribute_value:
        row['attribute_value'] = attribute_value.replace("'", "''")

    # Set attribute_source_value equal to attribute_value
    row['attribute_source_value'] = row['attribute_value']

    # Apply special character replacement to all cells
    for key in row:
        row[key] = replace_special_chars(row[key])

    return row

def process_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['attribute_source_value'] if 'attribute_source_value' not in reader.fieldnames else reader.fieldnames
        
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            new_row = process_row(row)
            writer.writerow(new_row)

# Usage
input_file = 'input.csv'  # Replace with your input file name
output_file = 'output.csv'  # Replace with your desired output file name

process_csv(input_file, output_file)
print(f"Processing complete. Output saved to {output_file}")
