import csv
import io

def replace_special_chars(text):
    replacements = {
        '¢': '™',
        'Â': '®',
        # Add more mappings as needed
    }
    
    original_text = text
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    if original_text != text:
        print(f"Replaced: '{original_text}' -> '{text}'")
    
    return text

def process_row(row):
    idmp_class = row.get('IDMP_CLASS', '')
    physical_name = row.get('PHYSCIAL_NAME', '')  # Note: 'PHYSCIAL_NAME' typo is preserved as per your query
    attribute_value = row.get('ATTRIBUTE_VALUE', '')

    # Apply transformations based on SQL queries
    if idmp_class in ['Marketing Authorisation', 'Marketing Authorisation Procedure'] and 'DT' in physical_name and attribute_value == 'N/A':
        row['ATTRIBUTE_VALUE'] = '1900-01-01'
        print(f"Updated date for {idmp_class} with {physical_name}")

    # Replace single quotes with double single quotes
    if "'" in attribute_value:
        row['ATTRIBUTE_VALUE'] = attribute_value.replace("'", "''")
        print(f"Replaced single quotes: '{attribute_value}' -> '{row['ATTRIBUTE_VALUE']}'")

    # Set attribute_source_value equal to attribute_value
    row['ATTRIBUTE_SOURCE_VALUE'] = row['ATTRIBUTE_VALUE']

    # Apply special character replacement to all cells
    for key in row:
        row[key] = replace_special_chars(row[key])

    return row

def process_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8-sig') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = [name.strip().upper() for name in reader.fieldnames]
        if 'ATTRIBUTE_SOURCE_VALUE' not in fieldnames:
            fieldnames.append('ATTRIBUTE_SOURCE_VALUE')
        
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            new_row = process_row(row)
            writer.writerow(new_row)

# Usage
input_file = 'input.csv'  # Replace with your input file name
output_file = 'output_processed.csv'  # Replace with your desired output file name

process_csv(input_file, output_file)
print(f"Processing complete. Output saved to {output_file}")
print("Check the console output for any replacements or updates made.")
