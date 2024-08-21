import cx_Oracle
import pandas as pd
import os

# Set up Oracle connection details
dsn_tns = cx_Oracle.makedsn('hostname', 'port', service_name='service_name') # Adjust as necessary
connection = cx_Oracle.connect(user='username', password='password', dsn=dsn_tns)

# Directory where CSV files will be saved
output_directory = r"C:\Users\cpadhan\OneDrive - Amgen\Extracted_files"

# List of queries to execute, each with a corresponding table name for the output file
queries = {
    "table1": "SELECT column1, column2, column3 FROM table1",
    "table2": "SELECT column1, column2, column3, column4 FROM table2",
    # Add all your 43 queries here
    "table43": "SELECT column1, column2, column3 FROM table43"
}

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

try:
    for table_name, query in queries.items():
        # Execute the query
        df = pd.read_sql(query, con=connection)

        # Define the output file path
        output_file = os.path.join(output_directory, f"{table_name}.csv")

        # Export the result to a CSV file
        df.to_csv(output_file, index=False)
        print(f"Data exported successfully to {output_file}")
finally:
    # Close the database connection
    connection.close()