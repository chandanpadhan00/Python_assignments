import csv

def clean_column_name(name):
    return name.strip().replace('\n', '').replace('\r', '')

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
    idmp_class = remove_bom(row.get('idmp_class', ''))
    physical_name = row.get('physcial_name', '')  # Typo preserved as per your query
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
        original = row[key]
        row[key] = replace_special_chars(remove_bom(row[key]))
        print(f"Original: {original} -> Replaced: {row[key]}")  # Debug print

    return row

def process_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8-sig') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = [clean_column_name(name) for name in reader.fieldnames]
        if 'attribute_source_value' not in fieldnames:
            fieldnames.append('attribute_source_value')
        
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            # Clean column names in each row
            cleaned_row = {clean_column_name(k): v for k, v in row.items()}
            new_row = process_row(cleaned_row)
            
            # Ensure all modifications are properly written
            if 'attribute_source_value' not in new_row:
                new_row['attribute_source_value'] = new_row['attribute_value']
            
            # Debug print to check final row before writing
            print(f"Writing row: {new_row}")  # Debug print
            writer.writerow(new_row)

# Usage
input_file = 'input.csv'  # Replace with your input file name
output_file = 'output.csv'  # Replace with your desired output file name

process_csv(input_file, output_file)
print(f"Processing complete. Output saved to {output_file}")