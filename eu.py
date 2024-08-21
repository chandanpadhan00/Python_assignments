import os
import pandas as pd

# Specify the folder containing the CSV files
folder_path = "path/to/your/folder"

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        
        try:
            # Try reading the CSV file with utf-8 encoding
            df = pd.read_csv(file_path, encoding='utf-8')
        
        except UnicodeDecodeError:
            print(f"UnicodeDecodeError: Switching to ISO-8859-1 for {filename}")
            
            # If utf-8 fails, try ISO-8859-1 encoding
            df = pd.read_csv(file_path, encoding='ISO-8859-1')
        
        # Add the new column with all values as 'EU'
        df['Regulatory Authorisation'] = 'EU'
        
        # Save the updated dataframe back to the CSV file
        # You can use the same encoding that worked for reading
        df.to_csv(file_path, index=False, encoding='utf-8')
        
        print(f"Updated file: {filename}")

print("All files processed successfully!")