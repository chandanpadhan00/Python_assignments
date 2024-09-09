import pandas as pd
import json

# Step 1: Load the CSV file
df = pd.read_csv('your_file.csv')

# Step 2: Infer the data types
data_types = df.dtypes

# Step 3: Create a class configuration in JSON format
class_config = {}
for column, dtype in data_types.items():
    # Mapping pandas dtypes to JSON-compatible data types
    if pd.api.types.is_integer_dtype(dtype):
        json_type = 'integer'
    elif pd.api.types.is_float_dtype(dtype):
        json_type = 'float'
    elif pd.api.types.is_bool_dtype(dtype):
        json_type = 'boolean'
    else:
        json_type = 'string'
    
    class_config[column] = {"type": json_type}

# Step 4: Convert the dictionary to a JSON object
json_config = json.dumps(class_config, indent=4)

# Output the JSON configuration
print(json_config)