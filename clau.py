import pandas as pd
import numpy as np
import re
import argparse

def process_csv(input_file, output_file, replacements):
    # Step 1: Read the CSV file into a pandas DataFrame
    try:
        df = pd.read_csv(input_file, encoding='utf-8', na_values=['', 'NA', 'N/A'], keep_default_na=False)
        print(f"Successfully read {input_file}")
        print("Initial data from CSV:")
        print(df.head())
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return

    # Step 2: Define a function to apply replacements
    def apply_replacements(text):
        if pd.isna(text):
            return text
        for old_value, new_value in replacements.items():
            text = re.sub(re.escape(old_value), new_value, str(text))
        return text

    # Step 3: Apply the replacements throughout the entire DataFrame
    for column in df.columns:
        df[column] = df[column].apply(apply_replacements)

    print("Data after replacements:")
    print(df.head())

    # Step 4: Save the updated DataFrame back to a CSV file
    try:
        df.to_csv(output_file, index=False, encoding='utf-8', na_rep='')
        print(f"Replacements applied successfully and CSV saved as '{output_file}'.")
    except Exception as e:
        print(f"Error saving the CSV file: {e}")

if __name__ == "__main__":
    # Default input and output file names
    default_input_file = 'table_1.csv'
    default_output_file = 'table_1_updated.csv'

    parser = argparse.ArgumentParser(description="Process a CSV file with custom replacements.")
    parser.add_argument("-i", "--input", help="Path to the input CSV file (default: %(default)s)", default=default_input_file)
    parser.add_argument("-o", "--output", help="Path to save the processed CSV file (default: %(default)s)", default=default_output_file)
    args = parser.parse_args()

    replacements = {
        "♡Â": "•○",
        "Â": "",
        "®": "(R)",
        "™": "(TM)",
        "|": "",
        # Add more replacements as needed
    }
    
    process_csv(args.input, args.output, replacements)
