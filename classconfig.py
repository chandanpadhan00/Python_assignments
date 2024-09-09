import pandas as pd
import json

# Step 1: Load the CSV file
df = pd.read_csv('medicinal_product.csv')

# Step 2: Initialize an empty dictionary for the JSON structure
json_structure = {
    "medicinal_product": {
        "IDMP_CLASS": "Medicinal Product",
        "ENTITY_NAME": "MedicinalProduct",
        "ATTR_REF": {}
    }
}

# Step 3: Iterate over rows to populate the JSON structure
for index, row in df.iterrows():
    attr_key = row['PHYSICAL_NAME']
    json_structure["medicinal_product"]["ATTR_REF"][row['ATTRIBUTE_NAME']] = {
        "ATTRIBUTE_NAME": row['ATTRIBUTE_NAME'],
        "PHYSICAL_NAME": row['PHYSICAL_NAME'],
        "TYPE": row['TYPE']
    }
    
    # Add IDMP_LEVEL if it exists
    if not pd.isnull(row['IDMP_LEVEL']):
        json_structure["medicinal_product"]["ATTR_REF"][row['ATTRIBUTE_NAME']]["IDMP_LEVEL"] = row['IDMP_LEVEL']

# Step 4: Convert the dictionary to a JSON object
json_output = json.dumps(json_structure, indent=4)

# Output the JSON configuration
print(json_output)