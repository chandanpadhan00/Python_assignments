import pandas as pd
import re

# Step 1: Read the CSV file into a pandas DataFrame with specified encoding
df = pd.read_csv('table_1.csv', encoding='utf-8')

# Debug: Check the first few rows of the DataFrame to ensure it is read correctly
print("Initial data from CSV:")
print(df.head())

# Step 2: Define the replacement mapping for substrings
# Include any special characters you want to replace
replacements = {
    "♡Â": "•○",  # Example replacement
    "Â": "",     # Remove unwanted special character
    "®": "(R)",  # Replace registered trademark symbol with text
    "™": "(TM)", # Replace trademark symbol with text
    "|": "",     # Remove vertical line symbol
    # Add more replacements as needed
}

# Step 3: Apply the replacements throughout the entire DataFrame
df = df.astype(str)

# Apply each replacement using regex=True to handle substring replacements
for old_value, new_value in replacements.items():
    # Debug: Print the current replacement being performed
    print(f"Replacing '{old_value}' with '{new_value}'")
    
    # Escaping old_value to treat it as a literal string if needed
    old_value = re.escape(old_value)
    df = df.replace(to_replace=old_value, value=new_value, regex=True)

# Debug: Check if replacements were successful by examining a few rows again
print("Data after replacements:")
print(df.head())

# Step 4: Save the updated DataFrame back to a CSV file with specified encoding
df.to_csv('table_1_updated.csv', index=False, encoding='utf-8')

print("Replacements applied successfully and CSV saved as 'table_1_updated.csv'.")