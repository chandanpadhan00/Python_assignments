import pandas as pd

# Step 1: Read the CSV file into a pandas DataFrame with specified encoding
df = pd.read_csv('table_1.csv', encoding='utf-8')

# Step 2: Define the replacement mapping for substrings
replacements = {
    "♡Â": "•○",
    "OLDPRODUCT1": "NEWPRODUCT1",  # Example substring replacement
    "OLDPRODUCT2": "NEWPRODUCT2",  # Example substring replacement
    # Add more replacements as needed
}

# Step 3: Apply the replacements throughout the entire DataFrame
df = df.astype(str)

# Apply each replacement using regex=True to handle substring replacements
for old_value, new_value in replacements.items():
    df = df.replace(to_replace=old_value, value=new_value, regex=True)

# Step 4: Save the updated DataFrame back to a CSV file with specified encoding
df.to_csv('table_1_updated.csv', index=False, encoding='utf-8')

print("Replacements applied successfully and CSV saved as 'table_1_updated.csv'.")