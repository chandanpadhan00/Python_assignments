import csv
import io

def clean_column_name(name):
    return name.strip().replace('\n', '').replace('\r', '').upper()

def remove_bom(text):
    return text.replace('\ufeff', '')

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
    idmp_class = remove_bom(row.get('IDMP_CLASS', ''))
    physical_name = row.get('PHYSCIAL_NAME', '')  # Note: 'PHYSCIAL_NAME' typo is preserved as per your query
    attribute_value = row.get('ATTRIBUTE_VALUE', '')

    # Apply transformations based on SQL queries
    if idmp_class in ['Marketing Authorisation', 'Marketing Authorisation Procedure'] and 'DT' in physical_name and attribute_value == 'N/A':
        row['ATTRIBUTE_VALUE'] = '1900-01-01'

    # Replace single quotes with double single quotes
    if "'" in attribute_value:
        row['ATTRIBUTE_VALUE'] = attribute_value.replace("'", "''")

    # Set attribute_source_value equal to attribute_value
    row['ATTRIBUTE_SOURCE_VALUE'] = row['ATTRIBUTE_VALUE']

    # Apply special character replacement to all cells
    for key in row:
        row[key] = replace_special_chars(remove_bom(row[key]))

    return row

def process_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8-sig') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = [clean_column_name(name) for name in reader.fieldnames]
        if 'ATTRIBUTE_SOURCE_VALUE' not in fieldnames:
            fieldnames.append('ATTRIBUTE_SOURCE_VALUE')
        
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            # Clean column names in each row
            cleaned_row = {clean_column_name(k): v for k, v in row.items()}
            new_row = process_row(cleaned_row)
            writer.writerow(new_row)

# Usage
input_file = 'input.csv'  # Replace with your input file name
output_file = 'output.csv'  # Replace with your desired output file name

process_csv(input_file, output_file)
print(f"Processing complete. Output saved to {output_file}")
