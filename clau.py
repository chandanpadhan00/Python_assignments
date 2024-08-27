import pandas as pd
import numpy as np
import re

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

# File names and replacements
input_file = 'table_1.csv'
output_file = 'table_1_updated.csv'
replacements = {
    "♡Â": "•○",
    "Â": "",
    "®": "(R)",
    "™": "(TM)",
    "|": "",
    # Add more replacements as needed
}

# Run the process
process_csv(input_file, output_file, replacements)
