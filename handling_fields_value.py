import csv
import chardet
import codecs

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw = file.read()
        result = chardet.detect(raw)
    return result['encoding']

def process_csv(input_file, output_file):
    # Detect the file encoding
    encoding = detect_encoding(input_file)

    # Open the input file with the detected encoding
    with codecs.open(input_file, 'r', encoding=encoding) as infile:
        # Check for BOM and skip if present
        if infile.read(1) == '\ufeff':
            infile.seek(0)
        else:
            infile.seek(0)

        # Detect the dialect
        dialect = csv.Sniffer().sniff(infile.read(1024))
        infile.seek(0)

        # Read the CSV file
        reader = csv.DictReader(infile, dialect=dialect)
        fieldnames = reader.fieldnames

        # Prepare the output file
        with codecs.open(output_file, 'w', encoding=encoding) as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames, dialect=dialect)
            writer.writeheader()

            # Process each row
            for row in reader:
                if row['3rd_LEvel_Number'] == '1.13.3.1':
                    row['2nd_Level_Name'] = 'ATC Code Flag'
                    row['2nd_Level_Number'] = ''
                    row['3rd_Level_Name'] = ''
                    row['3rd_Level_Number'] = ''
                writer.writerow(row)

    print(f"File processed successfully. Output saved to {output_file}")

# Usage
input_file = 'path/to/your/input/file.csv'
output_file = 'path/to/your/output/file.csv'
process_csv(input_file, output_file)
