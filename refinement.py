import pandas as pd

# Step 1: Read the CSV file into a pandas DataFrame with specified encoding
df = pd.read_csv('table_1.csv', encoding='utf-8')

# Step 2: Define the replacement mapping for substrings
replacements = {
    "AMGEVITA♡Â": "AMGEVITA•○",
    "OLDPRODUCT1": "NEWPRODUCT1",  # Example replacement
    "OLDPRODUCT2": "NEWPRODUCT2",  # Example replacement
    # Add more replacements as needed
}

# Step 3: Apply the replacements throughout the entire DataFrame
# Convert all DataFrame values to string for accurate replacement
df = df.astype(str)

# Iterating through each replacement pair
for old_value, new_value in replacements.items():
    # Using regex=True to search and replace substrings
    df = df.replace(to_replace=old_value, value=new_value, regex=True)

# Step 4: Save the updated DataFrame back to a CSV file with specified encoding
df.to_csv('table_1_updated.csv', index=False, encoding='utf-8')

print("Replacements applied successfully and CSV saved as 'table_1_updated.csv'.")