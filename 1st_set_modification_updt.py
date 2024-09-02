import csv
import io
import chardet

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

    # Existing transformations
    if idmp_class in ['Marketing Authorisation', 'Marketing Authorisation Procedure'] and 'DT' in physical_name and attribute_value == 'N/A':
        row['ATTRIBUTE_VALUE'] = '1900-01-01'

    # New transformations
    if idmp_class == 'Medicinal Product' and physical_name == 'PRD_CLS_VAL_CD' and attribute_value.strip() == '':
        row['ATTRIBUTE_VALUE'] = ''

    if idmp_class == 'Medicinal Product' and physical_name == 'MED_REG_AGN_ORG_ID' and attribute_value.strip() == '':
        row['ATTRIBUTE_VALUE'] = 'ORG-2003'

    if idmp_class == 'Medicinal Product' and physical_name == 'MED_REG_AGN_LOC_ID' and attribute_value.strip() == '':
        row['ATTRIBUTE_VALUE'] = 'LOC-1006'

    # Updated conditions for points 4 and 5
    if idmp_class == 'Marketing Authorisation' and physical_name == 'MRKT_AUTH_HLDR_ORG_ID' and attribute_value is None:
        row['ATTRIBUTE_VALUE'] = ''

    if idmp_class == 'Marketing Authorisation' and physical_name == 'MRKT_AUTH_REGLTR_LOC_ID' and attribute_value is None:
        row['ATTRIBUTE_VALUE'] = ''

    # Replace single quotes with double single quotes
    if attribute_value and "'" in attribute_value:
        row['ATTRIBUTE_VALUE'] = attribute_value.replace("'", "''")

    # Set attribute_source_value equal to attribute_value
    row['ATTRIBUTE_SOURCE_VALUE'] = row['ATTRIBUTE_VALUE']

    # Apply special character replacement to all cells
    for key in row:
        if row[key]:
            row[key] = replace_special_chars(remove_bom(row[key]))

    # Check if the row should be deleted
    if 'DUMMY' in product_key.upper():
        return None  # Returning None will signal that this row should be skipped

    return row

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
    return chardet.detect(raw_data)['encoding']

def process_csv(input_file, output_file):
    input_encoding = detect_encoding(input_file)
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

# Usage
input_file = 'input.csv'  # Replace with your input file name
output_file = 'output.csv'  # Replace with your desired output file name

process_csv(input_file, output_file)
