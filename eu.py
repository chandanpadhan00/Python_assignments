import os
import pandas as pd

# Specify the folder containing the CSV files
folder_path = "path/to/your/folder"

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)

        # Read the CSV file
        df = pd.read_csv(file_path)

        # Add the new column with all values as 'EU'
        df['Regulatory Authorisation'] = 'EU'

        # Save the updated dataframe back to the CSV file
        df.to_csv(file_path, index=False)

        print(f"Updated file: {filename}")

print("All files updated successfully!")